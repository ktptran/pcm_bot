import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = '%')

TOKEN = 'NjY0MTg2NDI1MTYzMzgyNzg0.XiYmkg.xqdTeqz_xWn4RsM7MAYCPjccVD4'

'''
Only administrators are able to program up new functions for the bot to
administrate the server.

Bot does not yet have permissions to do this on the server & will need to be readded later on.
'''


@client.command()
@commands.has_permissions(administrator=True)
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'The {extension} file has been loaded.')


@client.command()
@commands.has_permissions(administrator=True)
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'The {extension} file has been unloaded.')


@load.error
async def load_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send(f'**Error:** This cog is already loaded.')


@unload.error
async def unload_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send(f'**Error:** This cog is not loaded.')


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f'**Error:** This command does not exist.')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(TOKEN)