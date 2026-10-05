import pandas as pd


def load_sales_data(file_path: str) -> pd.DataFrame:
    """
    Load retail sales data from a CSV file.
    """
    df = pd.read_csv(file_path)

    print(f"Loaded {len(df)} records")
    print(f"Columns: {list(df.columns)}")

    return df


if __name__ == "__main__":
    data = load_sales_data("data/sample_sales.csv")
    print(data.head())
