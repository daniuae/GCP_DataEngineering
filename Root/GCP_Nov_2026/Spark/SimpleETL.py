from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, count, round

def main():
    spark = SparkSession.builder.appName("1001_SimpleETL").getOrCreate()

    # 1) Read CSV
    df = (
        spark.read
        .option("header", True)
        .option("inferSchema", True)
        .csv("people.csv")
    )

    # 2) Basic cleanup
    df = df.dropna(subset=["city", "age", "salary"])

    # 3) Filter: keep adults 30+ / where condition
    df30 = df.filter(col("age") >= 30)
    df.explain()
    print("**********************************************")
    # 4) Aggregate: avg salary and count per city /  as
    result = (
        df30.groupBy("city")
            .agg(
                round(avg("salary"), 2).alias("avg_salary"),
                count("*").alias("num_employees")
            )
            .orderBy(col("avg_salary").desc())
    )

    # 5) Show in console
    result.show(truncate=False)

    # 6) Save results (CSV + Parquet) to local folders
    # coalesce(1) just to write one CSV part file for convenience in this tiny demo
    '''
        coalesce(1)
        Reduces the number of partitions to 1
        Ensures only one output CSV file is written
        ->  Without this, Spark would create multiple part-*.csv files (one per partition).
        -> Caution:
        coalesce(1) brings all data to one executor
        Can cause performance bottlenecks or OOM errors for large datasets
    '''
    result.coalesce(1).write.mode("overwrite").option("header", True).csv("output/avg_salary_by_city_csv")
    result.write.mode("overwrite").parquet("output/avg_salary_by_city_parquet")

    spark.stop()

if __name__ == "__main__":
    main()
