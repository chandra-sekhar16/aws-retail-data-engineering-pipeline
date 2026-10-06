import csv
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "sample_sales.csv"
DB_FILE = BASE_DIR / "retail.db"


def create_table(connection):
    connection.executescript("""
    CREATE TABLE IF NOT EXISTS sales_data (
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
    """)


def load_data(connection):
    with open(DATA_FILE, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        rows = []

        for row in reader:
            quantity = int(row["quantity"])
            unit_price = float(row["unit_price"])
            total_amount = quantity * unit_price

            rows.append((
                int(row["order_id"]),
                row["order_date"],
                row["customer_id"],
                row["product"],
                row["category"],
                quantity,
                unit_price,
                row["region"],
                total_amount
            ))

    connection.executemany(
        """
        INSERT OR IGNORE INTO sales_data
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        rows
    )

    connection.commit()

    print(f"Loaded {len(rows)} records successfully.")


def main():
    connection = sqlite3.connect(DB_FILE)

    try:
        create_table(connection)
        load_data(connection)
        print("ETL pipeline completed successfully.")
    finally:
        connection.close()


if __name__ == "__main__":
    main()