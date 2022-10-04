import discord
from discord.ext import commands
import os
from mcstatus import JavaServer

intent = discord.Intents.default()
bot = commands.Bot(command_prefix=".", intents=intent)

@bot.event
async def on_ready():
    print('Bot info:')
    print('----------------------------------------------------')
    print(f'Bot name: {bot.user.name}')
    print(f'Bot id: {bot.user.id}')
    print(f'Bot version: {discord.__version__}')
    print('Bot is ready')
    print('----------------------------------------------------')

@bot.command()
async def lookup(ctx):
    #get message content and look up the server and remove .lookup from the message
    server = JavaServer.lookup(ctx.message.content[8:])
    status = server.status()
    await ctx.send(f"{ctx.message.content[8:]} has {status.players.online} players  online \nthe server replied in {status.latency} ms")

bot.run("Put token here")