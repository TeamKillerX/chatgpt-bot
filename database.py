import os
from pymongo import MongoClient
from dotenv import load_dotenv
import pymongo
from config import MONGO_URL

client = MongoClient(MONGO_URL)
db = client["chatgpt"]
collection = db["users"]

def start_bot(user_id):
    update_doc = {"user_id": user_id}
    return collection.update_one({"user_id": user_id}, {"$set": update_doc}, upsert=True)

def add_openai_api_key(user_id, api_key):
    update_doc = {"api_key": api_key}
    return collection.update_one({"user_id": user_id}, {"$set": update_doc}, upsert=True)

def get_openai_api_key(user_id):
    user = collection.find_one({"user_id": user_id})
    if user:
        return user.get("api_key")
    else:
        return None

def broadcast_only_bots():
    blacklist = []
    users = collection.find({})
    for get_user in users:
        if get_user:
            user_id = get_user.get("user_id")
            blacklist.append(user_id)
    return blacklist
