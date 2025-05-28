# wireguard 1.0.20210914
# syncthing 1.28.1
- Run `alpine` on docker.
```bash
docker run -it \
--cap-add=NET_ADMIN \
--cap-add=SYS_MODULE \
-v /lib/modules:/lib/modules \
-v /dev/net/tun:/dev/net/tun \
-p 51820:51820/udp \
alpine /bin/sh
```
- Install `wireguard-tools-wg-quick`, `iproute` and `iptables` inside docker.
```sh
apk add strace wireguard-tools-wg-quick iproute iptables
```
- Generate (SK, PK) pair.
```sh
cd /etc/wireguard
wg genkey | tee privatekey | wg pubkey > publickey
```
- Create a wireguard interface (`/etc/wireguard/wg0.conf`)
```console
[Interface]
PrivateKey = <insert contents of privatekey>
Address = 10.0.0.1/24
ListenPort = 51820
```
- Bring up the interface
```sh
strace wg-quick up wg0 2> /tmp/strace_out.log
ip a show wg0
strace wg show 2>> /tmp/strace_out.log
```
- Bring down the interface
```sh
strace wg-quick down wg0 2>> /tmp/strace_out.log
```
---
## Unsupported System Calls
- System calls used by wireguard which are not supported in Unikraft
    - `brk`
    - `clone`
    - `execve`
    - `faccessat2`
    - `readlinkat`
    - `rt_sigreturn`