from data.config.imports import *
from data.config.vars import *

"""
"""

class cog(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.remove_command("help")

    @command(name="cog")
    async def cog(self, ctx):
        await ctx.send(f'cog ok')
        
def setup(bot):
    bot.add_cog(cog(bot))