import random
import discord
from discord.ext import commands

responses = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."]


class QuestionsInfo(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Commands for questions with file are now loaded.')

    # Responds with a 8ball response to a question
    # Inputs required:
    #   question = must include an uppercase letter at the beginning in addition to a question mark at the end
    @commands.command(aliases=['8ball'])
    @commands.has_permissions(manage_messages=True)
    async def _8ball(self, ctx, *, question):
        if question.endswith('?') and question[0].isupper():
            await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')
        else:
            await ctx.send("**Error:** You must write a question. It must start with a capital letter end with a \'?\'")

    # Error for 8ball or add function when the question field is not inputted.
    # This then returns a message to the user entering in the command about what they need to put in
    @_8ball.error
    async def _8ball_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('**Error:** You must write a question after the command. '
                           'It must start with a capital letter end with a \'?\'')
        else:
            await ctx.send(f'The error was {error}')

    # Returns the amount of questions stored.
    @commands.command()
    async def quest_amount(self, ctx):
        with open('./cogs/questions.txt', 'r') as f:
            line_count = len(f.readlines())
        await ctx.send(f'There are {line_count} questions.')

    '''Move to Questions'''
    # Writes out all of the questions for the user to see.
    @commands.command(aliases=['list'])
    async def write_out(self, ctx, file_name):
        line_count = 0
        if file_name == 'questions':
            output = '**These are all the questions we currently have:** \n'
            with open(f'./cogs/{file_name}.txt') as f:
                for line in f:
                    output += f'{line_count}. {line}'
                    line_count += 1
                    if len(output) > 1600:
                        await ctx.send(output)
                        output = ''
        elif file_name == 'climb':
            output = 'Helpful links for you to climb!\n'
            with open(f'./cogs/{file_name}.txt') as f:
                for line in f:
                    output += f'{line_count}. <{line[:-1]}> \n'
                    line_count += 1
                    if len(output) > 1600:
                        await ctx.send(output)
                        output = ''
        elif file_name == 'info':
            output = '__Important documents containing information for Purple Caster Minions__\n'
            output += '**Staff Directory:** '
            output += '<https://docs.google.com/spreadsheets' \
                      '/d/1EhH3J2nYdfTkcHt_XtjIQNyEdHEtbdO6tzuAzZmJjr4/edit#gid=0>\n'
            output += '**Constitution:** https://drive.google.com/open?id=1s0VgKplFK-xuKGrZ-EFNZa7w0eig9opi\n'
            output += '**Calendar:** <https://docs.google.com/spreadsheets/u/2/d/1'
            output += 'e01nUzNl4weYyYL0Y_7CNCg0AwSoKoB_ShnOTzZN9ZI/edit?usp=drive_web&ouid=105285472884501025990>\n\n'
            output += '__Social Media__:\n'
            output += '**Facebook Page:** <https://facebook.com/lolpcm>\n'
            output += '**Facebook Group:** <http://facebook.com/groups/lolpcm>\n'
            output += '**Instagram Page:** <https://www.instagram.com/lolpcm>\n'
            output += '**Twitter Page:** <https://www.twitter.com/lolpcm> \n'
            output += '**Twitch Channel:** <https://wwww.twitch.tv/lolpcm> \n'
            output += '**Discord Link:** <https://discord.gg/lolpcm>\n\n'
            output += '__Forms:__\n'
            with open(f'./cogs/{file_name}.txt') as f:
                for line in f:
                    line_count += 1
                    if line_count % 2 == 0:  # even
                        output += f'{line[:-1]}>\n'
                    else:
                        output += f'{int((line_count + 1) / 2)}. ** {line[:-1]}** - '
        else:
            output = 'Please enter either questions/climb/info after the command %write_out.'
        await ctx.send(output)

    # Returns a specific question from the list of questions
    # Inputs:
    #   quest = index of question the user wants to get
    @commands.command()
    async def question(self, ctx, quest: int):
        with open('./cogs/questions.txt', 'r') as f:
            lines = f.readlines()
        if quest < 0 or quest >= len(lines):
            await ctx.send(f'**Error:** Number must be an integer less than {len(lines)} but greater than zero.')
        else:
            await ctx.send(f'Question #{quest}: {lines[quest]}')

    # Errors for putting in the wrong argument for the question function.
    # Errors:
    #   BadArgument = when the value inputted is not an integer
    #   MissingRequiredArgument = not enough values inputted
    #   indexError = choosing an index that does not exist within the text file
    @question.error
    async def question_error(self, ctx, error):
        with open('./cogs/questions.txt', 'r') as f:
            lines = f.readlines()
        length = len(lines) - 1
        if isinstance(error, commands.BadArgument) or isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'**Error:** You must enter in a numeric value from 0-{length}')
        elif isinstance(error, commands.indexError):
            await ctx.send(f'**Error:** You chose a non-existent question. Choose something within 0-{length}.')
        else:
            print(error)

    # Chooses a random question for the user to receive.
    @commands.command()
    async def rand_quest(self, ctx):
        lines = open('./cogs/questions.txt').read().splitlines()
        quest = random.choice(lines)
        index = lines.index(quest)
        await ctx.send(f'Question #{index}: {quest}')


def setup(client):
    client.add_cog(QuestionsInfo(client))