import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('!cyrus'):
        await message.channel.send('Alan')
    
    if message.content.startswith('!dain'):
        await message.channel.send('Darsh')

    if message.content.startswith('!kill'):
        await message.channel.send('Quitjak')
        quit()

    if message.content.startswith('!darshify'):
        try:
            words = message.content.split()
            del words[0]
            alans = ['jak', 'cel', 'braham', 'vit']
            for i in range(len(words)):
                if words[i][-1]:
                    pass
                else:
                    words[i] = words[i] + alans[random.randint(0,3)]

            await message.channel.send(' '.join(words))

        except discord.errors.HTTPException:

            third = len(words) // 3
            first_part = words[:third]
            second_part = words[third: third * 2]
            third_part = words[third * 2:]

            await message.channel.send(' '.join(first_part))
            await message.channel.send(' '.join(second_part))
            await message.channel.send(' '.join(third_part))

#twitter needs to send me something first before anything happens here

client.run(TOKEN)
