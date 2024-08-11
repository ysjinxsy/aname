import nextcord #type: ignore
from nextcord.ext import commands #type: ignore
import aiosqlite #type: ignore
import logging
import os
from shared import guild_id
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

intents = nextcord.Intents.all()
guild_id = [1266153230300090450, 1221092843288920065]
client = commands.Bot(command_prefix="?", intents=intents)
DATABASE_PATH = "database.db"

discord_token = os.getenv("TOKEN").strip()

# Assuming you have commands defined in commands.py
from commands import *

client.run(discord_token)

