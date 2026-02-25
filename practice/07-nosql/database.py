from pymongo import MongoClient, errors
from bson.json_util import dumps
import pprint
import os

# Use environment variables from README: MONGODB_ATLAS_URL, MONGODB_ATLAS_USER, MONGODB_ATLAS_PWD
uri = os.getenv('MONGODB_ATLAS_URL')
username = os.getenv('MONGODB_ATLAS_USER')
password = os.getenv('MONGODB_ATLAS_PWD')

# Connect to the MongoDB Atlas cluster
client = MongoClient(uri, username=username, password=password, connectTimeoutMS=200, retryWrites=True)

# Fetch list of collections and print total number of docs in each
for name in db.list_collection_names():
    count = db[name].count_documents({})
    print(f"{name}: {count} documents")

client.close()
print("Connection closed")