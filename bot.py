import discord
import logging
import asyncio
from discord.ext import commands

# .env
from dotenv import load_dotenv
import os

load_dotenv()
logging.basicConfig(level=logging.INFO)

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True 

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

bot = commands.Bot(command_prefix="!", intents=intents)

# events
@bot.event
async def on_ready():
    logging.info(f"logged in as {bot.user}")
    await bot.change_presence(activity=discord.Game(name="Template!"))

for folder in os.listdir("./cogs"):
    try:
        bot.load_extension(f"cogs.{folder}.__init__")
        logging.info(f"Cog {folder} loaded!")
    except Exception as e:
        logging.error(f"Cog {folder} not loaded, error: {e}")


bot.run(os.getenv("token"))