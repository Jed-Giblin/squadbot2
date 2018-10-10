import discord
import asyncio
import squadbot

client = discord.Client()

squad_rules = []


# The use of @client.event here passes it as an argument to the next defitiion
@client.event
@asyncio.coroutine
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----')


@client.event
@asyncio.coroutine
def on_message(message):
    if message.author.name == 'Sterence':
        squadbot.andrews_loop(client, message)

    if message.content.startswith('!squad'):
        yield from client.send_message(message.channel, 'Too soon executus...')


client.run('')

