import discord
import giphypop
from discord.ext import commands


class GifManager(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Gif manager loaded.")

    @commands.command()
    async def shiba(self, ctx):
        await ctx.send(giphypop.random_gif(tag="shibainu"))

    @commands.command()
    async def piggy(self, ctx):
        await ctx.send(giphypop.random_gif(tag="pig-piglet-piggy", strict=True))

    @commands.command()
    async def mood(self, ctx):
        await ctx.send(giphypop.random_gif(tag="mood"))

    @commands.command()
    async def pokemon(self, ctx):
        await ctx.send(giphypop.random_gif(tag="pokemon"))

    @commands.command()
    async def hamster(self, ctx):
        await ctx.send(giphypop.random_gif(tag="hamster"))


def setup(client):
    client.add_cog(GifManager(client))
