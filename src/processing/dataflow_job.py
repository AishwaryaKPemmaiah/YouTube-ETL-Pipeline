import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

class ProcessYouTubeData(beam.DoFn):
    def process(self, element):
        import json
        record = json.loads(element.decode('utf-8'))
        return [{
            'video_id': record['id']['videoId'],
            'title': record['snippet']['title'],
            'published_at': record['snippet']['publishedAt'],
            'channel_title': record['snippet']['channelTitle']
        }]

def run_dataflow_job():
    options = PipelineOptions(
        project='your-gcp-project-id',
        region='us-central1',
        runner='DataflowRunner',
        temp_location='gs://your-bucket/temp'
    )

    with beam.Pipeline(options=options) as p:
        (p
         | 'Read PubSub' >> beam.io.ReadFromPubSub(topic='projects/your-gcp-project-id/topics/youtube-data-ingest')
         | 'Process Data' >> beam.ParDo(ProcessYouTubeData())
         | 'Write to BigQuery' >> beam.io.WriteToBigQuery(
                'your-gcp-project-id:your_dataset.youtube_data',
                schema='video_id:STRING, title:STRING, published_at:TIMESTAMP, channel_title:STRING',
                write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND
         ))

if __name__ == "__main__":
    run_dataflow_job()
