from pyspark.sql import SparkSession
import boto3

spark = SparkSession.builder.config("spark.jars", "../aws_services/mysql-connector-java-8.0.30.jar") \
    .master("local").appName("PySpark_MySQL_test").getOrCreate()

emp_df = spark.read\
    .format("jdbc") \
    .option("url", "jdbc:mysql://localhost:3306/glue_test") \
    .option("driver", "com.mysql.jdbc.Driver") \
    .option("dbtable", "emp") \
    .option("user", "root") \
    .option("password", "root") \
    .load()

emp_df.show()

