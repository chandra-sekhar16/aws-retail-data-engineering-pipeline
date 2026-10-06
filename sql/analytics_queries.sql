-- AWS Retail Data Engineering Pipeline
-- Amazon Athena Analytics Queries
-- Database: retail_sales_db
-- Table: retail_sales_processed


-- 1. Total Sales
SELECT
    SUM(quantity * unit_price) AS total_sales
FROM retail_sales_db.retail_sales_processed;


-- 2. Total Orders
SELECT
    COUNT(DISTINCT order_id) AS total_orders
FROM retail_sales_db.retail_sales_processed;


-- 3. Sales by Region
SELECT
    region,
    SUM(quantity * unit_price) AS total_sales
FROM retail_sales_db.retail_sales_processed
GROUP BY region
ORDER BY total_sales DESC;


-- 4. Sales by Category
SELECT
    category,
    SUM(quantity * unit_price) AS total_sales
FROM retail_sales_db.retail_sales_processed
GROUP BY category
ORDER BY total_sales DESC;


-- 5. Top Products by Sales
SELECT
    product,
    SUM(quantity * unit_price) AS total_sales
FROM retail_sales_db.retail_sales_processed
GROUP BY product
ORDER BY total_sales DESC;


-- 6. Monthly Sales
SELECT
    substr(order_date, 1, 7) AS sales_month,
    SUM(quantity * unit_price) AS total_sales
FROM retail_sales_db.retail_sales_processed
GROUP BY substr(order_date, 1, 7)
ORDER BY sales_month;


-- 7. Average Order Value
SELECT
    SUM(quantity * unit_price) / COUNT(DISTINCT order_id) AS average_order_value
FROM retail_sales_db.retail_sales_processed;


-- 8. Customer Sales
SELECT
    customer_id,
    SUM(quantity * unit_price) AS total_sales
FROM retail_sales_db.retail_sales_processed
GROUP BY customer_id
ORDER BY total_sales DESC;


-- 9. Sales by Product Category
SELECT
    category,
    product,
    SUM(quantity * unit_price) AS total_sales
FROM retail_sales_db.retail_sales_processed
GROUP BY category, product
ORDER BY total_sales DESC;


-- 10. Top Performing Region and Product
SELECT
    region,
    product,
    SUM(quantity * unit_price) AS total_sales
FROM retail_sales_db.retail_sales_processed
GROUP BY region, product
ORDER BY total_sales DESC;