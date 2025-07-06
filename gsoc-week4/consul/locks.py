import requests, uuid
session = requests.put("http://localhost:8500/v1/session/create", json={"Name":"lock-session"}).json()["ID"]
# Try to acquire lock
key = "locks/my-lock"
owner = str(uuid.uuid4())
acquired = requests.put(
    f"http://localhost:8500/v1/kv/{key}",
    params={"acquire": session},
    data=owner).json()
print("Lock acquired?", acquired)

# Release
released = requests.put(
    f"http://localhost:8500/v1/kv/{key}",
    params={"release": session},
    data=owner).json()
print("Lock released?", released)
