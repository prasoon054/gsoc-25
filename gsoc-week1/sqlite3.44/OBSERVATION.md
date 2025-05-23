# Observations
## Observations from running using docker (strace output)
- First few lines in [`strace_out.txt`](strace_out.txt) do not have system calls specific to `SQLite`.
    - `execve`, `arch_prctl`, `set_tid_address`, `brk`, `mmap(line 6)` are related to \
    setting up the sqlite process and memory region for it.
- All the system calls except the ones in last point are written in [`uniq_syscalls.txt`](uniq_syscalls.txt).
- All other system calls are implemented already in unikraft.
## Observations from running using kraft
- System call logs, when trying to run with 1024M memory is written in [`kraft_syscall.log`](kraft_syscall.log)
- Keeps waiting on [futex](https://man7.org/linux/man-pages/man2/futex.2.html) system call (Waits until a certain condition is true)
    - What is the condition, our example keeps waiting on?
    - Waiting to have a value of 0x80 on some address when trying to register signal handler for `SIGINT`
    - Why?
