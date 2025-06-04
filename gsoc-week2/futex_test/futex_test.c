#define _GNU_SOURCE
#include <stdio.h>
#include <signal.h>
#include <unistd.h>
#include <errno.h>
#include <linux/futex.h>
#include <sys/syscall.h>
#include <sys/time.h>

static int futex_var = 0;

static int futex_wait(volatile int *uaddr) {
    return syscall(SYS_futex, uaddr, FUTEX_WAIT | FUTEX_PRIVATE_FLAG, 0, NULL, NULL, 0);
}

static int futex_wake(volatile int *uaddr) {
    return syscall(SYS_futex, uaddr, FUTEX_WAKE | FUTEX_PRIVATE_FLAG, 1, NULL, NULL, 0);
}

static void interrupt_handler(int sig) {
    (void)sig;
    printf("Handler ran!!\n");
    futex_var = 1;
    futex_wake(&futex_var);
}

int main(void) {
    struct sigaction sa;
    sa.sa_handler = interrupt_handler;
    sigemptyset(&sa.sa_mask);
    sa.sa_flags = 0;
    if (sigaction(SIGINT, &sa, NULL) == -1) {
        perror("sigaction");
        return 1;
    }
    printf("PID %d: waiting on futex; press Ctrl+C to wake it\n", getpid());
    int rc;
    while (1) {
        rc = futex_wait(&futex_var);
        if (rc == 0) {
            break;
        }
        if (errno == EINTR) {
            continue;
        }
        if (errno == EAGAIN) {
            break;
        }
        perror("futex_wait");
        return 1;
    }
    printf("Woken up by signal handler!\n");
    return 0;
}
