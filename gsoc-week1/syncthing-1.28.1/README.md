# syncthing 1.28.1
- Run `alpine` on docker.
```bash
docker run -it \
  -p 8384:8384 \
  -p 22000:22000 \
  -p 22000:22000/udp \
  -p 21027:21027/udp \
  alpine /bin/sh
```
- Install `syncthing` inside docker.
```sh
apk update && apk add strace syncthing
```
- Run `syncthing` under `strace`
```sh
strace syncthing -gui-address="0.0.0.0:8384" 2> /tmp/strace_out.log
```
- GUI available at `http://localhost:8384`
---
## Unsupported System Calls
- Following system calls were used by syncthing, but not implemented in Unikraft
  - `brk`
  - `clone`
  - `execve`
  - `fchmodat`
  - `inotify_add_watch`
  - `inotify_init1`
  - `inotify_rm_watch`
  - `ioprio_set`
  - `pidfd_open`
  - `pidfd_send_signal`
  - `readlinkat`
  - `recvmmsg`
  - `rt_sigreturn`
