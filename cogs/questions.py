import discord
from discord.ext import commands, tasks
import random


class questions(commands.Cog):
    def __init__(self, client):
        self.client = client
        test_channel = 546445725622468638  # bot_spam of PCM discord
        test_channel2 = 664186132233322517  # general on Test server
        gen_channel = 514612185578602532  # general of PCM discord

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        self.post_msg.start()
        print('Bot is now running loop.')

    @commands.command(aliases=['8ball', 'test'])
    async def _8ball(self, ctx, *, question):
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
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def add(self, ctx, *, arg):
        if arg.endswith('?') and arg[0].isupper():
            size = len(questions)
            questions.append(arg)
            await ctx.send(f'The question, \"{arg}\" has been added as index {size}.')
        else:
            await ctx.send("**Error:** You must write a question. It must start with a capital letter end with a \'?\'")

    @_8ball.error
    @add.error
    async def add_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('**Error:** You must enter in a question.')

    @commands.command()
    async def quest_amnt(self, ctx):
        size = len(questions)
        await ctx.send(f'There are {size} questions.')

    @commands.command(aliases=['list'])
    async def write_out(self, ctx):
        output = '**These are all the icebreaker questions we currently have:** \n'
        for i in range(len(questions)):
            output += f'{i}. {questions[i]}\n'
        await ctx.send(output)

    @commands.command()
    async def rand_quest(self, ctx):
        quest = random.choice(questions)
        index = questions.index(quest)
        await ctx.send(f'Question #{index}: {quest}')

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def remove(self, ctx, quest: int):
        if quest < 0:
            await ctx.send('**Error:**Number must be an integer greater than or equal to 0.')
        else:
            statement = questions.pop(quest)
            await ctx.send(f'You have removed question #{quest}: \"{statement}\"')

    @commands.command()
    async def question(self, ctx, quest: int):
        if quest < 0:
            await ctx.send('**Error:** Number must be an integer greater than or equal to 0.')
        else:
            await ctx.send(f'Question #{quest}: {questions[quest]}')

    @question.error
    @remove.error
    async def question_error(self, ctx, error):
        length = len(questions) - 1
        if isinstance(error, commands.BadArgument) or isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'**Error:** You must enter in a numeric value from 0-{length}')
        elif isinstance(error, commands.indexError):
            await ctx.send(f'**Error:** You chose a non-existent question. Choose something within 0-{length}.')
        else:
            print(error)

    # TODO: Make this work
    @tasks.loop(hours=24)
    async def post_msg(self, test_channel):
        channel = commands.get_channel(test_channel)
        await channel.send(f'Question of the day: {random.choice(questions)}')


def setup(client):
    client.add_cog(questions(client))