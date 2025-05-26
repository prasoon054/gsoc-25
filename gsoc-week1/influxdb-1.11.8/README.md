# influxdb 1.11.8
## How to replicate?
- Started influxdb container
```bash
sudo docker run -it -p 8086:8086 influxdb:1.11.8 /bin/sh
```
- Inside the container:
```sh
influxd &
influx
```
```sql
CREATE DATABASE demo
USE demo
INSERT temperature,sensor=living_room value=22.5
INSERT temperature,sensor=living_room value=23.0
INSERT temperature,sensor=bedroom value=21.2
INSERT temperature,sensor=bedroom value=20.9
SELECT * FROM temperature
SELECT * FROM temperature WHERE sensor='bedroom'
SELECT MEAN(value) FROM temperature
```
- Wrote data using curl from host.
```bash
curl -i -XPOST 'http://localhost:8086/write?db=demo' \
  --data-binary 'temperature,sensor=kitchen value=24.1'
```
- Queried again in container.
```sql
SELECT * FROM temperature WHERE sensor='kitchen'
```

## Unsupported System Calls
- These are the system calls which were used by InfluxDB but not supported in Unikraft.
    - `brk`
    - `clone`
    - `readlinkat`
    - `rt_sigreturn`
