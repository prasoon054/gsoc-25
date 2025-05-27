import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='test_queue')
channel.basic_publish(exchange='', routing_key='test_queue', body='Hello, Rabbit!')

print(" [x] Sent 'Hello, Rabbit!'")

method_frame, header_frame, body = channel.basic_get(queue='test_queue', auto_ack=True)
if body:
    print(" [x] Received:", body.decode())
else:
    print(" [x] No message received")

connection.close()
