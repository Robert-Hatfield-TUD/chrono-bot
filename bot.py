import os
import discord
from dotenv import load_dotenv
from discord.ext import commands


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
SERVER = os.getenv('DISCORD_SERVER')


client = discord.Client()
client = commands.Bot(command_prefix="!")

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
    
@client.event
async def on_message(message):
	# Hello?
	if message.content == "hello":
		# Fuck you
		await message.channel.send("Go fuck yourself Adam")

	# IMPORTANT IT BREAK WITHOUT
	await client.process_commands(message)
    
@client.command(
	help="Uses come crazy logic to determine if pong is actually the correct value or not.",
	brief="Prints pong back to the channel."
)

async def ping(ctx):
	await ctx.channel.send("pong")


@client.command(
	help="Looks like you need some help.",
	brief="Prints the list of values back to the channel."
)

async def print(ctx, *args):
	response = ""

	for arg in args:
		response = response + " " + arg

	await ctx.channel.send(response)

client.run(TOKEN)
