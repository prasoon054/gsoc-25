# rabbitmq 4-management
## How to replicate?
- Start the `rabbitmq` container in interactive mode
```bash
docker run -it -p 5672:5672 -p 15672:15672 rabbitmq:4-management bash
```
- Install `strace` inside the container
```bash
apt-get update
apt-get install -y strace
```
- Start RabbitMQ under `strace`
```bash
strace rabbitmq-server 2> /tmp/strace_out.log
```
- On client machine, run [`test_rabbit.py`](app/test_rabbitmq.py)
```bash
pip3 install pika
python3 test_rabbitmq.py
```
## Unsupported System Calls
- System calls which were used by `rabbitmq` which are not supported in `Unikraft`
    - `arch_prctl`
    - `brk`
    - `chmod`
    - `clone`
    - `clone3`
    - `close_range`
    - `execve`
    - `memfd_create`
    - `rseq`
    - `rt_sigreturn`
    - `set_robust_list`
    - `vfork`
