# netdata 2.5.0-93-nightly
## How to replicate?
- Start the container.
```bash
docker run -it -p 19999:19999 --entrypoint /bin/sh netdata/netdata
```
- Start netdata under `strace`.
```sh
apt update && apt install strace
strace netdata 2> /tmp/strace_out.log
```
- Access dashboard on `http://localhost:19999`
- Perform CPU stress test to generate some visible metrics.
```sh
docker exec -it <container-id> /bin/sh
yes > /dev/null &
killall yes
```
---
## Unsupported System Calls
- Following system calls were used by netdata but not supported in Unikraft:
    - `brk`
    - `clock_adjtime`
    - `clone`
    - `close_range`
    - `execve`
    - `faccessat2`
    - `fchmodat`
    - `fchownat`
    - `get_mempolicy`
    - `linkat`
    - `mknodat`
    - `personality`
    - `pidfd_open`
    - `pidfd_send_signal`
    - `readlinkat`
    - `restart_syscall`
    - `rseq`
    - `rt_sigreturn`
    - `sched_getscheduler`
    - `semctl`
    - `sendmmsg`
    - `set_robust_list`
    - `statx`
