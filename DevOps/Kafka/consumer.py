from confluent_kafka import Consumer, KafkaError

# Define Kafka broker address
bootstrap_servers = 'localhost:9092'

# Kafka Consumer Configuration
consumer_conf = {
    'bootstrap.servers': bootstrap_servers,
    'group.id': 'python-consumer',
    'auto.offset.reset': 'earliest'
}

# Create a Kafka Consumer instance
consumer = Consumer(consumer_conf)

# Retrieve the list of topics from the Kafka cluster
cluster_metadata = consumer.list_topics()
topics = cluster_metadata.topics.keys()

# Subscribe to each topic individually
for topic in topics:
    print("Stating Listen to Topic: " + topic)
    consumer.subscribe([topic])

# Consume messages from the subscribed topics
while True:
    msg = consumer.poll(1.0)  # Timeout in seconds
    print(msg)

    if msg is None:
        continue
    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            continue
        else:
            print(msg.error())
            break

    # Process the consumed message
    print(f"Received message from topic '{msg.topic()}': {msg.value().decode('utf-8')}")

# Close the consumer
consumer.close()
