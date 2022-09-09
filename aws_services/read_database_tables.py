import configparser
from pyspark.sql import SparkSession
file = '../resources/config.ini'
config = configparser.ConfigParser()
config.read(file)
spark = SparkSession \
        .builder \
        .appName("database_connection_test") \
        .config("spark.jars", "../aws_services/mysql-connector-java-8.0.30.jar") \
        .getOrCreate()

rdbms = config.get('rdbms_name', 'name')
db = config.get('rdbms_name', 'database_name')
tables = config.get('rdbms_name', 'tables')
user = config.get('rdbms_name', 'user')
password = config.get('rdbms_name', 'password')
table_names = [table for table in tables.split(",")]
print(user,password)
if rdbms == 'mysql':
    url = f"jdbc:mysql://localhost:3306/{db}"
    driver = "com.mysql.jdbc.Driver"
    for table in table_names:
        df = spark.read\
            .format("jdbc") \
            .option("url", url) \
            .option("driver", driver) \
            .option("dbtable", table) \
            .option("user", user) \
            .option("password", password) \
            .load()
        df.show()

