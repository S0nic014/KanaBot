import logging
from discord.ext import commands

LOGGER = logging.getLogger(__name__)


class AdminTool(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        # print("Admin commands loaded.")
        LOGGER.info("Admin commands loaded.")

    @commands.command()
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount)


def setup(client):
    client.add_cog(AdminTool(client))
