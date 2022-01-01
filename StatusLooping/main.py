import discord
from discord.ext import commands, tasks
from itertools import cycle

TOKEN = ''

# Prefix

client = commands.Bot(command_prefix='/')

# Status

status = cycle(['Hello', 'Hi'])


@tasks.loop(seconds=3)
async def change_status():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(next(status)))


@client.event
async def on_ready():
    change_status.start()
    print('Client is online.')


# Run

client.run(TOKEN)
