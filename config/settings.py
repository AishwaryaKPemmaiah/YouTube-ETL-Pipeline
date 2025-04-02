import os

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
PROJECT_ID = "your-project-id"
PUBSUB_TOPIC = "youtube-data-ingest"
BIGQUERY_DATASET = "your_dataset"
BIGQUERY_TABLE = "youtube_data"
KAFKA_SERVER = "your-kafka-server"
KAFKA_TOPIC = "youtube-streaming"