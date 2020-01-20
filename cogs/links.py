import discord
from discord.ext import commands

class links(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online.')

    # Lolchess command
    @commands.command()
    async def lolchess(self, ctx, args):
        link = 'https://lolchess.gg/profile/na/'
        link += args
        await ctx.send(f'**Lolchess:** {link}')

    # OPGG portion of bot
    @commands.command()
    async def opgg(self, ctx, *, args):
        link = 'https://na.op.gg/summoner/userName='
        if args == 'PCM_Varsity_Team':
            link = link + 'pascho%2CPlasticHoipolloi%2Ctachibanakanade%2Cmanabird%2Cdarquesse%2Cnattyp%2Chexsise%2Coshawatt%2Ctrendy%2Cyilililili\n'
            link = link + '**Team 1:** <https://na.op.gg/multi/query=oshawatt%2Chexsise%2Cdarquesse%2Ctrendy%2Cyilililili>\n'
            link = link + '**Team 2:** <https://na.op.gg/multi/query=pascho%2Cplastichoipolloi%2Ctachibanakanade%2Cmanabird%2Cnattyp>'
        elif "," in args:
            ign = args.split(', ')
            for i in range(len(ign)):
                ign[i] = ign[i].replace(' ', '_')
                link += ign[i] + '%2C'
            link = link[:-3]
        else:
            args = args.replace(' ', '_')
            link = link + args
        await ctx.send(f'**OP.GG:** {link}')

    @lolchess.error
    @opgg.error
    async def user_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'**Error:** Enter in at least one summoner name')

    @commands.command()
    # TODO: Load in forms and be able to add in
    async def info(self, ctx):
        message = '__Important documents containing information for Purple Caster Minions__\n'
        message += '**Staff Directory:** '
        message += '<https://docs.google.com/spreadsheets/d/1EhH3J2nYdfTkcHt_XtjIQNyEdHEtbdO6tzuAzZmJjr4/edit#gid=0>\n'
        message += '**Constitution:** https://drive.google.com/open?id=1s0VgKplFK-xuKGrZ-EFNZa7w0eig9opi\n'
        message += '**Calendar:** <https://docs.google.com/spreadsheets/u/2/d/1'
        message += 'e01nUzNl4weYyYL0Y_7CNCg0AwSoKoB_ShnOTzZN9ZI/edit?usp=drive_web&ouid=105285472884501025990>\n\n'
        message += '__Social Media__:\n'
        message += '**Facebook Page:** <https://facebook.com/lolpcm>\n'
        message += '**Facebook Group:** <http://facebook.com/groups/lolpcm>\n'
        message += '**Instagram Page:** <https://www.instagram.com/lolpcm>\n'
        message += '**Twitter Page:** <https://www.twitter.com/lolpcm> \n'
        message += '**Twitch Channel:** <https://wwww.twitch.tv/lolpcm> \n'
        message += '**Discord Link:** <https://discord.gg/lolpcm>\n\n'
        message += '__Forms:__\n'
        forms = ['https://forms.gle/tEt1LZdSYqGqteQE9', 'https://forms.gle/23ocUKYLvRc5tzQQ9',
                 'https://forms.gle/RvCtt2xSomXiqQdw5', 'https://forms.gle/yjzjdf6oogJEZuSR7']
        description = ['Staff Application Form: ', 'TFT tryouts: January 17 @8pm',
                       'Community tryouts: January 18-19 @8pm',
                       'Workshop Registration January 13 4:30-6:00 PM']
        for i in range(len(forms)):
            message += f'{i}. **{description[i]}** - <{forms[i]}>\n'
        await ctx.send(message)

    @commands.command()
    async def climb(self, ctx):
        helpful = ['https://u.gg/', 'https://champion.gg/', 'https://probuilds.net/', 'https://Leagueoflegends.com/',
                   'https://lolking.net/',
                   'https://lolnexus.com/', 'https://proguides.com']
        links = 'Helpful links for you to climb!\n0. <'
        for i in range(len(helpful)):
            links += helpful[i] + f'>\n {i + 1}. <'
        links = links[:-5]
        await ctx.send(links)


def setup(client):
    client.add_cog(links(client))