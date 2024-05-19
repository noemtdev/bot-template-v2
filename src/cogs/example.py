import discord
from discord.ext import commands
from discord import option

from src.util.cog import Cog

class Example(Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name="example",
        description="An example command."
    )
    @option(
        name="example_option",
        description="An example option.",
        type=str,
        required=True
    )
    async def example(self, ctx: discord.ApplicationContext, example_option: str):
        await ctx.respond(f"Example option: {example_option}")

def setup(bot):
    bot.add_cog(Example(bot))