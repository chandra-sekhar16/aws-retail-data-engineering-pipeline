import pandas as pd

from ingestion import load_sales_data
from transformation import transform_sales_data
from loading import load_to_database


def run_pipeline():
    """
    Run the complete retail sales data pipeline.
    """

    input_file = "data/sample_sales.csv"

    # Step 1: Extract
    sales_data = load_sales_data(input_file)

    # Step 2: Transform
    transformed_data = transform_sales_data(sales_data)

    # Step 3: Load
    database_url = "sqlite:///sales.db"
    load_to_database(transformed_data, database_url)

    print("Retail sales data pipeline completed successfully.")


if __name__ == "__main__":
    run_pipeline()
