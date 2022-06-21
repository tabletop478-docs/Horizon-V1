from data.config.imports import *
from data.config.vars import *

"""
"""

class info(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.remove_command("help")

def setup(bot):
    bot.add_cog(info(bot))