# Apache Kafka

It is an open-source distributed event streaming platform.
It was originally developed by LinkedIn and later open-sourced as an Apache Software Foundation project.

Kafka is designed to handle large-scale data streaming and processing in real-time.

It is not replacement of databases.
Here producer produces an event which is then send to kafka (can be topic based), kafka then send this to configured services(consumer).</br>
It can acts as Queue as well as Publish-Subscribe Architecture.</br>
For Queue => no. of partitions = no. of consumers.</br>
For Publish-Subscribe => no. of partitions > no. of consumers.

## Key features:

<b>Publish-Subscribe Architecture</b>: Kafka follows a publish-subscribe model, where producers publish messages to topics, and consumers subscribe to these topics to receive the messages.

<b>Distributed</b>: Kafka is designed to be distributed, fault-tolerant, and scalable.
It can run on a cluster of machines to handle high throughput and provide resilience.

<b>High Throughput</b>: Kafka is optimized for high throughput and low-latency data streaming.
It can handle a large number of events per second.

<b>Fault Tolerance</b>: Kafka is designed to be fault-tolerant by replicating data across multiple broker nodes.
If one node fails, others can take over to ensure continuous operation.

<b>Durability</b>: Kafka retains messages for a configurable period, allowing consumers to catch up on missed messages or replay events.

<b>Streaming Processing</b>: Kafka supports stream processing, allowing developers to build real-time applications and analytics by processing data as it flows through the system.

<b>Connectors</b>: Kafka provides a framework for connectors that enable integration with various data sources and sinks, facilitating the movement of data between different systems.

<b>Scalability</b>: Kafka scales horizontally by adding more broker nodes to the cluster as the data and load increase.

<img src="https://miro.medium.com/v2/resize:fit:750/format:webp/1*lu6wtETiXfeG23fIUJi-hA.png">

# Components:

## Kafka Topic

A topic in Kafka is a category or feed name to which messages are published by producers and from which messages are consumed by consumers.</br>
Topics serve as a way to categorize and organize the data streams in Kafka. Each message within Kafka belongs to a specific topic.

## Kafka Partition

Each Kafka topic is divided into partitions.Partitions allow for parallel processing and scalability.</br>
Partitions allow Kafka to horizontally scale and handle large amounts of data by distributing the data across multiple servers or brokers.</br>
Messages within a partition are ordered, but the order is not guaranteed across different partitions.</br>

## Broker

Brokers are individual Kafka servers, and they form a cluster when they are configured to work together. </br>
A Kafka cluster can have multiple brokers, each responsible for handling a share of the partitions and the associated data.</br>
A Kafka cluster is a group of Kafka brokers that work together to provide high availability and fault tolerance for your data.

## Event

Event: things that just happened OR change in status in process OR user interaction that happened

Events in Kafka is key value pair like JSON.
Events can be differentiated using Topic which is nothing but a separate key.

## Message Retention

Retention period for messages is configured using the <b>log.retention.hours</b> property.</br>
default value in 7 days.
After this period, messages will be eligible for deletion during the log segment cleanup process.

## Offset

An offset is a unique identifier assigned to each message within a partition.</br>
It represents the position of a consumer in a partition. Consumers use offsets to keep track of which messages they have already consumed.

## Consumers

It is service that subscribes to specific topic.
Each message in a topic is delivered to one consumer within each subscribing consumer group.</br>
When a consumer group subscribes to a topic, Kafka ensures that each partition is assigned to only one consumer within the group.</br>
Each consumer keeps track of the offset it has consumed within its assigned partitions.</br>
A Single Consumer can consume multiple partitions but a single partition can be consumed by only one consumer.</br>
It is Solved by Consumer Group. Here a Event in partition is assigned to a consumer in consumer group.

## Zoo keeper

It provides a simple and reliable way for distributed processes to coordinate and synchronize with each other through a centralized service.

### Uber Kafka Architecture

<img src="https://blog.uber-cdn.com/cdn-cgi/image/width=1460,quality=80,onerror=redirect,format=auto/wp-content/uploads/2020/12/pasted-image-0-14.png">
