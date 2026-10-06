-- Retail Sales Analytics Queries

-- 1. Total Sales
SELECT
    SUM(total_amount) AS total_sales
FROM sales_data;


-- 2. Total Orders
SELECT
    COUNT(DISTINCT order_id) AS total_orders
FROM sales_data;


-- 3. Sales by Region
SELECT
    region,
    SUM(total_amount) AS total_sales
FROM sales_data
GROUP BY region
ORDER BY total_sales DESC;


-- 4. Sales by Category
SELECT
    category,
    SUM(total_amount) AS total_sales
FROM sales_data
GROUP BY category
ORDER BY total_sales DESC;


-- 5. Top Products by Sales
SELECT
    product,
    SUM(total_amount) AS total_sales
FROM sales_data
GROUP BY product
ORDER BY total_sales DESC;


-- 6. Monthly Sales
SELECT
    strftime('%Y-%m', order_date) AS sales_month,
    SUM(total_amount) AS total_sales
FROM sales_data
GROUP BY sales_month
ORDER BY sales_month;


-- 7. Average Order Value
SELECT
    AVG(total_amount) AS average_order_value
FROM sales_data;


-- 8. Customer Sales
SELECT
    customer_id,
    SUM(total_amount) AS total_sales
FROM sales_data
GROUP BY customer_id
ORDER BY total_sales DESC;