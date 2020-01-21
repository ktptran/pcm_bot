import discord
from discord.ext import commands, tasks
import random

# TODO: Questions into text file
test_channel = 546445725622468638  # bot_spam of PCM discord
test_channel2 = 664186132233322517  # general on Test server
gen_channel = 514612185578602532  # general of PCM discord
questions1 = [
    'What’s the best thing you’ve got going on in your life at the moment?',
    'What scene in a movie always gives you goosebumps every time you watch it?',
    'What incredibly common thing have you never done?',
    'What topic could you give a 20-minute presentation on without any preparation?',
    'What are some of your favorite games to play?',
    'What takes a lot of time but is totally worth it?',
    'What is the most amazing fact you know?',
    'What website or app doesn’t exist, but you really wish it did?',
    'What’s your favorite type of day? (weather, temp, etc.)',
    'What is the most clever or funniest use of advertising you’ve seen?',
    'How into self-improvement are you?',
    'Are you more productive at night or in the morning? Do you think it’s possible to change and get used to another schedule?']


class questions(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.post_msg.start(client)

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Commands for questions are now loaded.')

    @commands.command()
    async def unload_post(self, ctx):
        self.post_msg.cancel()
        await ctx.send('You have stopped the scheduled posting of the random question.')

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def load_post(self, ctx):
        self.post_msg.start(ctx)
        await ctx.send('You have started the scheduled posting of the random question.')


    @commands.command(aliases=['8ball', 'test'])
    @commands.has_permissions(manage_messages=True)
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
            size = len(questions1)
            questions1.append(arg)
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
        size = len(questions1)
        await ctx.send(f'There are {size} questions.')

    @commands.command(aliases=['list'])
    async def write_out(self, ctx):
        output = '**These are all the icebreaker questions we currently have:** \n'
        for i in range(len(questions1)):
            output += f'{i}. {questions1[i]}\n'
        await ctx.send(output)

    @commands.command()
    async def rand_quest(self, ctx):
        quest = random.choice(questions1)
        index = questions1.index(quest)
        await ctx.send(f'Question #{index}: {quest}')

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def remove(self, ctx, quest: int):
        if quest < 0:
            await ctx.send('**Error:**Number must be an integer greater than or equal to 0.')
        else:
            statement = questions1.pop(quest)
            await ctx.send(f'You have removed question #{quest}: \"{statement}\"')

    @commands.command()
    async def question(self, ctx, quest: int):
        if quest < 0:
            await ctx.send('**Error:** Number must be an integer greater than or equal to 0.')
        else:
            await ctx.send(f'Question #{quest}: {questions1[quest]}')

    @question.error
    @remove.error
    async def question_error(self, ctx, error):
        length = len(questions1) - 1
        if isinstance(error, commands.BadArgument) or isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'**Error:** You must enter in a numeric value from 0-{length}')
        elif isinstance(error, commands.indexError):
            await ctx.send(f'**Error:** You chose a non-existent question. Choose something within 0-{length}.')
        else:
            print(error)

    @tasks.loop(hours=24)
    async def post_msg(self, client):
        channel = client.get_channel(test_channel)
        await channel.send(f'Question of the day: {random.choice(questions1)}')
        print('Ran through loop')


def setup(client):
    client.add_cog(questions(client))