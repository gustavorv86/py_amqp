#!/usr/bin/env python3

import pika
import time

HOST="127.0.0.1"
QUEUE_NAME="mq_test"
POLLING=5

def main():
	connection = pika.BlockingConnection(pika.ConnectionParameters(host=HOST))
	channel = connection.channel()
	channel.queue_declare(queue=QUEUE_NAME)
	
	count = 1
	while True:
		try:
			msg = "Message: {}".format(count)
			channel.basic_publish(exchange='', routing_key=QUEUE_NAME, body=msg)
			count +=1
			print("Send: {}".format(msg))
			
			time.sleep(POLLING)
		except KeyboardInterrupt:
			print("Stopping by user")
			break
	
	connection.close()

if __name__ == "__main__":
	main()
