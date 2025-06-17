import paho.mqtt.client as mqtt
import time

BROKER = "localhost"
PORT = 1883
TOPIC = "test/topic"
connected = False

def on_connect(client, userdata, flags, rc):
    global connected
    if rc == 0:
        connected = True
        print("[INFO] Connected successfully")
        client.subscribe(TOPIC)
    else:
        print(f"[ERROR] Connection failed with code {rc}")

def on_message(client, userdata, msg):
    print(f"[RECEIVED] Topic: {msg.topic}, Message: {msg.payload.decode()}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

rc = client.connect(BROKER, PORT, 60)
if rc != 0:
    print(f"[ERROR] Could not connect to broker. Return code: {rc}")
    exit(1)

client.loop_start()

while not connected:
    print("[INFO] Waiting for connection...")
    time.sleep(1)

try:
    while True:
        message = f"Hello MQTT at {time.ctime()}"
        print(f"[SENDING] {message}")
        client.publish(TOPIC, message)
        time.sleep(5)
except KeyboardInterrupt:
    print("Exiting...")
finally:
    client.loop_stop()
    client.disconnect()
