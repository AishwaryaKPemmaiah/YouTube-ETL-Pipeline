import requests
import json
import os
from google.cloud import pubsub_v1

youtube_api_key = os.getenv('YOUTUBE_API_KEY')
channel_id = "UC_x5XG1OV2P6uZZ5FSM9Ttw"
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path("your-project-id", "youtube-data-ingest")

def fetch_youtube_data(request):
    url = f"https://www.googleapis.com/youtube/v3/search?key={youtube_api_key}&channelId={channel_id}&part=snippet,id&order=date&maxResults=10"
    response = requests.get(url)
    data = response.json()
    if "items" in data:
        for item in data["items"]:
            message = json.dumps(item).encode("utf-8")
            publisher.publish(topic_path, message)
    return "Data published to Pub/Sub"