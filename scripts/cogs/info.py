import giphypop
from discord.ext import commands


class InfoTool(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Info commands loaded.")

    # Commands
    @commands.command(aliases=["kanahelp"])
    async def kanaHelp(self, ctx):
        await ctx.send("Here is help on me >3>")

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"I'm {round(self.client.latency*1000)}ms slow uwu\n{giphypop.random_gif(tag='embarrassed')}")

    @commands.command()
    async def avatar(self, ctx):
        await ctx.send("Drawing by: https://twitter.com/Yoaihime")


def setup(client):
    client.add_cog(InfoTool(client))
