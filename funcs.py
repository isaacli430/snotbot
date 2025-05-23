import random
from discord.ext import commands
from getranks import Summoner

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

        positions = ["top:", "jungle:", "mid:", "adc:", "support:"]
        available_roles = [0, 1, 2, 3, 4]
        random.shuffle(available_roles)

        players = list(players)

        for i, player in enumerate(players):
            lower_player = player.lower()
            found = False
            for j, position in enumerate(positions):
                if lower_player.startswith(position):
                    if j not in available_roles:
                        return await ctx.send("You can only have one person per role.")

                    available_roles.remove(j)
                    players[i] = [player[len(position):], j]
                    found = True
                    break

            if not found:
                players[i] = [player, None]

        while len(players) < 5:
            players.append([None, None])

        for player in players:
            if player[1] == None:
                player[1] = available_roles[0]
                del available_roles[0]

        players.sort(key = lambda player: player[1])

        out = []

        for i, player in enumerate(players):
            if player[0]:
                out.append(f"{positions[i].upper()} {player[0]}")

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

        await ctx.send(f"Antho has dropped the word {self.bot.data['counter']} times.")


    @commands.command(name="addsummoner")
    async def _addsummoner(self, ctx, unencrypted_username, tagline):
        username_key = unencrypted_username.lower().strip()

        if username_key in self.bot.data["summoners"]:
            await ctx.send(f"{username_key} is already stored.")
            return

        try:
            summoner = Summoner(unencrypted_username, tagline)
            self.bot.summoners[username_key] = summoner

            self.bot.data["summoners"][username_key] = {
                "unencrypted_username": summoner.unencrypted_username,
                "tagline": summoner.tagline,
            }

            with open("data.json", "w") as f:
                f.write(json.dumps(self.bot.data, indent=4))

            await ctx.send(f"Stored: {summoner.unencrypted_username}")

        except Exception as e:
            await ctx.send(f"Error: {str(e)}")
