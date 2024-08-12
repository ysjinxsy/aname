import nextcord #type: ignore
from nextcord.ext import commands #type: ignore
import aiosqlite #type: ignore
import logging
import os
from flask import Flask
from shared import guild_id
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

intents = nextcord.Intents.all()
guild_id = 1221092843288920065
client = commands.Bot(command_prefix="?", intents=intents)
DATABASE_PATH = "database.db"


discord_token = os.environ.get('TOKEN')
from flask import Flask

app = Flask(__name__)
port = int(os.environ.get('PORT', 5000))

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == "__main__":
    app.run(port=5000)
# Assuming you have commands defined in commands.py
from commands import *
client.run(discord_token)

