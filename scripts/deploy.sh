#!/bin/bash
echo "Deploying YouTube ETL Pipeline"
gcloud functions deploy fetch_youtube_data --runtime python39 --trigger-http --allow-unauthenticated
echo "Deployment complete!"
