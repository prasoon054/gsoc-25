import etcd3
import time

def on_change(response):
    # response is a WatchResponse; it has a .events list
    for event in response.events:
        # each `event` here is an Event, with .key and .value
        print(f"🔍 Watch event: {event.key.decode()} → {event.value.decode()}")

def main():
    # 1. Connect to etcd
    client = etcd3.client(host='localhost', port=2379)
    print("🔗 Connected to etcd at localhost:2379")

    # 2. Simple Put & Get
    client.put('foo', 'bar')
    value, _ = client.get('foo')
    print(f"📥 foo = {value.decode()}")

    # 3. Transactions (Compare‐And‐Swap)
    success, _ = client.transaction(
        compare=[client.transactions.value('foo') == b'bar'],
        success=[client.transactions.put('foo', 'baz')],
        failure=[client.transactions.put('foo', 'qux')],
    )
    if success:
        print("✔️  Transaction succeeded: foo was bar → now baz")
    else:
        print("❌ Transaction failed: foo was not bar → now qux")
    value, _ = client.get('foo')
    print(f"   current foo = {value.decode()}")

    # 4. Leases & TTL
    lease = client.lease(ttl=5)
    client.put('ephemeral', 'bye-bye', lease=lease)
    print("⏳ Wrote 'ephemeral' with 5s TTL")

    # 5. Watch via Callback (fixed)
    client.add_watch_callback('foo', on_change)

    # Trigger a change after 2 seconds
    time.sleep(2)
    client.put('foo', 'new-value')

    # 6. Observe lease expiry
    print("⏲️  Sleeping 6s to let 'ephemeral' expire…")
    time.sleep(6)
    val, _ = client.get('ephemeral')
    if val is None:
        print("💥 'ephemeral' has expired")
    else:
        print("❗ Still there:", val.decode())

    # 7. Distributed Lock
    lock = client.lock('my-lock', ttl=10)
    print("🔐 Trying to acquire lock…")
    if lock.acquire(timeout=3):
        print("🔒 Lock acquired! Doing work…")
        time.sleep(2)
        lock.release()
        print("🔓 Lock released")
    else:
        print("😕 Could not acquire lock")

    # 8. Cleanup
    client.delete('foo')
    client.delete('ephemeral')
    print("🧹 Cleaned up keys; demo done.")

if __name__ == '__main__':
    main()
