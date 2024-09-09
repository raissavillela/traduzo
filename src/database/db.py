from pymongo import MongoClient
import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "test_db_traduzo")

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
