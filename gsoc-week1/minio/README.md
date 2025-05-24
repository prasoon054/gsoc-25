# minio
- The popular [minio/minio](https://hub.docker.com/r/minio/minio) is minimal and doesn't have a package manager.
- Pulled the latest `alpine` linux image from `Dockerhub`.
```bash
docker pull alpine:latest
docker run -it -p 9000:9000 -p 9001:9001 /bin/sh
```
- Fetched the latest `MinIO` server binary (inside container)
```sh
apk update && apk add curl
curl -O https://dl.min.io/server/minio/release/linux-amd64/minio
chmod +x minio
mv minio /usr/local/bin/
```
- Created data directory
```sh
mkdir /data
```
- Launched MinIO under `strace`, targeting the console UI port 9001:
```sh
strace minio server /data --console-address ":9001" 2> /tmp/strace_out.txt
```
- After launching `minio`, a [python script](app/minio_app.py) was used to:
    - Connect to the minio server at `localhost:9000`.
    - Create a new bucket named `testbucket`.
    - Upload a file named `example.txt` to the bucket.
---
## Unsupported System Calls
- The following syscalls which were used by consul are not supported in Unikraft:
    - `clone`
    - `readlinkat`
    - `rt_sigreturn`
