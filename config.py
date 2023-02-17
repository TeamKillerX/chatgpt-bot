from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", 14429998))
API_HASH = getenv("API_HASH", "5282ba528684583fa35b7fc3ad433b0c")
BOT_TOKEN = getenv("BOT_TOKEN", "5850228712:AAEBNqngYJ9jgIyHtXAV1JHQjrd7cG0WH_s")
OPENAI_API = getenv("OPENAI_API", "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") # get api key : https://platform.openai.com/account/api-keys
