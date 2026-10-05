import pandas as pd

from ingestion import load_data
from transformation import transform_data
from loading import load_to_database


def run_pipeline():
    """
    Run the complete retail sales data pipeline.
    """

    input_file = "data/sample_sales.csv"

    # Step 1: Extract
    df = load_data(input_file)

    # Step 2: Transform
    transformed_df = transform_data(df)

    # Step 3: Load
    database_url = "sqlite:///sales.db"
    load_to_database(transformed_df, database_url)

    print("Retail sales data pipeline completed successfully.")


if __name__ == "__main__":
    run_pipeline()
