#   bot.py
import os
import sys
import traceback
from random import uniform, random, choice, sample

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='$', help_command=None, intents=intents)
client = discord.Client()

@client.event()
async def on_ready():
    print('OwO')

bot.run(TOKEN)
