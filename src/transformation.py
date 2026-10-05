import pandas as pd


def transform_sales_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and transform retail sales data.
    """

    df = df.copy()

    # Remove duplicate records
    df = df.drop_duplicates()

    # Convert order date to datetime
    df["order_date"] = pd.to_datetime(df["order_date"])

    # Calculate total sales amount
    df["total_amount"] = df["quantity"] * df["unit_price"]

    # Remove invalid records
    df = df[
        (df["quantity"] > 0) &
        (df["unit_price"] > 0)
    ]

    # Sort by order date
    df = df.sort_values("order_date")

    return df


if __name__ == "__main__":
    data = pd.read_csv("data/sample_sales.csv")
    transformed_data = transform_sales_data(data)

    print(transformed_data)
