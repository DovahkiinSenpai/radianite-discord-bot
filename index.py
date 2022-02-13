#import 
from multiprocessing.connection import wait
from pdb import Restart
import random
import time
import string
from datetime import datetime
from timeit import repeat
import discord
import subprocess 
from secretinfo import token

datetime.now(tz=None)
# Returns a datetime object containing the local date and time
dateTimeObj = datetime.now()

#random lists
homos = ['zach', 'josh', 'kael', 'konnar', 'geezer', 'ethan', 'roo']
loves = ['hewwo cutie! - boyfriend', 'insert distracting but adorable message here', 'blep :3', 'i wuv uuuuuu', ':3', 'o3o', 'boop! *~*']
exits = ["Please don't leave, there's more demons to toast!", "Just leave. When you come back, I'll be waiting with a bat. ", "This is no exit message! Message intentionally left blank.", "I'LL FORMAT YOUR HARD-DRIVE IF YOU QUIT NOW"]

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

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
        await message.channel.send(random.choice(homos))

    #Replies to messages 
    if message.author.id == 244858366373920778: #ethan
        if random.randint(1,20) < 7:
            await message.channel.send(",':)")
            print('fucking owned ethan at', dateTimeObj.hour, ':', dateTimeObj.minute, ':', dateTimeObj.second)
            repeat

    if message.author.id == 591027923624919050: #Rae
        if random.randint(1,20) < 10:
            await message.channel.send(random.choice(loves))
            print('<3 messaged da gf at', dateTimeObj.hour, ':', dateTimeObj.minute, ':', dateTimeObj.second)
            repeat
    
    #killswitch        
    if message.author.id == 244858366373920778: #Me, of course
        if message.content.startswith('r!killswitch'):
            await message.channel.send(random.choice(exits))
            await message.channel.send('https://cdn.discordapp.com/attachments/836674086348128278/942350630406721546/dcja6sq-200ea72c-19d4-4d32-b858-bebf193aa17a.gif')
            exit()
    
    #restart
    if message.author.id == 244858366373920778: #Me, of course
        if message.content.startswith('r!restart'):
            await message.channel.send("Restarting the bot in 5 seconds, please wait...")
            await message.channel.send('https://i.gifer.com/SjyG.gif')
            print('Restarting the bot')
            time.sleep(5)
            Restart

client.run(token)