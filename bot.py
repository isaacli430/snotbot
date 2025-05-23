import os, random, discord, aiohttp, inspect, json

from discord.ext import commands
from dotenv import load_dotenv
from funcs import Funcs
from getranks import Summoner

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')


class SnotBot(commands.Bot):

    def __init__(self):
        super().__init__(command_prefix="!", intents=discord.Intents.all())
        self.session = None
        
        with open("data.json") as f:
            self.data = json.load(f)

        self.summoners = {}

        for username, value in self.data["summoners"].items():
			summoner = Summoner(value["unencrypted_username"], value["tagline"])
			self.summoners[username] = summoner


    async def on_connect(self):
        self.session = aiohttp.ClientSession(loop=self.loop)
        await self.add_cog(Funcs(self))

    async def on_message(self, message):
        if message.author.id in self.data["antho_id"]:
            count = sum([message.content.count(variation) for variation in self.data["variations"]])

            if count > 0:
                self.data["counter"] += count
                with open("data.json", "w") as f:
                    f.write(json.dumps(self.data, indent=4))


                await message.channel.send(f"Antho has dropped the word {self.data['counter']} times.")

        if message.channel.id in self.data["allowed_channels"]:
            await self.process_commands(message)
        
		

if __name__ == '__main__':
    SnotBot().run(TOKEN)
