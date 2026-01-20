from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
MONGODB_URI = os.getenv("MONGODB_URI")

# Connect to MongoDB
client = MongoClient(MONGODB_URI)
db = client.get_database()  # uses 'app' from URI

# Collections
artists_collection = db["artists"]
new_events_collection = db["newevents"]
users_collection = db["users"]
emailevents_collection = db["emailevents"]