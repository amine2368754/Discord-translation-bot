import discord
from tr_func import *

client = discord.Client(intents=discord.Intents.default())
TOKEN = 'your token here'

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$help'):
        text=""
        await message.channel.send(text)
    elif message.content.startswith(''):
        my_string = message.content
        print(my_string)
        translated = translateText(my_string)
        print(translated)# Le modèle de traduction pour traduire la phrase
        await message.channel.send(translated)
client.run(TOKEN)
