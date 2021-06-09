from discord.ext import commands
from discord import Embed, Color


class Example(commands.Cog):
    """
    Represents a Cog for DEV.BG webinar example.
    """

    def __init__(self, bot):
        self.bot = bot
        number = 0

    @commands.command(aliases=('num?',))
    async def test(self, ctx, num: int):
        """
        The main command which handles the code execution process.
        """
        await ctx.send(f"The number entered {num}")
    
    @commands.command(aliases=('num'))
    async def test(self, ctx):
        await ctx.send(f"The number is {number}")
        number += 1

def setup(bot):
    bot.add_cog(Example(bot))
