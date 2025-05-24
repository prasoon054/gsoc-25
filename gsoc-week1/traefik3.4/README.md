# traefik 3.4
- Used the application in [`app`](app/server.py) directory

## Unsupported System Calls
- These system calls were used by traefik which is not supported in Unikraft:
    - `clone`
    - `inotify_add_watch`
    - `inotify_init1`
    - `readlinkat`
    - `rt_sigreturn`
