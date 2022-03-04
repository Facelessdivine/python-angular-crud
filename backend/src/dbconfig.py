from flask_pymongo import pymongo
import os
from  dotenv import load_dotenv
load_dotenv(override=True)


URI = os.getenv('DB_URI')

client = pymongo.MongoClient(URI)
c_users = client.users

