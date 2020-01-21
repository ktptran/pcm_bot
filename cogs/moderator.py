import discord
from discord.ext import commands
from discord.utils import get

class moderator(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Commands for moderators are loaded')

    @commands.command()
    @commands.has_permissions(manage_channels=True, manage_message=True)
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.mention}')

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'Kicked {member.mention}')

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')
        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member.name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.name}#{user.discriminator}')
                return

    @commands.command(pass_content=True)
    @commands.has_permissions(change_nickname=True)
    async def chg_nickname(self, ctx, name, chg_name):
        await ctx.change_nickname(ctx.message.author, nickname)
        role = get(ctx.message.server.roles, name=chg_name)  # Replace ARMA_ROLE as appropriate
        if role:  # If get could find the role
            await client.add_role(ctx.message.author, role)

    @commands.command(pass_context=True)
    @commands.has_permissions(change_nickname=True)
    async def chg_nickname(ctx, member: discord.Member, nick):
        await member.edit(nick=nick)
        await ctx.send(f'Nickname was changed for {member.mention} ')

def setup(client):
    client.add_cog(moderator(client))