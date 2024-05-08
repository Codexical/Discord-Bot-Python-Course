import discord
from discord.ext import commands

# ==========TODO==========

TOKEN = "YOUR_BOT_TOKEN"

prefix = "-"

# ========================

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=prefix, intents=intents)


@bot.event
async def on_ready():
    print(f"Login --> {bot.user}")


# ==========TODO==========


@bot.command()
async def test(ctx, *args):
    print(args)


# ========================

bot.run(TOKEN)
