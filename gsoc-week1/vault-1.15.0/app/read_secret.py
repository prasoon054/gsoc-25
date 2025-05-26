import requests

VAULT_ADDR = "http://127.0.0.1:8200"
VAULT_TOKEN = "root"
SECRET_PATH = "secret/data/myapp/config"

headers = {
    "X-Vault-Token": VAULT_TOKEN
}

response = requests.get(f"{VAULT_ADDR}/v1/{SECRET_PATH}", headers=headers)

if response.status_code == 200:
    secret_data = response.json()["data"]["data"]
    print("Retrieved secret:")
    print(f"Username: {secret_data['username']}")
    print(f"Password: {secret_data['password']}")
else:
    print("❌ Error retrieving secret:")
    print(response.text)
