from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.functions import col, avg, count, round

# Create Spark Session
spark = SparkSession.builder \
    .appName("SparkOperationsDemo") \
    .master("local[*]") \
    .getOrCreate()

# --------------------------------
# 1. Create Employee DataFrame
# --------------------------------

employees = [
    (1, "Arun", 101, 30000),
    (2, "Bala", 102, 40000),
    (3, "Chitra", 103, 50000),
    (4, "David", 101, 35000)
]

emp_columns = ["emp_id", "emp_name", "dept_id", "salary"]

emp_df = spark.createDataFrame(employees, emp_columns)

print("Employee Data")
emp_df.show()


# --------------------------------
# 2. Create Department DataFrame
# --------------------------------

departments = [
    (101, "IT"),
    (102, "HR"),
    (103, "Finance"),
    (104, "Sales")
]

dept_columns = ["dept_id", "dept_name"]

dept_df = spark.createDataFrame(departments, dept_columns)

print("Department Data")
dept_df.show()


# =================================
# 3. TRANSFORMATIONS
# =================================

# Transformation 1: Select
emp_df.select("emp_name", "salary").show()

# Transformation 2: Filter
emp_df.filter(col("salary") > 35000).show()

# Transformation 3: WithColumn
emp_df.withColumn(
    "bonus",
    col("salary") * 0.10
).show()

# Transformation 4: GroupBy
emp_df.groupBy("dept_id").sum("salary").show()


# =================================
# 4. JOINS
# =================================

# Inner Join
inner_df = emp_df.join(
    dept_df,
    emp_df.dept_id == dept_df.dept_id,
    "inner"
)

print("INNER JOIN")
inner_df.show()

# Left Join
left_df = emp_df.join(
    dept_df,
    "dept_id",
    "left"
)

# left_df = emp_df.join(dept_df, on="dept_id",how="left")

print("LEFT JOIN")
left_df.show()


# =================================
# 5. UNION
# =================================

# Create another Employee DataFrame
new_employees = [
    (5, "Kumar", 102, 45000),
    (6, "Priya", 103, 55000)
]

new_emp_df = spark.createDataFrame(
    new_employees,
    emp_columns
)

# Union
union_df = emp_df.union(new_emp_df)

print("UNION RESULT")
union_df.show()


# =================================
# 6. ACTIONS
# =================================

# Action 1: Show
emp_df.show()

# Action 2: Count
print("Total Employees:", emp_df.count())

# Action 3: Collect
print("Collect:", emp_df.collect())

# Action 4: First
print("First Record:", emp_df.first())

# Action 5: Take
print("First Two Records:", emp_df.take(2))


# Stop Spark Session
spark.stop()
