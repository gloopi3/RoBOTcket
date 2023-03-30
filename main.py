import json
import disnake
from disnake.ext import commands

bot = commands.Bot(command_prefix=disnake.ext.commands.when_mentioned)

with open('config.json') as c:
    config = json.load(c)
    token = config["TOKEN"]
    tbakey = config["TBA_API_KEY"]

@bot.slash_command()
async def ping(ctx):
    await ctx.send("pong!")

@bot.slash_command()
async def github(ctx):
    await ctx.send("Check out my github repo! https://github.com/gloopi3/RoBOTcket")

@bot.slash_command()
async def team(ctx, number: int):
    response = requests.get(f"https://www.thebluealliance.com/api/v3/team/frc{number}" + "?X-TBA-Auth-Key=" + tbakey)
    r = response.json()
    embed = disnake.Embed(title=f"FRC Team {number}")
    embed.add_field(name="Name:", value=r['nickname'])
    embed.add_field(name="Location:", value=r['city'] + ", " + r['state_prov'])
    embed.add_field(name="School:", value=r['school_name'])
    embed.add_field(name="Rookie Year:", value=r['rookie_year'])
    embed.add_field(name="Website:", value=r['website'])
    embed.add_field(name="TBA Page:", value=f"[link](https://www.thebluealliance.com/team/{number})")
    await ctx.send(embed=embed)

bot.run(token)
