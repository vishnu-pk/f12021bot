# -*- coding: utf-8 -*-
"""
"""

# bot.py
import os
import random
import nest_asyncio
nest_asyncio.apply()

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
print(TOKEN)
print(GUILD)

client = discord.Client()


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    f = open('standings.txt', 'r')

    content = f.read()

    f.close()
    
    standings = content
    leader = 'Championship Leader:' + str(content[30:41])

    if message.content == 'leader':
        response = leader
        await message.channel.send(response)
    
    if message.content == 'standings':
        response = standings
        await message.channel.send(response)
    
    if 'spa' in message.content.lower():
        response = 'Abhishek DJ is the king of spa'
        await message.channel.send(response)
        
    if 'austria' in message.content.lower():
        response = 'Stealth is the Stealth of Austria'
        await message.channel.send(response)
        
    if 'silverstone' in message.content.lower():
        response = 'Shut UP! Addy Desh owns Silverstone'
        await message.channel.send(response)

    if 'spin' in message.content.lower():
        response = 'SBinnala master Lightingbud'
        await message.channel.send(response)
        
    if 'sbinnala' in message.content.lower():
        response = 'SBinnala master Lightingbud'
    await message.channel.send(response)



        
client.run(TOKEN)
client.run(TOKEN)
