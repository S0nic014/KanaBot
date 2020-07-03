import discord
import giphypop
from discord.ext import commands


class EventManager(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Event manager loaded.")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f"{member} has joined a server.")

    @commands.Cog.listener()
    async def on_memeber_remove(self, member):
        print(f"{member} has left a server.")


def setup(client):
    client.add_cog(EventManager(client))
