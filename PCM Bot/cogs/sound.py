import discord
from discord.ext import commands
import youtube_dl
# Download FFmpeg, youtube_dl

players = {}
queues = {}


class Sound(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Prints out the notification for when the bot is ready.
    @commands.Cog.listener()
    async def on_ready(self):
        print('Commands for audio bot are good')

    # When someone adds a reaction, it sends in that channel that the user has put an emoji
    # Inputs:
    #   reaction = the reaction the user removed
    #   user = the id of the user that removed the reaction
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        channel = reaction.message.channel
        await self.client.send_message(channel, '{} has added {} to the message: {}'.
                                       format(user.name, reaction.emoji, reaction.message.content))

    # When someone removes a reaction, it sends that the user has removed an emoji in that channel.
    # Inputs:
    #   reaction = the reaction the user removed
    #   user = the id of the user that removed the reaction
    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction, user):
        channel = reaction.message.channel
        await self.client.send_message(channel, '{} has removed {} to the message: {}'.
                                       format(user.name, reaction.emoji, reaction.message.content))

    # Makes the bot join a channel when called.
    # Inputs:
    #   ctx = information on the command called
    @commands.command(pass_context=True)
    async def join(self, ctx):
        # When someone joins a voice channel
        channel = ctx.message.author.voice.voice_channel
        await self.client.join_voice_channel(channel)

    # Makes the bot exit a channel when called.
    # Inputs:
    #   ctx = information on the command called
    @commands.command(pass_context=True)
    async def leave(self, ctx):
        server = ctx.message.server
        voice_client = self.client.voice_client_in(server)  # an instance of the bot being in a voice channel
        await voice_client.disconnect()

    # The bot plays music in the channel
    # Inputs:
    #   ctx = information on the command called
    #   url = Youtube url of the video the user wants to be played
    @commands.command(pass_context=True)
    async def play(self, ctx, url):
        server = ctx.message.server
        voice_client = self.client.voice_client_in(server)
        player = await voice_client.create_ytdl_player(url)
        players[server.id] = player
        player.start()

    # The bot pauses what it is playing.
    # Inputs:
    #   ctx = information on the command called
    @commands.command(pass_context=True)
    async def pause(self, ctx):
        pid = ctx.message.server.id
        players[pid].pause()

    # Stops the bot from playing the video.
    # Inputs:
    #   ctx = information on the command called
    @commands.command(pass_context=True)
    async def stop(self, ctx):
        pid = ctx.message.server.id
        players[pid].stop()

    # Resumes the video the bot is playing
    # Inputs:
    #   ctx = information on the command called
    @commands.command(pass_context=True)
    async def resume(self, ctx):
        pid = ctx.message.server.id
        players[pid].resume()

    # Queues up the next video for the bot to play following all of those in the queue.
    # Inputs:
    #   ctx = information on the command called
    #   url = Youtube url of the video the user wants to be queued
    @commands.command(pass_context=True)
    async def queue(self, ctx, url):
        server = ctx.message.server
        voice_client = self.client.voice_client_in(server)
        player = await voice_client.create_ytdl_player(url, after=lambda: self.check_queue(server.id))
        if server.id in queues:
            queues[server.id].append(player)
        else:
            queues[server.id] = [player]
        await self.client.say('Video queued.')

    # Checks the queue for next item to play
    def check_queue(pid):
        if queues[pid] != []:
            player = queues[pid].pop(0)
            players[pid] = player
            player.start()


def setup(client):
    client.add_cog(Sound(client))
