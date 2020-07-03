import discord
import giphypop
import os
from discord.ext import commands


kanaBot = commands.Bot(command_prefix=".")


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
kanaBot.run("NzI4MzY5MjE4NTI0OTM4MzUy.Xv5Yyg.CSuSZBbMs3-o-dkrO7bpefqFejw")
