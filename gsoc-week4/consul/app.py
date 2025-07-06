from flask import Flask, jsonify
import requests, os, time

CONSUL_URL = os.getenv("CONSUL_URL", "http://localhost:8500")
SERVICE_NAME = "hello-service"
SERVICE_ID = f"{SERVICE_NAME}-{int(time.time())}"

app = Flask(__name__)

@app.route("/health")
def health():
    return "OK", 200

@app.route("/hello")
def hello():
    # Retrieve a message from KV store
    res = requests.get(f"{CONSUL_URL}/v1/kv/config/message?raw")
    message = res.text if res.status_code == 200 else "No message"
    return jsonify({"message": message})

def register_service():
    payload = {
        "ID": SERVICE_ID,
        "Name": SERVICE_NAME,
        "Address": os.getenv("SERVICE_ADDRESS", "localhost"),
        "Port": int(os.getenv("SERVICE_PORT", 5000)),
        "Check": {
            "HTTP": f"http://{os.getenv('SERVICE_ADDRESS','localhost')}:{os.getenv('SERVICE_PORT',5000)}/health",
            "Interval": "10s"
        }
    }
    requests.put(f"{CONSUL_URL}/v1/agent/service/register", json=payload)
    print(f"Registered {SERVICE_ID}")

if __name__ == "__main__":
    register_service()
    app.run(host="0.0.0.0", port=5000)
