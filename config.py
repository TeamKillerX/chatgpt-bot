import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
ADMINS = int(os.getenv("ADMINS"))
BOT_TOKEN = os.getenv("BOT_TOKEN")
MONGO_URL= os.getenv("MONGO_URL")
