# gitea 1.23.8

## Unsupported System Calls
- The following system calls which were used by etcd are not supported in Unikraft:
    - `clone`
    - `faccessat2`
    - `readlinkat`
    - `rt_sigreturn`
