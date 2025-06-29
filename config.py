from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = "23803580"
# -------------------------------------------------------------
API_HASH = "7d91da02949db09dc81df55532c93863"
# --------------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", "7203514667:AAHNigYBk8WjEMPtFyQ--ZoX7fsAXjgbWRE")
STRING1 = getenv("STRING_SESSION", None)
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://spicychatbot:Nothing0000@cluster0.fspyv8c.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
OWNER_ID = int(getenv("OWNER_ID", "7381712992"))
SUPPORT_GRP = "SpicyxBots"
UPDATE_CHNL = "SpicyxNetwork"
OWNER_USERNAME = "NoMoreMaxim"
