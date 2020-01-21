import discord, random, asyncio
from datetime import datetime
from discord.ext import commands, tasks


client = commands.Bot(command_prefix='%')
TOKEN = ''
questions = [
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

send_time = '11:54' # time is in 24hr format
test_channel = 546445725622468638  # bot_spam of PCM discord
test_channel2 = 664186132233322517 # general on Test server
gen_channel = 514612185578602532  # general of PCM discord


async def time_check():
    await client.wait_until_ready()
    channel = client.get_channel(test_channel)
    print()
    while not client.is_closed:
        now = datetime.strftime(datetime.now(),'%H:%M')
        if now == send_time:
            message = random.choice(questions)
            await channel.send(f'Question of the day: {message}')
            time = 90
        else:
            time = 1
        await asyncio.sleep(time)

@client.event
async def on_ready():
    # with open('questions.txt') as f:
    #     content = f.read().splitlines()
    #     questions.append(content)
    # print(questions)
    # post_msg.start()
    print('Bot is online.')

# OP.GG portion
# Moved
@client.command()
@commands.has_permissions(manage_messages=True)
async def add(ctx, *, arg):
    if arg.endswith('?') and arg[0].isupper():
        size = len(questions)
        questions.append(arg)
        await ctx.send(f'The question, \"{arg}\" has been added as index {size}.')
    else:
        await ctx.send("**Error:** You must write a question. It must start with a capital letter end with a \'?\'")

# Moved
@client.command(aliases=['8ball', 'test'])
async def _8ball(ctx, *, question):
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

# Moved
@_8ball.error
@add.error
async def add_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('**Error:** You must enter in a question.')

# Moved
@client.command()
async def quest_amnt(ctx):
    size = len(questions)
    await ctx.send(f'There are {size} questions.')


@client.command(aliases=['list'])
async def write_out(ctx):
    output = '**These are all the icebreaker questions we currently have:** \n'
    for i in range(len(questions)):
        output += f'{i}. {questions[i]}\n'
    await ctx.send(output)


@client.command()
async def rand_quest(ctx):
    quest = random.choice(questions)
    index = questions.index(quest)
    await ctx.send(f'Question #{index}: {quest}')


@client.command()
@commands.has_permissions(manage_messages=True)
async def remove(ctx, quest: int):
    if quest < 0:
        await ctx.send('**Error:**Number must be an integer greater than or equal to 0.')
    else:
        statement = questions.pop(quest)
        await ctx.send(f'You have removed question #{quest}: \"{statement}\"')


@client.command()
async def question(ctx, quest: int):
    if quest < 0:
        await ctx.send('**Error:** Number must be an integer greater than or equal to 0.')
    else:
        await ctx.send(f'Question #{quest}: {questions[quest]}')


@question.error
@remove.error
async def question_error(ctx, error):
    length = len(questions) - 1
    if isinstance(error, commands.BadArgument) or isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'**Error:** You must enter in a numeric value from 0-{length}')
    elif isinstance(error, commands.indexError):
        await ctx.send(f'**Error:** You chose a non-existent question. Choose something within 0-{length}.')
    else:
        print(error)


# Lolchess command - moved
@client.command()
async def lolchess(ctx, args):
    link = 'https://lolchess.gg/profile/na/'
    link += args
    await ctx.send(f'**Lolchess:** {link}')


# OPGG portion of bot - moved
@client.command()
async def opgg(ctx, *, args):
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
# Moved
async def user_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'**Error:** Enter in at least one summoner name')

@client.command()
async def info(ctx):
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
    description = ['Staff Application Form: ', 'TFT tryouts: January 17 @8pm', 'Community tryouts: January 18-19 @8pm',
                   'Workshop Registration January 13 4:30-6:00 PM']
    for i in range(len(forms)):
        message += f'{i}. **{description[i]}** - <{forms[i]}>\n'
    await ctx.send(message)

# Moved
@client.command()
async def climb(ctx):
    helpful = ['https://u.gg/', 'https://champion.gg/', 'https://probuilds.net/', 'https://Leagueoflegends.com/', 'https://lolking.net/',
               'https://lolnexus.com/', 'https://proguides.com']
    links = 'Helpful links for you to climb!\n0. <'
    for i in range(len(helpful)):
        links += helpful[i] + f'>\n {i + 1}. <'
    links = links[:-5]
    await ctx.send(links)

# Append out for later
@tasks.loop(hours=24)
async def post_msg():
    channel = client.get_channel(gen_channel)
    await channel.send(f'Question of the day: {random.choice(questions)}')


@post_msg.before_loop
async def before():
    await client.wait_until_ready()
    print("Finished waiting")

# client.loop.create_task(time_check())
client.run(TOKEN)
