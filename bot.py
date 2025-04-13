import os, random, discord, aiohttp, inspect

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')


class SnotBot(commands.Bot):

    def __init__(self):
        super().__init__(command_prefix="!", intents=discord.Intents.all())
        self._last_result = None
        self.session = None


    async def on_connect(self):
        self.session = aiohttp.ClientSession(loop=self.loop)

        for name, func in inspect.getmembers(self):
            if isinstance(func, commands.Command):
                self.add_command(func)


    @commands.command()
    async def cyrus(self):
        await self.send('Alan')

    @commands.command()
    async def dain(self, ctx):
        await ctx.send('Darsh')

    @commands.command()
    async def darshify(self, ctx):
        try:
            words = message.content.split()
            del words[0]
            alans = ['jak', 'cel', 'braham', 'vit']
            for i in range(len(words)):
                if words[i][-1]:
                    pass
                else:
                    words[i] = words[i] + alans[random.randint(0,3)]

            await ctx.send(' '.join(words))

        except discord.errors.HTTPException:

            third = len(words) // 3
            first_part = words[:third]
            second_part = words[third: third * 2]
            third_part = words[third * 2:]

            await ctx.send(' '.join(first_part))
            await ctx.send(' '.join(second_part))
            await ctx.send(' '.join(third_part))
        

#twitter needs to send me something first before anything happens here

SnotBot().run(TOKEN)
