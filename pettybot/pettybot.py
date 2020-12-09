import os
import discord
from dotenv import load_dotenv
import beefs
from random import choice


load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "!halo":
        await message.channel.send(beefs.halo_beef())
    if message.content.startswith("!elon"):
        user = choice(message.channel.guild.members)
        await message.channel.send('%s thinks that Elon Musk is a genius' % user.mention)
    if message.content == "!twitch":
        await message.channel.send(beefs.twitch_beef())
client.run(token)


