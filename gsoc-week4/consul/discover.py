import requests

def discover_and_call():
    # Query Consul catalog
    res = requests.get("http://localhost:8500/v1/catalog/service/hello-service")
    instances = res.json()
    for inst in instances:
        url = f"http://{inst['ServiceAddress']}:{inst['ServicePort']}/hello"
        print(requests.get(url).json())

if __name__ == '__main__':
    discover_and_call()
