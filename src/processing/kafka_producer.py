from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers='your-kafka-server:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def produce_messages():
    sample_data = [
        {"video_id": "abc123", "title": "Video 1", "views": 1000},
        {"video_id": "def456", "title": "Video 2", "views": 2500}
    ]

    for message in sample_data:
        producer.send('youtube-streaming', message)
        print(f"Produced: {message}")
        time.sleep(2)

if __name__ == "__main__":
    produce_messages()
