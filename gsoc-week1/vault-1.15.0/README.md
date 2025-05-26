# vault 1.15.0
## How to replicate?
- Pulled the latest `alpine` image from `Dockerhub`.
```bash
docker pull alpine:latest
docker run -it alpine /bin/sh
```
- Installed dependencies on Alpine.
```sh
apk update
apk add curl unzip python3 py3-pip
pip3 install requests
```
- Downloaded and installed `vault` binary.
```sh
VAULT_VERSION="1.15.0"
curl -O https://releases.hashicorp.com/vault/${VAULT_VERSION}/vault_${VAULT_VERSION}_linux_amd64.zip
unzip vault_${VAULT_VERSION}_linux_amd64.zip
mv vault /usr/local/bin/
chmod +x /usr/local/bin/vault
```
- Started vault in dev mode.
```sh
vault server -dev -dev-root-token-id=root
```
- In a second terminal, exported environment variables for Vault CLI.
```bash
docker exec -it <container-id> /bin/sh
```
```sh
export VAULT_ADDR='http://127.0.0.1:8200'
export VAULT_TOKEN='root'
```
- Stored test secret using vault CLI.
```sh
vault kv put secret/myapp/config username="admin" password="s3cr3t"
```
- Verified the stored secret.
```sh
vault kv get secret/myapp/config
```
- Started the python script [`read_secret.py`](app/read_secret.py) via vault HTTP API.
```sh
python3 read_secret.py
```
---
## Unsupported System Calls
- These system calls were used by traefik which is not supported in Unikraft:
    - `clone`
    - `readlinkat`
    - `rt_sigreturn`
