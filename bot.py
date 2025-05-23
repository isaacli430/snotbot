import os, random, discord, aiohttp, inspect, json

from discord.ext import commands
from dotenv import load_dotenv
from funcs import Funcs

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')


class SnotBot(commands.Bot):

    def __init__(self):
        super().__init__(command_prefix="!", intents=discord.Intents.all())
        self.session = None
        
        with open("data.json") as f:
            self.counter_data = json.load(f)


    async def on_connect(self):
        self.session = aiohttp.ClientSession(loop=self.loop)
        await self.add_cog(Funcs(self))

    async def on_message(self, message):
        if message.author.id in self.counter_data["antho_id"]:
            count = sum([message.content.count(variation) for variation in self.counter_data["variations"]])

            if count > 0:
                self.counter_data["counter"] += count
                with open("data.json", "w") as f:
                    f.write(json.dumps(self.counter_data, indent=4))


                await message.channel.send(f"Antho has dropped the word {self.counter_data['counter']} times.")

        if message.channel.id in self.counter_data["allowed_channels"]:
            await self.process_commands(message)
        
	@bot.event
	async def on_ready():
		bot.summoners = {}
		bot.summoners_data = {}

		try:
			with open("data.json", "r") as f:
				bot.summoners_data = json.load(f)

			for username, data in bot.summoners_data.items():
				summoner = Summoner(data["unencrypted_username"], data["tagline"])
				bot.summoners[username] = summoner

			print(f"Loaded {len(bot.summoners)} summoners.")
		except FileNotFoundError:
			print("No leaderboard file found. Starting fresh.")

if __name__ == '__main__':
    SnotBot().run(TOKEN)
