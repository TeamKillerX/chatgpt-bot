import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()
API_ID = os.environ["API_ID"]
API_HASH = os.environ["API_HASH"]
ADMINS = os.environ["ADMINS"]
BOT_TOKEN = os.environ["BOT_TOKEN"]
MONGO_URL = os.environ["MONGO_URL"]
