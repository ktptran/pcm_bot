import discord
from discord.ext import commands

# Finished this one
helpful = ['https://u.gg/', 'https://champion.gg/',
           'https://probuilds.net/', 'https://Leagueoflegends.com/',
           'https://lolking.net/', 'https://lolnexus.com/', 'https://proguides.com']
forms = ['https://forms.gle/tEt1LZdSYqGqteQE9', 'https://forms.gle/23ocUKYLvRc5tzQQ9',
        'https://forms.gle/RvCtt2xSomXiqQdw5', 'https://forms.gle/yjzjdf6oogJEZuSR7']
descriptions = ['Staff Application Form: ', 'TFT tryouts: January 17 @8pm',
                       'Community tryouts: January 18-19 @8pm',
                       'Workshop Registration January 13 4:30-6:00 PM']


class Links(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Commands for when the cog is loaded.
    @commands.Cog.listener()
    async def on_ready(self):
        print('Commands for links are now loaded.')

    # Prints out the op.gg or lolchess link for the inputted user or team.
    # Inputs required:
    #   gm = gamemode (either TFT or SR)
    #   args = arguments inputted for summoner names
    @commands.command()
    async def lol_info(self, ctx, gm, *, args):
        if gm.lower() == 'sr':
            if args == 'PCM_Teams':
                link = '\n**PCM Teams:**\n__Varsity Team__\n*Full Team:* https://na.op.gg/summoner/userName='
                link = link + 'pascho%2CPlasticHoipolloi%2Ctachibanakanade%2Cmanabird%2Cdarquesse%2Cnattyp%2Chexsise%2'
                link = link + 'Coshawatt%2Ctrendy%2Cyilililili\n*Team 1:* <https://na.op.gg/multi/query=oshawatt%'
                link = link + '2Chexsise%2Cdarquesse%2Ctrendy%2Cyilililili>\n*Team 2:* <https://na.op.gg/multi/'
                link = link + 'query=pascho%2Cplastichoipolloi%2Ctachibanakanade%2Cmanabird%2Cnattyp>\n\n'
                link = link + '__Cloud Team__\n<https://na.op.gg/multi/query=n%C3%B8timportant%2Cbungy%2Cwiggywonka%'
                link = link + '2Cmighty93%2Cchetgeezus%2Clostpath>'
            elif "," in args:
                link = 'https://na.op.gg/summoner/userName='
                ign = args.split(', ')
                for i in range(len(ign)):
                    ign[i] = ign[i].replace(' ', '_')
                    link += ign[i] + '%2C'
                link = link[:-3]
            else:
                link = 'https://na.op.gg/summoner/userName='
                args = args.replace(' ', '_')
                link = link + args
            await ctx.send(f'**OP.GG:** {link}')
        elif gm.lower() == 'tft':
            link = 'https://lolchess.gg/profile/na/'
            link += args
            print('Should send link')
            await ctx.send(f'**Lolchess:** {link}')
        else:
            await ctx.send('You must enter \'%lol_info {tft/sr} {player name(s)}\'')

    # Errors for when there is a missing required argument.
    # Errors:
    #   MissingRequiredArgument = not enough inputs entered
    @lol_info.error
    async def user_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'**Error:** Enter in at least one summoner name')

    # Finished moving
    # Prints out info about the club and other important documents for the members.
    @commands.command()
    async def info(self, ctx):
        # This part is stagnant and always stays consistent.
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
        for i in range(len(forms)):
            message += f'{i}. **{descriptions[i]}** - <{forms[i]}>\n'
        await ctx.send(message)


    # Completed added to QuestFile
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def add_link(self, ctx, form, *, description):
        if form.startswith('https://'):
            forms.append(form)
            descriptions.append(description)
            await ctx.send('Inputted form and description.')
        else:
            await ctx.send('**Error:** You did not input a link followed by a description. Please try again.')

    # TODO: Combine this with the remove function in QuestFile.py
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def remove_link(self, ctx, link: int):
        if link < 0:
            await ctx.send('**Error:**Number must be an integer greater than or equal to 0.')
        else:
            statement = forms.pop(link)
            description = descriptions.pop(link)
            await ctx.send(f'You have removed question {statement}: \"{description}\"')

    @remove_link.error
    @add_link.error
    async def link_error(self, ctx, error):
        length = len(descriptions) - 1
        if isinstance(error, commands.BadArgument) or isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'**Error:** You must enter in a numeric value from 0-{length}')
        elif isinstance(error, commands.indexError):
            await ctx.send(f'**Error:** You chose a non-existent question. Choose something within 0-{length}.')
        else:
            print(error)

    # Finished
    # Prints out helpful links for League analytics to help with game knowledge.
    @commands.command()
    async def climb(self, ctx):
        links1 = 'Helpful links for you to climb!\n0. <'
        for i in range(len(helpful)):
            links1 += helpful[i] + f'>\n {i + 1}. <'
        links1 = links1[:-5]
        await ctx.send(links1)

    # Finished added to QuestFile
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def climb_add(self, ctx, *, arg):
        if arg.endswith('/') and arg.beginswith('https://'):
            helpful.append(arg)
            await ctx.send(f'We have added your link: {arg}')
        else:
            await ctx.send(f'We could not add in your link because it does not start with \'https://\' and end with /.')


def setup(client):
    client.add_cog(Links(client))