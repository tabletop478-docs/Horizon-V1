from data.config.imports import *
from data.config.vars import *

"""
"""

class control(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.remove_command("help")
        
    @has_permissions(manage_guild=True)
    @command(name="whitelist")
    async def whitelist(self, ctx, targets: Greedy[discord.Member]):
        for target in targets:
            try:
                db.field("UPDATE whitelisted SET userid = ?", target.id)
                
            except:
                pass
            await ctx.send(f"```Whitelisted {target.name}#{target.discriminator}```")

    @command(name="get")
    async def get(self, ctx, targets: Greedy[discord.Member]):
        targetids = []

        for target in targets:
            targetids.append(target.id)

        await ctx.send(targetids)

    @has_permissions(manage_guild=True)
    @command(name="blacklist")
    async def blacklist(self, ctx, targets: Greedy[discord.Member]):
        for target in targets:
            try:
                db.field("UPDATE blacklisted SET userid = ?", target.id)
                
            except:
                pass
            await ctx.send(f"```Blacklisted {target.name}#{target.discriminator}```")

    @has_permissions(manage_guild=True)
    @command(name="overseer")
    async def overseer(self, ctx, targets: Greedy[discord.Member]):
        for target in targets:
            try:
                db.field("UPDATE administrator SET userid = ?", target.id)
                
            except:
                pass
            await ctx.send(f"```Given overseer to {target.name}#{target.discriminator}```")

    @has_permissions(manage_guild=True)
    @command(name="appendally")
    async def appendally(self, ctx, *, target: Optional[str]):
        try:
            db.field("UPDATE allied SET guildid = ?", target)
            
        except:
            pass
        await ctx.send(f"```Appended {target} to allies```")

    @has_permissions(manage_guild=True)
    @command(name="removeally")
    async def removeally(self, ctx, *, target: Optional[str]):
        try:
            db.field("DELETE FROM allied WHERE guildid = ?", target)
            
        except:
            pass
        await ctx.send(f"```Removed {target} from allies```")

    @has_permissions(manage_guild=True)
    @command(name="appendenemy")
    async def appendenemy(self, ctx, *, target: Optional[str]):
        try:
            db.field("UPDATE enemy SET guildid = ?", target)
            
        except:
            pass
        await ctx.send(f"```Appended {target} to enemies```")

    @has_permissions(manage_guild=True)
    @command(name="removeenemy")
    async def removeenemy(self, ctx, *, target: Optional[str]):
        try:
            db.field("DELETE FROM enemy WHERE guildid = ?", target)
            
        except:
            pass
        await ctx.send(f"```Removed {target} from enemies```")
    
def setup(bot):
    bot.add_cog(control(bot))