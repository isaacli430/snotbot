import os, random, discord, aiohttp, inspect

from discord.ext import commands
from dotenv import load_dotenv
from funcs import Funcs

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')


class SnotBot(commands.Bot):

    def __init__(self):
        super().__init__(command_prefix="!", intents=discord.Intents.all())
        self.session = None


    async def on_connect(self):
        self.session = aiohttp.ClientSession(loop=self.loop)
        await self.add_cog(Funcs(self))

        

#twitter needs to send me something first before anything happens here

if __name__ == '__main__':
    SnotBot().run(TOKEN)
