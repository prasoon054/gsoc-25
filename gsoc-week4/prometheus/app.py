from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from flask import Flask, Response

app = Flask(__name__)

# A simple counter metric
hello_counter = Counter("hello_requests_total", "Total number of hellos served")

@app.route("/hello")
def hello():
    hello_counter.inc()
    return "Hello, Prometheus!\n"

# Expose metrics on /metrics
@app.route("/metrics")
def metrics():
    data = generate_latest()
    return Response(data, mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    # Listen on all interfaces, port 8000
    app.run(host="0.0.0.0", port=5000)
