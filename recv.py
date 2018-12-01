#!/usr/bin/env python3

import pika

HOST="127.0.0.1"
QUEUE_NAME="mq_test"

def callback(ch, method, properties, body):
	message = body.decode("ascii")
	print("Received message: {}".format(message))

def main():
	connection = pika.BlockingConnection(pika.ConnectionParameters(host=HOST))
	channel = connection.channel()
	channel.queue_declare(queue=QUEUE_NAME)
	channel.basic_consume(callback, queue=QUEUE_NAME, no_ack=True)
	try:
		channel.start_consuming()
	except KeyboardInterrupt:
		print("Stopped by user")

if __name__ == "__main__":
	main()
