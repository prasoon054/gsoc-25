# prometheus 2.53.2
- Pulled the latest `alpine` linux image from `Dockerhub`.
```bash
docker pull alpine:latest
docker run -it -p 9000:9000 -p 9001:9001 /bin/sh
```
- Installed the latest `prometheus` using `apk` package manager.
```sh
apk add --repository https://dl-cdn.alpinelinux.org/alpine/edge/community prometheus=2.53.4-r2
```
- Started a http server on container.
```bash
python3 -m http.server 9000
```
- Created a demo metric on container
```bash
echo -e "demo_metric 42" > metrics
```
- Created [`prometheus.yml`](app/prometheus.yml) inside the container.
- Ran `prometheus` under strace using the configuration files set up in last step
```sh
strace prometheus --config.file=prometheus.yml 2> /tmp/strace_out.log
```
- Verified metrics are accessible.
```bash
curl http://localhost:9000/metrics
```
---
## Unsupported System Calls
- The following syscalls which were used by mosquitto are not supported in Unikraft:
    - `clone`
    - `readlinkat`
    - `rt_sigreturn`
