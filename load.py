import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = '%')

TOKEN = 'NjY0MTg2NDI1MTYzMzgyNzg0.XhUdNQ.4u8QvaiM5aJ_slZvRPfmF4GNE50'


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


@load.error
async def load_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send(f'**Error:** This cog is already loaded.')


@unload.error
async def unload_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send(f'**Error:** This cog is not loaded.')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(TOKEN)