from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'youtube-streaming',
    bootstrap_servers='your-kafka-server:9092',
    auto_offset_reset='earliest',
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

def consume_messages():
    for message in consumer:
        data = message.value
        print(f"Consumed: {data}")

if __name__ == "__main__":
    consume_messages()
