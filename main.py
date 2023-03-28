import json
import disnake
from disnake.ext import commands

bot = commands.Bot(command_prefix=disnake.ext.commands.when_mentioned)

with open('config.json') as c:
    config = json.load(c)
    token = config["TOKEN"]

@bot.slash_command()
async def ping(ctx):
    await ctx.send("pong!")

bot.run(token)