-- Amazon Redshift Star Schema for Retail Sales Analytics

-- 1. Date Dimension
CREATE TABLE IF NOT EXISTS dim_date (
    date_id DATE PRIMARY KEY,
    day INT,
    month INT,
    quarter INT,
    year INT
)
DISTSTYLE ALL;

-- 2. Customer Dimension
CREATE TABLE IF NOT EXISTS dim_customer (
    customer_id VARCHAR(50) PRIMARY KEY,
    region VARCHAR(50)
)
DISTSTYLE ALL;

-- 3. Product Dimension
CREATE TABLE IF NOT EXISTS dim_product (
    product_name VARCHAR(100) PRIMARY KEY,
    category VARCHAR(50),
    unit_price NUMERIC(10,2)
)
DISTSTYLE ALL;

-- 4. Sales Fact Table
CREATE TABLE IF NOT EXISTS fact_retail_sales (
    order_id BIGINT PRIMARY KEY,
    order_date DATE REFERENCES dim_date(date_id),
    customer_id VARCHAR(50) REFERENCES dim_customer(customer_id),
    product_name VARCHAR(100) REFERENCES dim_product(product_name),
    category VARCHAR(50),
    quantity BIGINT,
    unit_price NUMERIC(10,2),
    total_sales NUMERIC(12,2),
    region VARCHAR(50),
    data_quality_status VARCHAR(20),
    created_at TIMESTAMP DEFAULT SYSDATE
)
DISTKEY(customer_id)
COMPOUND SORTKEY(order_date, region);