from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col,
    trim,
    to_date,
    round,
    when
)
from pyspark.sql.types import (
    LongType,
    DoubleType
)


def create_spark_session():
    """
    Create and configure Spark session.
    """
    return (
        SparkSession.builder
        .appName("RetailSalesETL")
        .config("spark.hadoop.fs.file.impl", "org.apache.hadoop.fs.LocalFileSystem")
        .config("spark.hadoop.fs.file.impl.disable.cache", "true")
        .getOrCreate()
    )

def read_source_data(spark, input_path):
    """
    Read retail sales CSV data from the source path.
    """
    return (
        spark.read
        .option("header", True)
        .option("inferSchema", True)
        .csv(input_path)
    )


def transform_data(df):
    """
    Clean and transform retail sales data.
    """

    transformed_df = (
        df
        .withColumn("order_id", col("order_id").cast(LongType()))
        .withColumn("quantity", col("quantity").cast(LongType()))
        .withColumn("unit_price", col("unit_price").cast(DoubleType()))
        .withColumn("order_date", to_date(col("order_date"), "yyyy-MM-dd"))
        .withColumn("customer_id", trim(col("customer_id")))
        .withColumn("product", trim(col("product")))
        .withColumn("category", trim(col("category")))
        .withColumn("region", trim(col("region")))
    )

    # Remove records with missing mandatory fields
    transformed_df = transformed_df.filter(
        col("order_id").isNotNull()
        & col("customer_id").isNotNull()
        & col("product").isNotNull()
        & col("order_date").isNotNull()
    )

    # Validate quantity and price
    transformed_df = transformed_df.filter(
        (col("quantity") > 0)
        & (col("unit_price") > 0)
    )

    # Calculate total sales amount
    transformed_df = transformed_df.withColumn(
        "total_sales",
        round(col("quantity") * col("unit_price"), 2)
    )

    # Add a simple data quality status
    transformed_df = transformed_df.withColumn(
        "data_quality_status",
        when(
            col("total_sales").isNotNull()
            & (col("total_sales") > 0),
            "VALID"
        ).otherwise("INVALID")
    )

    # Remove duplicate orders
    transformed_df = transformed_df.dropDuplicates(["order_id"])

    return transformed_df


def write_processed_data(df, output_path):
    """
    Write transformed data in Parquet format.
    """
    (
        df.write
        .mode("overwrite")
        .parquet(output_path)
    )


def main():
    """
    Main ETL execution.
    """

    input_path = "data/sample_sales.csv"
    output_path = "data/processed"

    spark = create_spark_session()

    try:
        print("Starting Retail Sales ETL pipeline...")

        # Extract
        print("Reading source data...")
        source_df = read_source_data(spark, input_path)

        print("Source record count:", source_df.count())

        # Transform
        print("Transforming data...")
        processed_df = transform_data(source_df)

        print("Processed record count:", processed_df.count())

        # Display transformed data
        processed_df.show(truncate=False)

        # Load
        print("Writing processed data to Parquet...")
        write_processed_data(processed_df, output_path)

        print("ETL pipeline completed successfully.")
        print("Output location:", output_path)

    except Exception as error:
        print("ETL pipeline failed.")
        print("Error:", error)
        raise

    finally:
        spark.stop()


if __name__ == "__main__":
    main()