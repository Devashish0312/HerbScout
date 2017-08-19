from elasticsearch import Elasticsearch
from pymongo import MongoClient

client = MongoClient('localhost:27017')
db = client.random_data

data = db.information.find()

es = Elasticsearch()

for i in data:
    es.index('herbs_random_data', 'doc', {
        'botanical_name': i['botanical_name'],
        'family': i['family'],
        'places': i['places'],
        'properties': i['properties']})
