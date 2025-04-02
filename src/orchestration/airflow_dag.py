from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from src.ingestion.fetch_youtube_data import fetch_youtube_data
from src.processing.dataflow_job import run_dataflow_job

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 4, 2),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'youtube_etl_pipeline',
    default_args=default_args,
    description='YouTube ETL Pipeline with Apache Airflow',
    schedule_interval=timedelta(hours=1),
)

extract_task = PythonOperator(
    task_id='extract_youtube_data',
    python_callable=fetch_youtube_data,
    dag=dag,
)

transform_task = PythonOperator(
    task_id='run_dataflow_job',
    python_callable=run_dataflow_job,
    dag=dag,
)

extract_task >> transform_task
