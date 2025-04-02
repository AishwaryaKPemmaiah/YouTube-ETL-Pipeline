from google.cloud import pubsub_v1
import json

def publish_message(topic_name, data):
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path("your-project-id", topic_name)
    message = json.dumps(data).encode("utf-8")
    publisher.publish(topic_path, message)
    print(f"Message published to {topic_name}")