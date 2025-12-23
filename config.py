import os

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

HOST = os.environ.get("REDIS_HOST")
PORT = int(os.environ.get("REDIS_PORT"))
PASSWORD = os.environ.get("REDIS_PASSWORD", "")

PRIVATE_CHAT_ID = int(os.environ.get("PRIVATE_CHAT_ID"))
COOKIE = os.environ.get("COOKIE")

ADMINS = list(map(int, os.environ.get("ADMINS").split(",")))
