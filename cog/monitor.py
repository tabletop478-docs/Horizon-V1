from data.config.imports import *
from data.config.vars import *

class monitor(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.remove_command("help")

    @command(name="announcemedium")
    async def announcemedium(self, ctx):
        pass

    @command(name="scrapeguilds", aliases=["scrapeservers"])
    async def guildlist(self, ctx):

        guilds = []

        for guild in self.bot.guilds:
            guilds.append(f"{guild.id} | ({guild.name})")

        guildlist = '\n'.join(guilds)

        await ctx.send(f"""```fix
{len(guilds)} servers scraped

[guilds]
{guildlist}
[end guilds]            ```""")

    @command(name="getinvite", aliases=["getinv"])
    async def getinvite(self, ctx, guildid: Optional[int]):
        if guildid == 0:
            await ctx.send("Missing argument")

        channels = []

        for guild in self.bot.guilds:
            if guildid == int(guild.id):
                for channel in guild.text_channels:
                    channels.append(channel.id)
                    
                invchannel = random.choice(channels)
                invchannelid = guild.get_channel(invchannel)
                inv = await invchannelid.create_invite(max_uses=1, unique=True)

                await ctx.send(inv)
def setup(bot):
    bot.add_cog(monitor(bot))