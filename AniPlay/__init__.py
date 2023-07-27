from os import environ
from pyrogram.client import Client

app = Client(
    "AniPlay",
    api_id= int(environ.get("APP_ID", "9976721")),
    api_hash= environ.get("API_HASH", "3ef17a8cdb938335bd8ba292e6d816aa"),
    bot_token= environ.get("TOKEN", "6474235595:AAFr8HaA_PrGFGFaBaTYgygAgfRENICcQs0")
)
