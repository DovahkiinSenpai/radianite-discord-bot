#pylint: disable=line-too-long, missing-module-docstring, missing-final-newline
#import 
from pdb import Restart
from userids import *
from lists import *
import random
import time
from datetime import datetime
from timeit import repeat
import discord
import subprocess 
from secretinfo import token
from discord.ext import commands, tasks
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix="r!")

client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Doin' Your Mom/r!help"))
    print('Welcome user. Bot logged in as {0.user}'.format(client))
    
    # Setting `Playing ` status (activity=discord.Game(name="a game"))

    # Setting `Streaming ` status (activity=discord.Streaming(name="My Stream", url=my_twitch_url))
   
    # Setting `Listening ` status (activity=discord.Activity(type=discord.ActivityType.listening, name="Doin' Your Mom"))
    
    # Setting `Watching ` status (activity=discord.Activity(type=discord.ActivityType.watching, name="a movie"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('r!radhelp'):
        await message.channel.send('radhelp = rad help\nspin = SPIIIIIIIIN\nhomo = whos a homo\nheheheha = heheheha\nping = lol')

    if message.content.startswith('r!spin'):
        await message.channel.send('https://media.discordapp.net/attachments/837207335453458432/910689528073826305/3dgifmaker04128.gif')

    if message.content.startswith('r!heheheha'):
        await message.channel.send('https://tenor.com/view/clash-royale-clash-royale-emote-gif-23858585')

    if message.content.startswith('r!ping'):
        await message.channel.send('ping balls')

    if message.content.startswith('r!homo'):
        await message.channel.send(f"{random.choice(homos)} is a homo")

    if message.content.startswith('r!deletetest'):
            msg = await message.channel.send(f"{message.author.mention},’:)")
            time.sleep(2)
            Restart
            await msg.delete()
         
    if message.author.id == me: #killswitch
        if message.content.startswith('r!killswitch'):
            await message.channel.send(random.choice(exits))
            await message.channel.send('https://cdn.discordapp.com/attachments/836674086348128278/942350630406721546/dcja6sq-200ea72c-19d4-4d32-b858-bebf193aa17a.gif')
            exit()

    #Replies to when certain members speak 
    if message.author.id == ethan: 
        if random.randint(1,100) < 3:
            msg = await message.channel.send(f"{message.author.mention},’:) https://tenor.com/view/troll-trolled-trollge-troll-success-gif-22597471")
            time.sleep(4)
            await msg.delete()
            datetime.now(tz=None)
            dateTimeObj = datetime.now() 
            print("ratio'd ethan at", dateTimeObj.hour, ':', dateTimeObj.minute, ':', dateTimeObj.second)
            repeat

    if message.author.id == zach: 
        if random.randint(1,100) < 3:
            await message.channel.send(random.choice(gatos))
            datetime.now(tz=None)
            dateTimeObj = datetime.now() 
            print("gato'd zach at", dateTimeObj.hour, ':', dateTimeObj.minute, ':', dateTimeObj.second)
            repeat

    if message.author.id == rae:
        if random.randint(1,30) < 2:
            await message.channel.send(random.choice(loves))
            print('<3 messaged da gf at', dateTimeObj.hour, ':', dateTimeObj.minute, ':', dateTimeObj.second)
            repeat

client.run(token)