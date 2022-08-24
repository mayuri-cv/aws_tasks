#############################################
#This is code to read csv file from s3 bucket using boto3
#apply transformation
#write to s3
############################################


import boto3
import pandas as pd
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('FirstAWS').getOrCreate()
s3 = boto3.client('s3')
s3 = boto3.resource(
    service_name='s3',
    region_name='us-east-2',
    aws_access_key_id='AKIASY7ODLDQ23O2ZNWD',
    aws_secret_access_key='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'
)

for bucket in s3.buckets.all():
    print(bucket.name)
filename = 'employees.csv'
s3.Bucket('s3buckettrial1').download_file(Key='employees.csv', Filename=filename)
df = spark.read.csv(filename,header=True, inferSchema=True)
df.show()

new_df = df.drop_duplicates().orderBy('emp_id')
new_df.show()
new_df.toPandas().to_csv('new_emp.csv')
s3.Bucket('s3buckettrial1').upload_file(Filename='new_emp.csv', Key='new_employee.csv')