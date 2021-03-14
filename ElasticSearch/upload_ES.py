import json
import boto3
import datetime
from botocore.vendored import requests
from elasticsearch import Elasticsearch, RequestsHttpConnection
import csv
from io import BytesIO

host = 'search-concierge-es-jxx6b4ugbw2hxzjliff2feen6e.us-west-2.es.amazonaws.com' 

es = Elasticsearch(
    hosts = [{'host': host, 'port': 443}],
    http_auth=("Master123", "Master123!"),
    use_ssl = True,
    verify_certs = True,
    connection_class = RequestsHttpConnection
)

print(es)
with open('Restaurants.csv', newline='') as f:
    reader = csv.reader(f)
    restaurants = list(reader)

restaurants = restaurants[1:]
for restaurant in restaurants:
    index_data = {
        'bID': restaurant[0],
        'cuisine': restaurant[7]
    }
    print ('dataObject', index_data)
    es.index(index="restaurants", doc_type="Restaurant", id=restaurant[0], body=index_data, refresh=True)
#es.indices.refresh(index="restaurant")