from os import getenv
from dotenv import load_dotenv

load_dotenv("config.env")

API_ID = int(getenv("API_ID", 0))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OPENAI_API = getenv("OPENAI_API", "") # get api key : https://platform.openai.com/account/api-keys
