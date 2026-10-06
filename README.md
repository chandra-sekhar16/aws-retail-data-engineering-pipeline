# AWS Retail Data Engineering Pipeline

An end-to-end data engineering portfolio project demonstrating a retail sales data pipeline using Python, SQL, and AWS data engineering technologies.

## Project Overview

This project processes retail sales data through an ingestion, transformation, and loading pipeline.

The current implementation demonstrates the pipeline locally using Python, Pandas, and SQLite. The project is designed to extend the same workflow to AWS services such as Amazon S3, AWS Glue, PySpark, Amazon Redshift, and Apache Airflow.

## Architecture

```text
CSV Sales Data
      |
      v
Python / Pandas
      |
      v
Data Ingestion
      |
      v
Data Transformation
      |
      +--> Remove duplicates
      +--> Validate quantity and price
      +--> Convert order dates
      +--> Calculate total sales
      |
      v
SQLite Database
      |
      v
SQL Analytics


AWS Target Architecture

CSV / JSON Data
      |
      v
Amazon S3
      |
      v
AWS Glue / PySpark
      |
      v
Data Quality & Transformation
      |
      v
Curated S3 Data
      |
      v
Amazon Redshift
      |
      v
SQL Analytics
