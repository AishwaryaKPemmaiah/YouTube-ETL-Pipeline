📌 Project Overview

The YouTube ETL Pipeline is an end-to-end data pipeline designed to extract, process, and store YouTube data for advanced analytics. This pipeline automates the Extraction, Transformation, and Loading (ETL) processes, ensuring seamless data ingestion, processing, and visualization using Google Cloud Platform (GCP).

🔥 Key Highlights:

Real-time Data Streaming using Kafka & Google Pub/Sub

Batch & Streaming Processing with Apache Beam

Data Storage & Querying using Google BigQuery

Pipeline Orchestration with Apache Airflow

Visualization & Reporting with Looker Studio

Containerized Deployment using Docker & Terraform

⚡ Technology Stack

This pipeline is built using enterprise-grade technologies:

- Apache Airflow – Orchestrates ETL workflows.
- Google Pub/Sub – Manages event-driven messaging.
- Apache Kafka – Handles real-time streaming data.
- Apache Beam – Processes data efficiently.
- Google BigQuery – Stores structured data for analytics and querying.
- Google Looker Studio – Provides data visualization and reporting.
- Docker – Ensures a scalable and containerized deployment.
- Terraform – Automates cloud infrastructure provisioning.
- Google Cloud Logging – Provides monitoring and logging capabilities.


![image](https://github.com/user-attachments/assets/19c327e5-6464-4cb8-93f3-2557958bd939)



🔄 ETL Process Explanation

This structured ETL process ensures efficiency and scalability:

Step 1: Data Extraction

Source: YouTube Data API

Transport: Google Pub/Sub (for real-time ingestion)

Script: fetch_youtube_data.py

Step 2: Data Processing & Transformation

Kafka consumes data from Pub/Sub.

Apache Beam processes, cleans, and enriches the data.

Script: dataflow_job.py

Step 3: Data Storage

Processed Data is stored in Google BigQuery.

Enables efficient SQL-based analytics.

Script: kafka_consumer.py

Step 4: Workflow Orchestration (Apache Airflow DAGs)

Automates ETL process with Apache Airflow DAGs.

Task dependencies: Extract → Transform → Load.

Script: airflow_dag.py

Step 5: Visualization & Reporting

Looker Studio fetches data from BigQuery.

Generates interactive dashboards.

File: looker_studio_dashboard.json

![image](https://github.com/user-attachments/assets/4568f87d-8adb-4a31-8a95-569ca49da903)


Summary

✔ Automated Data Pipeline: Extracts, processes, and loads YouTube data seamlessly.
✔ Optimized Storage: Uses Google BigQuery for structured data storage and querying.
✔ Scalable & Reliable: Handles large-scale data processing with Kafka and Apache Beam.
✔ Airflow Orchestration: Schedules, monitors, and automates ETL workflows.
✔ Cloud & Docker Integration: Enables easy deployment and scalability.
✔ Infrastructure as Code: Uses Terraform to provision cloud resources efficiently.
✔ Interactive Dashboards: Looker Studio provides real-time visualizations and reports.
