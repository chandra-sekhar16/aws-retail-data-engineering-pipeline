# AWS Retail Data Engineering Pipeline

## Project Overview

End-to-end retail data engineering pipeline built using Python, Pandas, SQL and AWS data engineering services.

The project demonstrates data ingestion, transformation, data quality validation and loading into an analytical database.

## Architecture

CSV / JSON Data
        |
        v
       S3
        |
        v
   AWS Glue
   PySpark
        |
        v
Data Quality & Transformation
        |
        v
   Curated S3
        |
        v
   Redshift
        |
        v
 SQL Analytics

## Technologies

- Python
- Pandas
- SQL
- PySpark
- AWS S3
- AWS Glue
- Amazon Redshift
- Amazon Athena
- Apache Airflow
- AWS Lambda
- Amazon CloudWatch
- Git
- GitHub

## Project Structure

aws-retail-data-engineering-pipeline/
├── data/
│   └── sample_sales.csv
├── src/
│   ├── ingestion.py
│   ├── transformation.py
│   ├── loading.py
│   └── pipeline.py
├── sql/
│   └── create_tables.sql
├── requirements.txt
├── README.md
├── .gitignore
└── LICENSE

## Pipeline Steps

### 1. Data Ingestion

The pipeline reads retail sales data from CSV files using Pandas.

### 2. Data Transformation

The transformation layer:

- Removes duplicate records
- Converts order dates to datetime
- Calculates total sales amount
- Removes invalid quantity and price values
- Sorts records by order date

### 3. Data Loading

The transformed dataset is loaded into a relational database.

For local development, SQLite is used as the target database.

## Sample Data

The sample dataset contains:

- Order ID
- Order Date
- Customer ID
- Product
- Category
- Quantity
- Unit Price
- Region

A derived total_amount column is calculated during transformation.

## Data Quality

The pipeline applies basic data quality checks including:

- Duplicate record removal
- Positive quantity validation
- Positive unit price validation
- Date type conversion
- Derived sales amount validation

## Local Pipeline Execution

Install dependencies:

pip install -r requirements.txt

Run the pipeline:

python src/pipeline.py

The pipeline loads the sample data, performs transformations and creates the local SQLite database.

## SQL Schema

The SQL schema is available in:

sql/create_tables.sql

## AWS Target Architecture

The project is designed to be extended into an AWS-based data engineering platform using:

- Amazon S3 for data storage
- AWS Glue for ETL processing
- PySpark for distributed transformations
- Amazon Redshift for analytical workloads
- Amazon Athena for SQL-based querying
- Apache Airflow for orchestration
- AWS Lambda for event-driven processing
- Amazon CloudWatch for monitoring

## Future Enhancements

- Add AWS S3 ingestion
- Implement AWS Glue PySpark jobs
- Add Redshift integration
- Add Apache Airflow DAG
- Add automated data quality tests
- Add CloudWatch monitoring
- Add analytical SQL queries
- Add CI/CD using GitHub Actions

## Project Goals

This project demonstrates practical data engineering concepts including:

- ETL pipeline development
- Data transformation
- Data quality
- SQL analytics
- Cloud data architecture
- AWS data engineering
- Pipeline orchestration

## Disclaimer

This is a personal portfolio project using synthetic sample data. No confidential company data or proprietary code is included.

## Author

Chandra Sekhar

Cloud Data Engineer | AWS | PySpark | Python | SQL

GitHub: https://github.com/chandra-sekhar16
