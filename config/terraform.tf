resource "google_pubsub_topic" "youtube_data" {
  name = "youtube-data-ingest"
}

resource "google_bigquery_dataset" "youtube_dataset" {
  dataset_id = "your_dataset"
}
