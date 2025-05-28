# gitea 1.23.8

## Unsupported System Calls
- The following system calls which were used by etcd are not supported in Unikraft:
    - `brk`
    - `clone`
    - `execve`
    - `faccessat2`
    - `fchmodat`
    - `linkat`
    - `pidfd_open`
    - `pidfd_send_signal`
    - `readlinkat`
    - `restart_syscall`
    - `rt_sigreturn`
    - `sendfile`
    - `symlinkat`
