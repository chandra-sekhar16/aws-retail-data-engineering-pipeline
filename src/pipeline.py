from ingestion import load_sales_data
from transformation import transform_sales_data
from loading import load_to_database


def run_pipeline():
    """
    Run the complete retail data pipeline.
    """

    # Step 1: Ingest
    df = load_sales_data("data/sample_sales.csv")

    # Step 2: Transform
    transformed_df = transform_sales_data(df)

    # Step 3: Load
    database_url = "sqlite:///sales.db"
    load_to_database(transformed_df, database_url)

    print("Pipeline completed successfully.")


if __name__ == "__main__":
    run_pipeline()
