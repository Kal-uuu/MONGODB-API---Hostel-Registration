from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv

load_dotenv()


uri = (f"mongodb+srv://{os.getenv('USER')}:{os.getenv('PASSWORD')}@cluster0.dxx2gkl.mongodb.net/?retryWrites=true"
       f"&w=majority"
       "&appName"
       "=Cluster0")


client = MongoClient(uri, server_api=ServerApi('1'))

db = client.ug_hostels

collection = db["ug_host"]
