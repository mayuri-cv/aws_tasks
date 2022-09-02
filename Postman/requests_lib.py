import json
import requests
from pprint import pprint
import boto3
from pyspark.sql import SparkSession

#GET data from URL
req = requests.get('https://jsonplaceholder.typicode.com/posts')

# Page encoding
e = req.encoding
print("Encoding: ",e)

# Response code
s = req.status_code
print("Response code: ",s)

# Response Time
t = req.elapsed
print("Response Time: ",t)


t = req.headers['Content-Type']
print("Header: ",t)

z = req.text
print("Content =", z[0:50])

#pprint(req.json())


##Write the GET data in file data_file

data = req.json()
print(data)
with open ("data_file","w") as File:
    json.dump(req.json(),File, indent=4)

##Write the file in s3 bucket

spark = SparkSession.builder.appName('FirstAWS').getOrCreate()
s3 = boto3.client('s3')
s3 = boto3.resource(
    service_name='s3',
    region_name='us-east-2',
    aws_access_key_id='',
    aws_secret_access_key=''
)
s3.Bucket('s3buckettrial1').upload_file(Filename='../Postman/data_file', Key='data_file')
##POST request

in_values = {'title':'This is new title','body':'This is new body','userId':1}

res = requests.post('https://httpbin.org/post',data = in_values)
print(res.text)