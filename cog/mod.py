from data.config.imports import *
from data.config.vars import *

class mod(Cog):
    def __init__(self, bot):
        self.bot = bot
      
    @has_permissions(manage_guild=True)
    @command(name="mute", aliases=["supress"])
    async def mutemember(self, ctx, targets: Greedy[discord.Member], *, reason: Optional[str] = "N/A"):
        guild = ctx.guild

        mutedrole = discord.utils.get(guild.roles, name = "muted")

        if not mutedrole:
            mutedrole = await guild.create_role(name = "muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedrole, speak=False, send_messages=False, read_message_history=False)

        if not len(targets):
          await ctx.send(MISSING)

        else:
            unmutes = []

        for target in targets:
            if (ctx.guild.me.top_role.position > target.top_role.position):

                if target.id == ctx.message.author.id:
                      await ctx.send(f"You cant mute yourself")
                      return
    
                await target.send(f"``MUTED IN {guild.name} FOR:``{reason}``")
    
                await target.edit(roles=[mutedrole])
    
                embed = discord.Embed(title=f"``{target.name}#{target.discriminator} MUTED``",
                                        colour=target.colour)
    
                embed.set_thumbnail(url=ctx.author.avatar_url)
    
                fields = [("VICTIM", f"{target.display_name}#{target.discriminator}", False),
                          ("COMMIT BY", f"{ctx.author.display_name}#{ctx.author.discriminator}", False),
                          ("REASON", f"```{reason}```", False)]
        
                for name, value, inline in fields:
                    embed.add_field(name=name, value=value, inline=inline)
    
                await ctx.send(embed=embed)

            else:
                embed = discord.Embed(title=f"{target.name}#{target.discriminator} COULD NOT BE MUTED",
                                        colour=target.colour)

                embed.set_thumbnail(url=ctx.author.avatar_url)

                await ctx.send(embed=embed)

        await ctx.send(PROCESS)
        
    @has_permissions(manage_guild=True)
    @command(name="unmute", aliases=["unsupress"])
    async def unmutemember(self, ctx, targets: Greedy[discord.Member]):
        guild = ctx.guild
  
        mutedrole = discord.utils.get(guild.roles, name = "muted")
  
        if not len(targets):
            await ctx.send(MISSING)
            return

        for target in targets:

            await target.send(f"``UNMUTED FROM {guild.name} FOR:``")
            
            await target.remove_roles(mutedrole)
  
            embed = discord.Embed(title=f"{target.name}#{target.discriminator} UNMUTED",
                                  colour=target.colour)
  
            embed.set_thumbnail(url=ctx.author.avatar_url)
  
            fields = [("VICTIM", f"{target.display_name}#{target.discriminator}", False),
                      ("COMMIT BY", f"{ctx.author.display_name}#{ctx.author.discriminator}", False)]
  
            for name, value, inline in fields:
              embed.add_field(name=name, value=value, inline=inline)
  
            await ctx.send(embed=embed)
          
    @has_permissions(manage_guild=True)
    @command(name="kick")
    async def kickmember(self, ctx, targets: Greedy[discord.Member], *, reason: Optional[str] = "N/A"):
        guild = ctx.guild

        if not len(targets):
            await ctx.send(MISSING)
            return 
  
        for target in targets:
            if (ctx.guild.me.top_role.position > target.top_role.position):
  
                if target.id == ctx.message.author.id:
                    await ctx.send(f"``You cant kick yourself``")
                    return

                await target.kick(reason=reason)
      
                embed = discord.Embed(title=f"``{target.name}#{target.discriminator} KICKED``",
                                          colour=target.colour)
      
                embed.set_thumbnail(url=ctx.author.avatar_url)
      
                fields = [("VICTIM", f"{target.display_name}#{target.discriminator}", False),
                          ("COMMIT BY", f"{ctx.author.display_name}#{ctx.author.discriminator}", False),
                          ("REASON", f"```{reason}```", False)]
      
                for name, value, inline in fields:
                    embed.add_field(name=name, value=value, inline=inline)
      
                await ctx.send(embed=embed)
                
            else:
                embed = discord.Embed(title=f"{target.name}#{target.discriminator} COULD NOT BE KICKED",
                                      colour=target.colour)
      
                embed.set_thumbnail(url=ctx.author.avatar_url)
      
                await ctx.send(embed=embed)
  
            await ctx.send(PROCESS)
      
    @command(name="ban")
    async def banmember(self, ctx, targets: Greedy[discord.Member], reason: Optional[str] = "N/A"):
        guild = ctx.guild
  
        if not len(targets):
            await ctx.send(MISSING)
            return
  
        for target in targets:
            if (ctx.guild.me.top_role.position > target.top_role.position):
    
                if target.id == ctx.message.author.id:
                    await ctx.send(f"``You cant banish yourself``")
                    return

                await target.ban(reason=reason)
      
                embed = discord.Embed(title=f"``{target.name}#{target.discriminator} BANISHED``",
                                          colour=target.colour)
      
                embed.set_thumbnail(url=ctx.author.avatar_url)
      
                fields = [("VICTIM", f"{target.display_name}#{target.discriminator}", False),
                          ("COMMIT BY", f"{ctx.author.display_name}#{ctx.author.discriminator}", False),
                          ("REASON", f"```{reason}```", False)]
      
                for name, value, inline in fields:
                    embed.add_field(name=name, value=value, inline=inline)
      
                await ctx.send(embed=embed)
              
            else:
                embed = discord.Embed(title=f"{target.name}#{target.discriminator} COULD NOT BE BANNED",
                                    colour=target.colour)
    
                embed.set_thumbnail(url=ctx.author.avatar_url)
    
                await ctx.send(embed=embed)
    
        await ctx.send(PROCESS)
      
    @has_permissions(manage_guild=True)
    @command(name="unban")
    async def unbanmember(self, ctx, targets: Greedy[discord.Member]):
        guild = ctx.guild
        
        if not len(targets):
            await ctx.send(MISSING)
            return
  
        for target in targets:

            if target.id == ctx.message.author.id:
                await ctx.send(f"``You arent banned``")
                return
    
            await target.unban()
    
            embed = discord.Embed(title=f"``{target.name}#{target.discriminator} BANISHED``",
                                  colour=target.colour)
    
            embed.set_thumbnail(url=ctx.author.avatar_url)
    
            fields = [("VICTIM", f"{target.display_name}#{target.discriminator}", False),
                      ("COMMIT BY", f"{ctx.author.display_name}#{ctx.author.discriminator}", False),
                      ("REASON", f"```{reason}```", False)]

            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)
    
            await ctx.send(embed=embed)
    
        await ctx.send(PROCESS)

    @command(name="purge", aliases=["delete"])
    async def purge(self, ctx, amount: Optional[int] = 3):
        guild = ctx.guild

        await ctx.message.delete()

        def check(message):
            return not message.pinned

        lp = await ctx.channel.purge(limit=amount, check=check)
        em = await ctx.send(f"```Purged {len(lp)} messages```")
        
        time.sleep(5)
        await em.delete()
        
def setup(bot):
    bot.add_cog(mod(bot))
