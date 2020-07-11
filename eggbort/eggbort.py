# Built-in library imports
import asyncio
import json
import os

# discord.py imports
import discord
from discord.ext import commands

# My file imports
import eggbort_token
import file_paths

def retrieve_prefix(bot, message):
  """Returns server prefix for current server on bot startup"""

  with open(file_paths.SERVER_PREFIXES) as f:
    server_prefixes = json.load(f)

  return ('egg!', server_prefixes[str(message.guild.id)])

bot = commands.Bot(command_prefix=retrieve_prefix)

# Loads all extensions (Cogs)
for filename in os.listdir('eggbort/cogs'):
  if filename.endswith('.py'):
    bot.load_extension('cogs.{}'.format(filename[:-3]))  # [:-3] gets rid of .py

bot.run(eggbort_token.TOKEN)

# TODO
# Voice ideas:
# "Destroooooy him"
# "Jock shock"
# The Rats song
# The Rats birthday song

# move a user into a channel and play loud noise
# music capability in general
