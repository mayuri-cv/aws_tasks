from mysql.connector import connect
import pandas as pd
from pyspark.sql import SparkSession
import configparser
file = '../resources/config.ini'
config = configparser.ConfigParser()
config.read(file)
appName = "PySpark MySQL Example - via mysql.connector"
master = "local"

spark = SparkSession.builder.master(master).appName(appName).getOrCreate()
user = config.get('fetch_sql_data_db', 'user')
db = config.get('fetch_sql_data_db', 'database')
table = config.get('fetch_sql_data_db', 'table-name')
host = config.get('fetch_sql_data_db', 'host')
password = config.get('fetch_sql_data_db', 'password')
port = config.get('fetch_sql_data_db', 'port')
# Establish a connection
conn = connect(user=user,
               database=db,
               password=password,
               host=host,
               port=port)

cursor = conn.cursor()

cursor.execute(f"SELECT * FROM {table}")

result = cursor.fetchall()

df = spark.createDataFrame(result)
df.show()