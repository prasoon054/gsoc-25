# tomcat 9.0
## How to replicate
- Start `tomcat:9.0` container in interactive mode.
```bash
docker run -it -p 8080:8080 tomcat:9.0 /bin/sh
```
- Install `strace` inside the container.
```sh
apt-get update
apt-get install -y strace
```
- Start `tomcat` under `strace`.
```sh
strace -o /tmp/strace_out.txt -f /usr/local/tomcat/bin/catalina.sh run
```
- Copy [`hello.war`](hello-servlet/hello.war) to the container's `webapps` directory.
```bash
docker cp hello.war tomcat-strace:/usr/local/tomcat/webapps/
```
- Access now via `http://localhost:8080/hello/hello`
---
## Unsupported System Calls
- System calls used by `tomcat` but not supported in `Unikraft`:
    - `arch_prctl`
    - `brk`
    - `clone`
    - `clone3`
    - `execve`
    - `faccessat2`
    - `readlinkat`
    - `rseq`
    - `rt_sigreturn`
    - `set_robust_list`
    - `statx`
