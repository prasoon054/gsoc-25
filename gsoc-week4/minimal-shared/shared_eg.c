#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
    const char *path = "example.txt";
    const size_t SIZE = 4096;
    int fd = open(path, O_RDWR | O_CREAT, 0666);
    if (fd < 0) {
        perror("open");
        return -1;
    }
    if (ftruncate(fd, SIZE) == -1) {
        perror("ftruncate");
        close(fd);
        return -1;
    }
    char *addr = mmap(NULL, SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);
    if (addr == MAP_FAILED) {
        perror("mmap");
        close(fd);
        return -1;
    }
    const char *msg = "Hello, file-backed mmap!";
    memcpy(addr, msg, strlen(msg));
    if (msync(addr, SIZE, MS_SYNC) == -1) {
        perror("msync");
    }
    munmap(addr, SIZE);
    close(fd);
    return 0;
}
