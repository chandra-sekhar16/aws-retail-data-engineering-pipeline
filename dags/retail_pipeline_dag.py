from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.amazon.aws.operators.glue import GlueJobOperator
from airflow.providers.amazon.aws.operators.athena import AthenaOperator

default_args = {
    'owner': 'chandra_sekhar',
    'depends_on_past': False,
    'start_date': datetime(2026, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'aws_retail_data_pipeline',
    default_args=default_args,
    description='Automated orchestration for AWS Retail ETL & Athena Validation',
    schedule_interval='@daily',
    catchup=False
) as dag:

    trigger_glue_job = GlueJobOperator(
        task_id='trigger_glue_retail_etl',
        job_name='retail-sales-etl-job',
        region_name='us-east-1',
        wait_for_completion=True
    )

    run_athena_analytics = AthenaOperator(
        task_id='run_athena_validation',
        query='SELECT SUM(quantity * unit_price) AS total_sales FROM retail_sales_db.retail_sales_processed;',
        database='retail_sales_db',
        output_location='s3://aws-retail-data-engineering-chandu/athena-results/'
    )

    trigger_glue_job >> run_athena_analytics