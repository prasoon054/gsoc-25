#include <sys/mman.h>
#include <sys/wait.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    const size_t SIZE = sizeof(int);
    int *shared = mmap(NULL, SIZE, PROT_READ | PROT_WRITE, MAP_SHARED | MAP_ANONYMOUS, -1, 0);
    if (shared == MAP_FAILED) {
        perror("mmap");
        exit(EXIT_FAILURE);
    }
    pid_t pid = fork();
    if (pid < 0) {
        perror("fork");
        exit(EXIT_FAILURE);
    }
    if (pid == 0) {
        *shared = 1234;
        printf("Child: wrote %d\n", *shared);
        _exit(EXIT_SUCCESS);
    } else {
        wait(NULL);
        printf("Parent: read %d\n", *shared);
    }
    munmap(shared, SIZE);
    return 0;
}
