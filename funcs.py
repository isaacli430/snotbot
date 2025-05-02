import random
from discord.ext import commands

class Funcs(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="cyrus")
    async def _cyrus(self, ctx):
        await ctx.send('Alan')

    @commands.command(name="dain")
    async def _dain(self, ctx):
        await ctx.send('Darsh')

    @commands.command(name="darshify")
    async def _darshify(self, ctx):
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


    @commands.command(name="rolesmix")
    async def _rolesmix(self, ctx, *players):

        if len(players) > 5:
            return await ctx.send("You cannot have more than 5 players.")

        positions = ["Top", "Jungle", "Mid", "ADC", "Support"]

        players = list(players)

        while len(players) < 5:
            players.append(None)

        random.shuffle(players)

        out = []

        for i, player in enumerate(players):
            if player:
                out.append(f"{positions[i]}: {player}")

        await ctx.send("\n".join(out))


    @commands.command(name="playersmix")
    async def _playersmix(self, ctx, *players):

        if len(players) != 10:
            return await ctx.send("You need 10 players.")

        players = list(players)

        random.shuffle(players)

        team_1 = '\n'.join(players[:5])
        team_2 = '\n'.join(players[5:10])

        out = f"__**Team 1**__:\n{team_1}\n\n__**Team 2**__:\n{team_2}"

        await ctx.send(out)


    @commands.command(name="count")
    async def _count(self, ctx):

        await ctx.send(f"Antho has dropped the word {self.bot.counter_data['counter']} times.")