import paho.mqtt.client as mqtt
import time

BROKER = "localhost"
PORT = 1883
TOPIC = "test/topic"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    print(f"[RECEIVED] Topic: {msg.topic}, Message: {msg.payload.decode()}")

client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)

client.loop_start()

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
