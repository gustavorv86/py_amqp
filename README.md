# pyAMQP
Simple example to send and receive AMQP (Advanced Message Queuing Protocol)

Install
-------

Install next packages:

```
sudo apt install rabbitmq-server
sudo apt install python3-pika
```

Run
---

Check the RabbitMQ server status:

```
sudo ./server/rabbitmq-status.sh
```

If the server is not running then execute the next command:

```
sudo ./server/rabbitmq-start.sh
```

Run the consume program:

```
./recv.py
```

In another terminal run the publish program:

```
./send.py
```
