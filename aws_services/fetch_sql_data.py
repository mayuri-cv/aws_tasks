from mysql.connector import connect
import pandas as pd
from pyspark.sql import SparkSession

appName = "PySpark MySQL Example - via mysql.connector"
master = "local"

spark = SparkSession.builder.master(master).appName(appName).getOrCreate()

# Establish a connection
conn = connect(user='root',
               database='glue_test',
               password='root',
               host="localhost",
               port=3306)

cursor = conn.cursor()

cursor.execute("SELECT * FROM emp")

result = cursor.fetchall()

df = spark.createDataFrame(result)
df.show()