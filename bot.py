import os
import discord
from dotenv import load_dotenv

#  a6256877-c8a2-4946-943a-ede987488d68
#  valorant.gg token


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
SERVER = os.getenv('DISCORD_SERVER')



client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == SERVER:
            break

    print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id:{guild.id})')

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Server Members:\n - {members}')

client.run(TOKEN)

