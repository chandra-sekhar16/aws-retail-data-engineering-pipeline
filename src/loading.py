import pandas as pd
from sqlalchemy import create_engine


def load_to_database(df, database_url):
    """
    Load transformed sales data into a relational database.
    """

    engine = create_engine(database_url)

    try:
        df.to_sql(
            "sales_data",
            engine,
            if_exists="replace",
            index=False
        )

        print("Data loaded successfully into sales_data table.")

    except Exception as e:
        print(f"Error loading data: {e}")

    finally:
        engine.dispose()


if __name__ == "__main__":
    print("Loading module ready.")
