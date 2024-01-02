# #  pip install confluent-kafka

# from confluent_kafka import Producer

# # Define Kafka broker address
# bootstrap_servers = 'localhost:9092'

# # Define Kafka topic
# topic = 'test1'

# # Kafka Producer Configuration
# producer_conf = {
#     'bootstrap.servers': bootstrap_servers,
#     'client.id': 'python-producer'
# }

# # Create a Kafka Producer instance
# producer = Producer(producer_conf)

# # Produce a message to the Kafka topic
# message = 'Hello, Kafka!'
# producer.produce(topic, key='key', value=message)

# # Wait for any outstanding messages to be delivered and delivery reports received
# producer.flush()

# print(f"Message produced to '{topic}': {message}")


from confluent_kafka import Producer

p = Producer({'bootstrap.servers': 'mybroker1,mybroker2'})


data_stream = [f"msg{i}" for i in range(10000)]

# Optional per-message on_delivery handler (triggered by poll() or flush())]

def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

for data in data_stream:
    # Trigger any available delivery report callbacks from previous produce() calls
    p.poll(0)

    # Asynchronously produce a message. The delivery report callback will
    # be triggered from the call to poll() above, or flush() below, when the
    # message has been successfully delivered or failed permanently.
    p.produce('mytopic', data.encode('utf-8'), callback=delivery_report)

# Wait for any outstanding messages to be delivered and delivery report
# callbacks to be triggered.
p.flush()