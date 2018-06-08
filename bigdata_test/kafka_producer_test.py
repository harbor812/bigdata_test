from kafka.producer import SimpleProducer
from kafka import KafkaConsumer
from kafka import KafkaClient
from kafka import TopicPartition

from kafka import KafkaProducer
print('start ')
# producer = KafkaProducer(bootstrap_servers='Kafka-01:9092')
# for i in range(100):
#     producer.send('kafka_input', 'video :%s' % i)
# producer.close()
# print('produced ')

#consumer = KafkaConsumer('node-online-data-player',bootstrap_servers='Kafka-game-01:9092',auto_offset_reset="earliest")


consumer = KafkaConsumer('node-bullet-crawler-57',bootstrap_servers='Kafka-game-01:9092',auto_offset_reset="earliest")

#consumer = KafkaConsumer('node-online-data-player',bootstrap_servers='Kafka-01:9092',auto_offset_reset="earliest")
# consumer.set_topic_partitions('kafka_input')
for i in consumer:
    print(i.value)
consumer.close()