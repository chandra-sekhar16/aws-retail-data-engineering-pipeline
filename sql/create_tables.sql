CREATE TABLE sales_data (
    order_id INTEGER,
    order_date DATE,
    customer_id VARCHAR(50),
    product VARCHAR(100),
    category VARCHAR(100),
    quantity INTEGER,
    unit_price DECIMAL(10, 2),
    region VARCHAR(50),
    total_amount DECIMAL(12, 2)
);
