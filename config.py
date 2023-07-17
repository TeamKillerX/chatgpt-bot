from os import getenv
from dotenv import load_dotenv

load_dotenv("config.env")

API_ID = int(getenv("29472662", 0))
API_HASH = getenv("b0498eb513a3e2edb10ba4d713dd6dee", "")
BOT_TOKEN = getenv("6169793838:AAFFUfd37emgFZ3ikcg_XudE-0H4FCJCHD0", "")
OPENAI_API = getenv("OPENAI_API", "") # get api key : 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
