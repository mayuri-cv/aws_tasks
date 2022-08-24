import boto3, json
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb',endpoint_url="http://localhost:8000" ,region_name='us-west-2')
table = dynamodb.Table('Music')

resp = table.query(KeyConditionExpression=Key('Artist').eq('The Acme Band'))

print("The query returned the following items:")
for item in resp['Items']:
    print(json.dumps(item, indent=4, sort_keys=True))