# Built-in library imports
import asyncio
import json
import os

# discord.py imports
import discord
from discord.ext import commands

# My file imports
import file_paths

def retrieve_prefix(bot, message):
  """Returns server prefix for current server on bot startup"""

  with open(file_paths.SERVER_PREFIXES) as f:
    server_prefixes = json.load(f)

  return ('egg!', server_prefixes[str(message.guild.id)])

bot = commands.Bot(command_prefix=retrieve_prefix)
# bot.remove_command('help')  # removes the default help command
# TODO implement new help command and uncomment line above

# Loads all extensions (Cogs)
for filename in os.listdir('eggbort/cogs'):
  if filename.endswith('.py'):
    bot.load_extension('cogs.{}'.format(filename[:-3]))  # [:-3] gets rid of .py


bot.run(os.environ['EGGBORT_TOKEN'])
