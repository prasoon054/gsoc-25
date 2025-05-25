# mosquitto 2.0.21
- Pulled and ran Mosquitto container interactively.
```bash
docker run -it -p 1883:1883 eclipse-mosquitto:2.0.21 /bin/sh
```
- Manually started the Mosquitto broker inside the container
```sh
strace mosquitto -c /mosquitto/config/mosquitto.conf 2> strace_out.log
```
- Created [`mqtt_app.py`](app/mqtt_app.py) with pub-sub logic using paho.mqtt.client
```bash
pip install paho-mqtt
python mqtt_app.py
```
---
## Unsupported System Calls
- The following syscalls which were used by mosquitto are not supported in Unikraft:
    - `brk` &rarr; Used only once (not sure, during what step)
