from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
APP_ID = os.environ.get("APP_ID", "25281175")
APP_HASH = os.environ.get("APP_HASH", "6d99cb2b60a2c519fc1f99bd19565730")
SESSION = os.environ.get("SESSION")
elhzeyba = TelegramClient(StringSession(SESSION), APP_ID, APP_HASH)
elhzeyba.start()
