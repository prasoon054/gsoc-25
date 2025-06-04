#define _GNU_SOURCE
#include <stdio.h>
#include <signal.h>
#include <unistd.h>
#include <errno.h>
#include <linux/futex.h>
#include <sys/syscall.h>
#include <sys/time.h>
#include <pthread.h>

static int futex_var = 0;

/* Wait on futex until futex_var != 0 */
static int futex_wait(volatile int *uaddr) {
    return syscall(SYS_futex, (void*)uaddr, FUTEX_WAIT | FUTEX_PRIVATE_FLAG, 0, NULL, NULL, 0);
}

/* Wake exactly one waiter on futex_var */
static int futex_wake(volatile int *uaddr) {
    return syscall(SYS_futex, (void*)uaddr, FUTEX_WAKE | FUTEX_PRIVATE_FLAG, 1, NULL, NULL, 0);
}

/* Runs as SIGINT handler */
static void interrupt_handler(int sig) {
    (void)sig;
    /* Mark futex_var so the waiter passes the comparison */
    futex_var = 1;
    /* Wake the thread blocked in futex_wait() */
    futex_wake(&futex_var);
}

/* This thread sleeps 2s, then sends SIGINT to the process group */
static void *sig_sender(void *arg) {
    (void)arg;
    sleep(2);
    /* Issue SIGINT to ourselves (PID 1 inside the unikernel) */
    kill(getpid(), SIGINT);
    return NULL;
}

int main(void) {
    struct sigaction sa;
    pthread_t tid;

    /* 1) Install our SIGINT handler */
    sa.sa_handler = interrupt_handler;
    sigemptyset(&sa.sa_mask);
    sa.sa_flags = 0;
    if (sigaction(SIGINT, &sa, NULL) == -1) {
        perror("sigaction");
        return 1;
    }

    /* 2) Spawn a thread that will send SIGINT after 2 seconds */
    if (pthread_create(&tid, NULL, sig_sender, NULL) != 0) {
        perror("pthread_create");
        return 1;
    }

    printf("PID %d: waiting on futex; sending SIGINT in 2 seconds…\n",
           getpid());

    /* 3) Wait on futex (blocks until futex_var != 0 or signalled) */
    int rc;
    while (1) {
        rc = futex_wait(&futex_var);
        if (rc == 0) {
            /* Futex_WAKE won: futex_var changed to 1 inside handler */
            break;
        }
        if (errno == EINTR) {
            /* Interrupted by a handler, retry the wait */
            continue;
        }
        if (errno == EAGAIN) {
            /* futex_var already != 0, so treat as “woken” */
            break;
        }
        perror("futex_wait");
        return 1;
    }

    printf("Woken up by signal handler!\n");
    return 0;
}
