# traefik 3.4
- Created config files:
    - [`traefik.yml`](app/traefik.yml) - Traefik static configuration
    - [`dynamic.yml`](app/dynamic.yml) - Defined routers and services (linked to a local Python server)
    - [`server.py`](app/server.py) - Simple Python HTTP server on port 5000
- Started container with traefik image:
```bash
docker run -it -p 80:80 -p 8080:8080 traefik /bin/sh
```
- Started Python server inside the container
```sh
python3 /app/server.py
```
- Ran Traefik manually inside the container
```sh
traefik \
  --entrypoints.web.address=:80 \
  --api.dashboard=true \
  --providers.file.filename=/traefik_eg/dynamic.yml
```
- Accessed services from host machine:
    - `http://localhost` &rarr; Proxies to Python server
    - `http://localhost:8080/dashboard/ &rarr; Traefik dashboard

## Unsupported System Calls
- These system calls were used by traefik which is not supported in Unikraft:
    - `clone`
    - `inotify_add_watch`
    - `inotify_init1`
    - `readlinkat`
    - `rt_sigreturn`
