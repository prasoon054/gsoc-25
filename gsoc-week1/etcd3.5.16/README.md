# etcd 3.5.16
- Pulled the latest `alpine` linux image from `Dockerhub`.
```bash
docker pull alpine:latest
docker run -it -p 2379:2379 -p 2380:2380 /bin/sh
```
- Installed `etcd` using package manager (inside container)
```sh
apk update && apk add etcd
```
- Launched etcd under `strace`
```sh
strace etcd --data-dir /etcd-data --listen-client-urls http://0.0.0.0:2379 \
--advertise-client-urls http://0.0.0.0:2379 2> /tmp/strace_out.log
```
- On host machine, ran [`etcd_app.py`](app/etcd_app.py)
```bash
pip install etcd3 protobuf<=3.20.3
python etcd_app.py
```
---
## Unsupported System Calls
- The following system calls which were used by etcd are not supported in Unikraft:
    - `clone`
    - `readlinkat`
    - `rt_sigreturn`
