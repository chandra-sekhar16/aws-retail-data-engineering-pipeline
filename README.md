# AWS Retail Data Engineering Pipeline

## Project Overview

This project demonstrates an end-to-end retail data engineering pipeline using Python, SQL, and AWS-oriented data engineering concepts.

The project processes retail sales data, stores it in a relational database, and performs analytical queries to generate business insights.

## Architecture

```text
Retail Sales Data
       |
       v
   Python ETL
       |
       v
 Data Validation
       |
       v
 SQLite Database
       |
       v
  SQL Analytics
       |
       v
 Business Insights
```

## Technologies Used

* Python 3.14
* SQL
* SQLite
* AWS Data Engineering Concepts
* Git & GitHub

## Project Structure

```text
aws-retail-data-engineering-pipeline/
|
+-- data/
|   +-- sales_data.csv
|
+-- sql/
|   +-- create_tables.sql
|   +-- analytics_queries.sql
|
+-- scripts/
|
+-- retail.db
|
+-- README.md
```

## Database Schema

The `sales_data` table contains:

| Column       | Description             |
| ------------ | ----------------------- |
| order_id     | Unique order identifier |
| order_date   | Date of the order       |
| customer_id  | Customer identifier     |
| product      | Product name            |
| category     | Product category        |
| quantity     | Quantity purchased      |
| unit_price   | Price per unit          |
| region       | Sales region            |
| total_amount | Total order amount      |

## SQL Analytics

The project includes SQL queries for:

1. Total sales
2. Total orders
3. Sales by region
4. Sales by category
5. Top products
6. Monthly sales
7. Average order value
8. Customer sales

## Current Analytics Results

Based on the sample dataset:

| Metric             |      Result |
| ------------------ | ----------: |
| Total Sales        |     204,500 |
| Total Orders       |           6 |
| Top Region         |       South |
| South Region Sales |     117,000 |
| Top Category       | Electronics |
| Electronics Sales  |     172,500 |

## How to Run

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd aws-retail-data-engineering-pipeline
```

### 2. Create the database

```bash
python -c "import sqlite3; conn=sqlite3.connect('retail.db'); conn.executescript(open('sql/create_tables.sql').read()); conn.commit(); conn.close(); print('Database and table created successfully')"
```

### 3. Load sample data

```bash
python -c "import sqlite3; conn=sqlite3.connect('retail.db'); conn.executemany('INSERT INTO sales_data VALUES (?,?,?,?,?,?,?,?,?)', [(1001,'2026-01-05','C001','Laptop','Electronics',1,75000,'South',75000),(1002,'2026-01-10','C002','Phone','Electronics',2,30000,'East',60000),(1003,'2026-02-03','C003','Chair','Furniture',4,5000,'West',20000),(1004,'2026-02-15','C001','Desk','Furniture',1,12000,'South',12000),(1005,'2026-03-01','C004','Headphones','Electronics',3,2500,'North',7500),(1006,'2026-03-12','C005','Monitor','Electronics',2,15000,'South',30000)]); conn.commit(); conn.close(); print('Sample sales data loaded successfully')"
```

### 4. Run Analytics

The SQL queries are available in:

```text
sql/analytics_queries.sql
```

## Future AWS Architecture

The local prototype can be extended into an AWS-based production pipeline:

```text
Amazon S3
   |
   v
AWS Glue
   |
   v
Amazon Redshift
   |
   v
Amazon QuickSight
```

### AWS Services

* **Amazon S3** - Data lake storage
* **AWS Glue** - ETL and data catalog
* **Amazon Redshift** - Data warehouse
* **Amazon QuickSight** - Business intelligence dashboards

## Key Skills Demonstrated

* Python data processing
* SQL analytics
* Relational database design
* ETL pipeline concepts
* Data validation
* Business analytics
* AWS data engineering architecture
* Git/GitHub project organization

## Author

**Data Engineering Portfolio Project**

This project was created to demonstrate practical data engineering and analytics skills.
