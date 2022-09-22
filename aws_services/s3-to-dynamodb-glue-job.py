import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node Data Catalog table
DataCatalogtable_node1 = glueContext.create_dynamic_frame.from_catalog(
    database="zipcodesdb",
    table_name="tablefors3todynamodb",
    transformation_ctx="DataCatalogtable_node1",
)

# id,zipcode,type,city,state,population
# Map the source field names and data types to target values.

Mapped = ApplyMapping.apply(frame=DataCatalogtable_node1, mappings=[
    ("id", "bigint", "id", "string"),
    ("zipcode", "bigint", "zipcode", "string"),
    ("type", "string", "type", "string"),
    ("city", "string", "city", "string"),
    ("state", "string", "state", "string"),
    ("population", "bigint", "population", "string")
],
     transformation_ctx="Mapped")

# Write to target DynamoDB table.
glueContext.write_dynamic_frame_from_options(
    frame=Mapped,
    connection_type="dynamodb",
    connection_options={
        "dynamodb.region": "us-east-1",
        "dynamodb.output.tableName": "zipcodes",
        "dynamodb.throughput.write.percent": "1.0"
    }
)

job.commit()
