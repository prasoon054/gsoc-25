import etcd3
import threading
import time

# Connect to the local etcd instance
etcd = etcd3.client(host='localhost', port=2379)

KEY = "/config/myapp"

def watch_key():
    events_iterator, cancel = etcd.watch(KEY)
    print(f"Watching for changes on key: {KEY}")
    for event in events_iterator:
        key = event.key.decode() if event.key else "<none>"
        value = event.value.decode() if event.value else "<deleted>"
        print(f"Detected change: {type(event).__name__} -> {key} = {value}")

def write_key(value):
    etcd.put(KEY, value)
    print(f"Wrote to etcd: {KEY} = {value}")

def read_key():
    value, meta = etcd.get(KEY)
    if value:
        print(f"Read from etcd: {KEY} = {value.decode()}")
    else:
        print(f"Key {KEY} not found.")

if __name__ == "__main__":
    threading.Thread(target=watch_key, daemon=True).start()

    write_key("initial-value")

    time.sleep(1)

    read_key()

    time.sleep(1)

    write_key("updated-value")

    time.sleep(5)
