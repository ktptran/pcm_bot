import discord
from discord.ext import commands


class GameLinks(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Tells the user that the bot is ready
    @commands.Cog.listener()
    async def on_ready(self):
        print('Commands for in game links are now loaded.')

    # Prints out the op.gg or lolchess link for the inputted user or team.
    # Inputs required:
    #   gm = game mode (either TFT or SR)
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


def setup(client):
    client.add_cog(GameLinks(client))
