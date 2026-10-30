# Databricks notebook source
# MAGIC %md
# MAGIC ### Data Reading

# COMMAND ----------

#SHOW CATALOGS is used to list all available catalogs in a Spark or Databricks environment. It helps users identify available data domains and navigate the Unity Catalog hierarchy before accessing schemas and tables.
spark.sql("SHOW CATALOGS").show(truncate=False)

# COMMAND ----------

#This command is used to list all files and folders inside the databricks-datasets directory in DBFS (Databricks File System).dbutils.fs → File System utilities in Databricks.ls() → Lists contents of a directory.
dbutils.fs.ls("dbfs:/databricks-datasets/")

# COMMAND ----------

#dbutils.fs.ls("dbfs:/") is used to view the root directories of the Databricks File System. It helps users explore available storage locations, verify uploaded files, and navigate datasets before reading them into Spark DataFrames.
dbutils.fs.ls("dbfs:/")

# COMMAND ----------

#SHOW CATALOGS is used to list all available catalogs in a Databricks or Spark environment. It helps users discover data locations and navigate the Unity Catalog hierarchy before accessing schemas and tables.
spark.sql("SHOW CATALOGS").show(truncate=False)

# COMMAND ----------

#SHOW TABLES is used to list all tables and views available in the current schema or a specified schema. It helps users verify existing objects, confirm table creation, and explore available data before running queries.
spark.sql("SHOW TABLES").show(truncate=False)

# COMMAND ----------

#spark.table("big_mart_sales") loads the Spark table big_mart_sales into a DataFrame. df.show() displays the first 20 rows of that DataFrame, allowing us to quickly inspect the data before performing transformations or analysis.

df = spark.table("big_mart_sales")
df.show()

# COMMAND ----------

#display(dbutils.fs.ls("/Volumes/workspace/default/raw")) is used to view all files and folders stored in a Unity Catalog Volume. It helps verify uploads, explore storage contents, and obtain file paths before loading data into Spark DataFrames.
display(dbutils.fs.ls("/Volumes/workspace/default/raw"))

# COMMAND ----------

#dbutils.fs.ls("/Volumes/workspace/default/raw") is used to list all files and directories present in the raw Unity Catalog Volume. It helps verify uploads, inspect storage contents, and obtain file paths before loading data into Spark.
dbutils.fs.ls("/Volumes/workspace/default/raw")

# COMMAND ----------

#spark.read.csv() → Reads a CSV file into a Spark DataFrame.header=True → Uses the first row as column names.inferSchema=True → Automatically detects data types (Integer, Double, String, etc.).df → Stores the data in a DataFrame.

df = spark.read.csv(
    "/Volumes/workspace/default/raw/sales_data.csv",
    header=True,
    inferSchema=True
)

display(df)

# COMMAND ----------

#df.show() is used to display the contents of a Spark DataFrame. By default, it shows the first 20 rows and helps verify data after loading or transforming it.
df.show()

# COMMAND ----------

#df.printSchema() is used to view the schema of a Spark DataFrame. It displays column names, data types, and nullability information, helping validate that the data has been loaded correctly.
df.printSchema()