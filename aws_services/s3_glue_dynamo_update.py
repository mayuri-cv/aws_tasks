import sys
import os
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from datetime import datetime
from pyspark.sql.functions import count, col

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

RelationalDB_node1663246176753 = glueContext.create_dynamic_frame.from_catalog(
    database="mysql-sample-db",
    table_name="sample_db_user_details",
    transformation_ctx="RelationalDB_node1663246176753",
)

AmazonS3_node1663246224416 = glueContext.write_dynamic_frame.from_options(
    frame=RelationalDB_node1663246176753,
    connection_type="s3",
    format="json",
    connection_options={

        "path": "s3://mysql-data-retrive/data_for_mysql_to_dynamodb/29-09-2022/",
        "partitionKeys": ["user_id"],
    },
    transformation_ctx="AmazonS3_node1663246224416",
)

current_date = datetime.now()
new_date = current_date.strftime("%Y-%m-%d")

dyf = glueContext.create_dynamic_frame.from_options(
    connection_type="dynamodb",
    connection_options={
        "dynamodb.input.tableName": "SVB_Test",
        "dynamodb.throughput.read.percent": "1.0",
        "dynamodb.splits": "100"
    }
)

filtered_dyf = dyf.filter(f=lambda x: x["start_date"] == new_date)
x = filtered_dyf.count()

if x >= 1:
    print('For this date, job already ran')
    os._exit(0)
else:
    columns = ['job_name', 'start_date', 'end_date', 'status']
    data = [('SVB_Test', new_date, new_date, 'SUCCESS')]
    df = spark.createDataFrame(data=data, schema=columns)
    result_df = DynamicFrame.fromDF(df, glueContext, "result_df")

    write_df = glueContext.write_dynamic_frame_from_options(
        frame=result_df,
        connection_type="dynamodb",
        connection_options={
            "dynamodb.region": "us-east-1",
            "dynamodb.output.tableName": "SVB_Test",
            "dynamodb.throughput.write.percent": "1.0"
        },
        transformation_ctx="write_df"
    )

    job.commit()
