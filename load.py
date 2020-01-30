import discord
import youtube_dl
from discord.ext import commands
import os

client = commands.Bot(command_prefix='%')
client.remove_command('help')  # removes the help command

# Token for the bot
TOKEN = 'TOKEN'
welcome_channel = 542109074901303336
new_user_message = ["""
Welcome to University of Washington: Purple Caster Minions - League of Legends Discord! \n\n
This discord server is for University of Washington's PCM LoL club. Here you will find updates/posts on club events,
club socials, public tournaments, PCM in-house tournaments, streams by UW students, etc. \n\n
Your nickname on this server should be in the following format: IGN [ROLE (as in League of Legends main role)]. \n\n
If you have a [?] after your name or nothing at all, it means your preferred/main role is unknown. Please PM what it is
so I may change it. \nIf you have any questions, feel free to DM me. Thank you!
""", """ __Rules__\n
1. Please be respectful of everyone in this server at all times. This means no name calling, threatening, harassing, or
 otherwise belitttling anyone (in public chat or in PMs). There is no tolerance for flaming one another verbally or
 vocally. Teasing/friendly banter is acceptable, however if it reaches to the point where it is viewed as
 harassment by the party, it is then forbidden. Don't intentionally provoke other users to anger them.
2. Intolerance of anyone's age, race, sexual orientation, religious preferences, financial status, ethnicity, gender
 identity, or personal choices is not acceptable. \n
3. Cursing and otherwise derogatory language is allowed. Please be considerate of to what words you choose using
the rules above as a guideline. If someone asks you to refrain from using a word, please oblige. \n
4. SFW and any NSFW picture or sexual allusions is not allowed. \n
5. This is not a server for finding a lover. Don't flirt with other members in the server or PM them
like you're on a love-finding app. \n
6. Don't be bringing the atmosphere down. If the game isn't going your way, don't take it out on your team members.
The point of this is to have fun and meet other people that play the game in our community. Don't be the one that
ruins the community. \n
7. Posting pictures and videos are allowed, but please post them in the relative text channel. \n
8. Please refrain from spamming in the text channels. If such events do occur, the right to post
media will be removed. \n
9. Don't mass tag people for no reason. Tagging is for summoning people or making them understand you're
talking specifically to them.""", """
10. Be welcoming to new members. They are apart of the community we are in. We all play the same game that we enjoy.\n
11. When posting media, please do not use URL shorteners for your safety. Will be removed if found. \n
12. No spamming, no unapproved advertisements. If found, they will be deleted.\n

__Tips on how to avoid spam:__\n
You can mute an entire server and suppress everyone/here pings in notification settings.
You can also mute text channels individually by clicking the bell icon in the channel you want to mute.  \n\n

We recommend picking up roles in #role_pickup because we do not allow the general members to use the everyone/here
pings. You will only be pinged for the roles you pick up. Enjoy!
"""]


# TODO: Potentially combine these two as they are short methods that do the same thing
# Loads a cog that has not been loaded into the program. Requires the command to be issued by an admin.
# Inputs:
#   ctx = the command issued
#   extension = the name of the cog file to unload/load
@client.command()
@commands.has_permissions(administrator=True)
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'The {extension} file has been loaded.')


# Unloads a cog that has been loaded into the program. Requires the command to be issued by an admin.
# Inputs:
#   ctx = the command issued
#   extension = the name of the cog file to unload
@client.command()
@commands.has_permissions(administrator=True)
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'The {extension} file has been unloaded.')


# Prints out a custom help function to describe the functions of this program within the
# channel the command was issued.
# Inputs:
#   ctx = the command issued
@client.command()
async def help(ctx):
    # author = ctx.message.author used for messaging back information
    embed = discord.Embed(
        colour=discord.Colour.orange()
    )
    # TODO: Add in how to change it with permissions
    embed.set_author(name='Help')
    embed.add_field(name='Administrator', value='__Load:__ Loads in a file [%load <file_name>]\n'
                    '__unload:__ Unloads a file [%unload <file_name>]\n', inline=False)
    embed.add_field(name='Moderator', value='__add:__ Adds a statement into a file [%add <file_name> <file_input>]\n'
                    '__unban/ban:__ (Un)bans a user from the server [%(un)ban <discord_member> <reason>] \n'
                    '__chg_nickname:__ Changes the user\'s nickname [%chg_nickname <discord_member> <nickname>\n'
                    '__kick:__ Kicks a person from the server [%kick <discord_member> <reason>]\n'
                    '__remove:__ Removes a statement from a file [%remove <file_name> <remove_index>\n'
                    '__setup_post:__ Controls the loop for posting daily messages [%setup_post <start/stop>\n',
                    inline=False)
    embed.add_field(name='Members', value='__8ball:__ Responds to a yes or no question [%8ball <question>]\n'
                    '__quest_amount:__ Returns the amount of questions [%quest_amount]\n'
                    '__rand_quest:__ Returns a random question to the channel you are in [%rand_quest]\n'
                    '__write_out:__ Writes out all of the information for that file [%write_out <file_name>\n'
                    '__lol_info__: Returns the op.gg/lolchess for summoner(s) [%lol_info <sr/tft> <summoner name(s)'
                    , inline=False)
    await ctx.send(embed=embed)


# @client.event
# async def on_member_join(member):
#
#
#    await channel.send(f'{message}')
#    roles = discord.utils.get(member.guild.roles, name='Newcomer')
#    await member.add_roles(roles)


# When the loads a cog that is already loaded, it sends an error to indicate
# that the cog has already been loaded.
# Inputs:
#   ctx = the command issued
#   error = the type of error that came from the command
@load.error
async def load_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send(f'**Error:** This cog is already loaded.')
    # TODO: What happens when you have a file that is not within the directory?


# When the user unloads a cog that is not loaded, this function is called
# to indicate why the command did not work.
# Inputs:
#   ctx = the command issued
#   error = the type of error that came from the command
@unload.error
async def unload_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send(f'**Error:** This cog is not loaded.')


# When the user issues a command that is not within the bot, it sends
# an error to indicate they made a wrong command.
# Inputs:
#   ctx = the command issued
#   error = the type of error that came from the command
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f'**Error:** This command does not exist.')

# When a new member joins a discord server, we will print a welcome message
# to the user that outlines the rules of the server in addition to prompting
# them for new roles
# @client.event
# async def on_member_join(member):
    # Get the welcome channel
#    channel = client.get_channel(int(welcome_channel))
    # Send out message to channel, @ the member
#    await channel.send(f'Welcome {member}!\n')
#    for msg in new_user_message:
#        await channel.send(msg)

# TODO: Work on giving roles
# giving members a role
# to do this the bot must have 'Manage Roles' permission on server, and role to add must be lower than bot's top role
#    role = discord.utils.get(member.server.roles, name="name-of-your-role")
#    await client.add_roles(member, role)
#    print("Added role '" + role.name + "' to " + member.name)


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(TOKEN)
