# consul 1.15.4
- Started consul docker container:
    ```console
    docker run -it -p 8500:8500 -p 8600:8600/udp consul /bin/sh
    ```
- Launched consul agent inside container, under `strace`:
    ```sh
    strace -ff -o consul agent -dev -ui -client=0.0.0.0
    ```
- From host, registered a sample `web-service` using:
    ```bash
    curl --request PUT --data @web-service.json http://localhost:8500/v1/agent/service/register
    ```
- Did some health checks.
- System call logs from `strace` stored in [`strace_out.log`](strace_out.log)
- The following syscalls which were used by consul are not supported in Unikraft:
    - `clone`
    - `detached`
    - `readlinkat`
    - `rt_sigreturn`
