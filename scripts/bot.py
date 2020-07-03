import discord
import os
from discord.ext import commands
from scripts.ui import trayApp
# import importlib
# importlib.reload(trayApp)

# Get token in user home path
TOKKEN_PATH = os.path.join(os.path.expanduser("~"), "discordToken.txt")
kanaBot = commands.Bot(command_prefix=".")


def getToken() -> str:
    with open(TOKKEN_PATH) as tokenFile:
        data = tokenFile.read()
    return data


# Extension commands
@kanaBot.command()
async def load(ctx, extension):
    kanaBot.load_extension(f"cogs.{extension}")


@kanaBot.command()
async def unload(ctx, extension):
    kanaBot.unload_extension(f"cogs.{extension}")


# Events
@kanaBot.event
async def on_ready():
    print("Kana Bot is ready.")


# Load cogs
for fileName in os.listdir("scripts/cogs"):
    if fileName.endswith(".py"):
        kanaBot.load_extension(f"cogs.{fileName[:-3]}")


# Run bot
# kanaBot.run(getToken())
# kanaBot.logout()
tray = trayApp.runTray(kanaBot, getToken())
