import json  # module for converting Python objects to JSON
# decimal module support correctly-rounded decimal floating point arithmetic.
from decimal import Decimal
import boto3  # import Boto3


def load_data(mlist, dynamodb=None):
    dynamodb = boto3.resource(
        'dynamodb', endpoint_url="http://localhost:8000")

    music_table = dynamodb.Table('Music')
    # Loop through all the items and load each
    for item in mlist:
        Artist = (item['Artist'])
        SongTitle = item['SongTitle']
        # Print device info
        print("Loading Devices Data:", Artist, SongTitle)
        music_table.put_item(Item=item)


if __name__ == '__main__':
    # open file and read all the data in it
    with open("music_data.json") as json_file:
        music_list = json.load(json_file, parse_float=Decimal)
    load_data(music_list)