import discord
import giphypop
from discord.ext import commands


class TaskManager(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Task manager loaded.")


def setup(client):
    client.add_cog(TaskManager(client))
