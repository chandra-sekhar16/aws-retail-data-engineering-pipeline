# AWS Retail Data Engineering Pipeline

An end-to-end **AWS Data Engineering pipeline** that ingests retail sales data into Amazon S3, processes the data using AWS Glue, converts the dataset into Apache Parquet format, catalogs the processed data using AWS Glue Data Catalog, and performs SQL-based analytics using Amazon Athena.

---

## 🚀 Project Overview

This project demonstrates a practical cloud-based data engineering workflow for processing retail sales data.

The pipeline takes raw CSV data, stores it in Amazon S3, processes it using AWS Glue ETL, writes optimized Parquet output to a processed S3 location, registers the processed dataset in AWS Glue Data Catalog, and enables serverless analytics through Amazon Athena.

### End-to-End Pipeline

```text
Raw Retail CSV
      |
      v
Amazon S3
      |
      v
AWS Glue ETL
      |
      v
Parquet Transformation
      |
      v
S3 Processed Layer
      |
      v
AWS Glue Data Catalog
      |
      v
Amazon Athena
      |
      v
Business Analytics
```

---

## 🏗️ Architecture

```text
                    ┌─────────────────────┐
                    │   Retail Sales CSV  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │     Amazon S3       │
                    │    Raw Data Layer   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │      AWS Glue       │
                    │      ETL Job        │
                    │                     │
                    │ retail-sales-etl-job│
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │       Parquet       │
                    │  Processed Dataset  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │     Amazon S3       │
                    │   processed/ layer  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Glue Data Catalog │
                    │                     │
                    │ retail_sales_db     │
                    │ retail_sales_       │
                    │ processed           │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Amazon Athena    │
                    │    SQL Analytics    │
                    └─────────────────────┘
```

---

## 🛠️ Technologies Used

| Technology                | Purpose                           |
| ------------------------- | --------------------------------- |
| **Amazon S3**             | Raw and processed data storage    |
| **AWS Glue**              | ETL processing                    |
| **AWS Glue Data Catalog** | Metadata and table management     |
| **Amazon Athena**         | Serverless SQL analytics          |
| **Apache Parquet**        | Optimized columnar storage        |
| **SQL**                   | Analytical queries                |
| **Git & GitHub**          | Version control and documentation |

---

## ☁️ AWS Resources

### S3 Bucket

```text
aws-retail-data-engineering-chandu
```

### Raw Data

```text
s3://aws-retail-data-engineering-chandu/
```

### Processed Data

```text
s3://aws-retail-data-engineering-chandu/processed/
```

### AWS Glue Job

```text
retail-sales-etl-job
```

### Glue Database

```text
retail_sales_db
```

### Glue Source Table

```text
aws_retail_data_engineering_chandu
```

### Glue Processed Table

```text
retail_sales_processed
```

### Athena

Amazon Athena is used to query the processed Parquet dataset using SQL without managing any database servers.

---

## 📂 S3 Data Layout

```text
aws-retail-data-engineering-chandu/
│
├── sample_sales.csv
│
├── processed/
│   ├── run-...parquet
│   └── run-...parquet
│
└── Unsaved/
```

The analytical dataset is stored under:

```text
s3://aws-retail-data-engineering-chandu/processed/
```

The dedicated `processed/` prefix separates the transformed Parquet data from the raw/source files.

---

## 📊 Source Dataset

The retail sales dataset contains the following fields:

| Column        | Data Type | Description             |
| ------------- | --------- | ----------------------- |
| `order_id`    | bigint    | Unique order identifier |
| `order_date`  | string    | Order date              |
| `customer_id` | string    | Customer identifier     |
| `product`     | string    | Product name            |
| `category`    | string    | Product category        |
| `quantity`    | bigint    | Quantity purchased      |
| `unit_price`  | double    | Price per unit          |
| `region`      | string    | Sales region            |

---

## ⚙️ AWS Glue ETL

### Job Configuration

| Configuration | Value                  |
| ------------- | ---------------------- |
| Job Name      | `retail-sales-etl-job` |
| Job Type      | Visual ETL             |
| Glue Version  | 5.1                    |
| Worker Type   | G.1X                   |
| Output Format | Apache Parquet         |

### Source

```text
s3://aws-retail-data-engineering-chandu/
```

### Target

```text
s3://aws-retail-data-engineering-chandu/processed/
```

The AWS Glue ETL job reads the raw retail sales data from Amazon S3 and writes the transformed dataset in Apache Parquet format.

The job was successfully executed and generated Parquet output in the processed S3 location.

---

## 🗂️ AWS Glue Data Catalog

The processed dataset is registered in the AWS Glue Data Catalog.

### Database

```text
retail_sales_db
```

### Table

```text
retail_sales_processed
```

### Table Location

```text
s3://aws-retail-data-engineering-chandu/processed/
```

### Table Format

```text
Parquet
```

The Glue Data Catalog provides the metadata required by Amazon Athena to query the processed dataset.

---

## 🔎 Amazon Athena Analytics

