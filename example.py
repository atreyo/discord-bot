import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        print(client.user)
        print(message.author)
        await message.channel.send('hello back!')

    if message.content.startswith('e ai'):
        print(client.user)
        print(message.author)
        await message.channel.send('oooopa!')

client.run(os.getenv('DISCORD_BOT_TOKEN'))
