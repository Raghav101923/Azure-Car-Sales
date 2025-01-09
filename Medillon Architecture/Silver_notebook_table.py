# Databricks notebook source
# MAGIC %md
# MAGIC # DATA READING

# COMMAND ----------

df = spark.read.format('parquet')\
                .option('inferSchema',True)\
                    .load('abfss://bronze@ragcardatalake.dfs.core.windows.net/rawdata')

# COMMAND ----------

df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC # DATA TRANSFORMATION

# COMMAND ----------

from pyspark.sql.functions import *
from pyspark.sql.types import *

# COMMAND ----------

df = df.withColumn('model_category', split(col('Model_ID'),'-')[0])
df.display()

# COMMAND ----------

df.withColumn('Units_Sokd', col('Units_Sold').cast(StringType())).printSchema()

# COMMAND ----------

df = df.withColumn('RevPerUnit',col('Revenue')/col('Units_Sold'))
df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC # AD-HOC

# COMMAND ----------

df.display()

# COMMAND ----------

df.groupBy('Year','BranchName').agg(sum('Units_Sold').alias('Total_Units')).sort('Year','Total_Units',ascending=[1,0]).display()

# COMMAND ----------

# MAGIC %md
# MAGIC #DATA WRITING

# COMMAND ----------

df.write.format('parquet')\
    .mode('append')\
        .option('path','abfss://silver@ragcardatalake.dfs.core.windows.net/carsales')\
            .save()

# COMMAND ----------

# MAGIC %md
# MAGIC #Querying Silver Data

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM parquet.`abfss://silver@ragcardatalake.dfs.core.windows.net/carsales`