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

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1663335336668 = glueContext.create_dynamic_frame.from_catalog(
    database="dynamodb-music",
    table_name="music",
    transformation_ctx="AWSGlueDataCatalog_node1663335336668",
)

# Script generated for node Amazon S3
AmazonS3_node1663335386160 = glueContext.getSink(
    path="s3://mysql-data-retrive/dynamodb-music/",
    connection_type="s3",
    updateBehavior="LOG",
    partitionKeys=[],
    enableUpdateCatalog=True,
    transformation_ctx="AmazonS3_node1663335386160",
)
AmazonS3_node1663335386160.setCatalogInfo(
    catalogDatabase="dynamodb-music", catalogTableName="music"
)
AmazonS3_node1663335386160.setFormat("json")
AmazonS3_node1663335386160.writeFrame(AWSGlueDataCatalog_node1663335336668)
job.commit()
