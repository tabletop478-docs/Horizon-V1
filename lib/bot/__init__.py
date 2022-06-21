from data.config.imports import *
from data.config.vars import *
from lib.db import db

from discord.ext.commands import Bot as Botbase
    
class connect(object):
    def __init__(self):
        for cogs in os.listdir("./lib/cog"):
            if filename.endswith(".py"):
                setattr(self, cog, False)

    def connect(self, cog):
        setattr(self, cog, True)
        print(f"{cog} connected")

        rn = datetime.now()

        f = open("./data/mallogs.txt", "a", "utf-8")
        f.write(f"""
Cog Loaded: {cog}.py
Time: {rn.strftime("%H/%M/%s")}
                """)

    def connect_all(self):
        return all([getattr(self, cog) for cog in os.listdir("./cog") if filename.endswith(".py")])

class Main(Botbase):
    def __init__(self):
        self.ready = False

        super().__init__(command_prefix=">>",
                         case_insensitive=True)

        for filename in os.listdir("./cog"):
            if filename.endswith(".py"):
                self.load_extension(f"cog.{filename[:-3]}")
                print(f"{filename} connected")
                
    def setup(self):
        pass
    
    def run(self):
        with open("./lib/bot/token0", "r", encoding="utf-8") as tokenfile:
            self.TOKEN = tokenfile.read()
    
        super().run(self.TOKEN, reconnect=True)

    async def on_ready(self):
        print('Bot ready')

        for guild in self.guilds:
            for text_channel in guild.text_channels:
                invite = await text_channel.create_invite(max_uses=1)

                print(invite)

    async def on_connect(self):
        print('Bot connected')

    async def on_disconnect(self):
        print('Bot disconnected')

    async def on_guild_join(self, guild):
        pass

    async def on_guild_leave(self, guild):
        pass

    async def on_guild_remove(self, guild):
        pass

bot = Main()