Amazon Athena is used to perform serverless SQL analytics on the processed Parquet data.

### 1. Total Sales

```sql
SELECT
    SUM(quantity * unit_price) AS total_sales
FROM retail_sales_db.retail_sales_processed;
```

**Result:**

```text
₹10,06,400
```

---

### 2. Sales by Region

```sql
SELECT
    region,
    SUM(quantity * unit_price) AS total_sales
FROM retail_sales_db.retail_sales_processed
GROUP BY region
ORDER BY total_sales DESC;
```

**Result:**

| Region |     Sales |
| ------ | --------: |
| South  | ₹4,92,400 |
| West   | ₹1,90,000 |
| North  | ₹1,84,000 |
| East   | ₹1,40,000 |

---

### 3. Sales by Product

```sql
SELECT
    product,
    SUM(quantity * unit_price) AS total_sales
FROM retail_sales_db.retail_sales_processed
GROUP BY product
ORDER BY total_sales DESC;
```

**Result:**

| Product    |     Sales |
| ---------- | --------: |
| Laptop     | ₹4,60,000 |
| Mobile     | ₹2,62,000 |
| Monitor    | ₹1,92,000 |
| Headphones |   ₹58,000 |
| Keyboard   |   ₹20,000 |
| Mouse      |   ₹14,400 |

---

### 4. Sales by Category

```sql
SELECT
    category,
    SUM(quantity * unit_price) AS total_sales
FROM retail_sales_db.retail_sales_processed
GROUP BY category
ORDER BY total_sales DESC;
```

**Result:**

| Category    |     Sales |
| ----------- | --------: |
| Electronics | ₹9,14,000 |
| Accessories |   ₹92,400 |

---

### 5. Monthly Sales

```sql
SELECT
    substr(order_date, 1, 7) AS month,
    SUM(quantity * unit_price) AS total_sales
FROM retail_sales_db.retail_sales_processed
GROUP BY substr(order_date, 1, 7)
ORDER BY month;
```

**Result:**

| Month   |      Sales |
| ------- | ---------: |
| 2026-01 | ₹10,06,400 |

---

## 📈 Business Insights

Based on the current sample dataset:

| Metric                 |          Result |
| ---------------------- | --------------: |
| **Total Sales**        |  **₹10,06,400** |
| **Orders Processed**   |          **10** |
| **Top Region**         |       **South** |
| **South Region Sales** |   **₹4,92,400** |
| **Top Product**        |      **Laptop** |
| **Laptop Sales**       |   **₹4,60,000** |
| **Top Category**       | **Electronics** |
| **Electronics Sales**  |   **₹9,14,000** |

### Key Observations

* South generated the highest regional sales.
* Laptop was the highest-revenue product.
* Electronics contributed the majority of total sales.
* The processed Parquet dataset was successfully queried using Amazon Athena.
* The complete pipeline successfully processed the retail sales dataset from raw CSV to analytical results.

---

## ✅ Pipeline Validation

```text
CSV Ingestion             ✅
S3 Raw Storage             ✅
AWS Glue ETL               ✅
Parquet Conversion         ✅
S3 Processed Storage       ✅
Glue Data Catalog          ✅
Athena Table               ✅
Athena SQL Analytics       ✅
Business Insights          ✅
```

---

## 🎯 Data Engineering Skills Demonstrated

* AWS S3
* AWS Glue ETL
* AWS Glue Data Catalog
* Amazon Athena
* Apache Parquet
* SQL Analytics
* ETL Pipeline Development
* Cloud Data Lake Architecture
* Raw and Processed Data Layers
* Metadata Management
* Data Transformation
* Serverless Data Analytics
* Git & GitHub

---

## 🔮 Future Enhancements

The project can be extended into a production-oriented data platform by implementing:

* Incremental data processing
* S3 partitioning
* AWS Glue Job Bookmarks
* Data quality validation
* CloudWatch monitoring and alerts
* IAM least-privilege policies
* Scheduled Glue workflows
* Event-driven processing
* Amazon QuickSight dashboards
* CI/CD for ETL pipelines
* Additional retail datasets
* Automated data ingestion

---

## 📸 Project Screenshots

Screenshots demonstrating the AWS pipeline will be added to this repository, including:

* Amazon S3 raw data
* AWS Glue ETL job
* Successful Glue job execution
* S3 processed Parquet files
* AWS Glue Data Catalog
* Amazon Athena queries
* Athena analytical results

---

## 💼 Resume Project Description

**AWS Retail Data Engineering Pipeline**

> Developed an end-to-end AWS retail data engineering pipeline using Amazon S3, AWS Glue, Glue Data Catalog, Apache Parquet, and Amazon Athena. Implemented an ETL workflow to process raw CSV sales data into optimized Parquet format, cataloged the processed dataset, and performed SQL-based analytics for regional, product, category, and monthly sales insights.

---

## 👨‍💻 Author

**Chandra Sekhar**

**Data Engineering | AWS | SQL | ETL | Cloud Data Platforms**

---

⭐ If you found this project useful, feel free to explore the repository and connect with me.
