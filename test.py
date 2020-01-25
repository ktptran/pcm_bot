import random

# Situation 2:
# Before starting -->
# From text file (initially):
# What’s the best thing you’ve got going on in your life at the moment?
# What scene in a movie always gives you goosebumps every time you watch it?
# What incredibly common thing have you never done?
#
# During -->
# Always get questions from list and append
#
# Ending -->
# Nothing needed, just shutdown bot
#
# Overall should go with situation 2, so instead of implementing the functions through a list,
# we should do through a text file.
def read():
    with open('cogs/questions.txt', 'r') as f:
        data = f.readlines()
        print(data)


# @commands.command()
# async def add(self, ctx, *, arg):
def add(arg):
    if arg.endswith('?') and arg[0].isupper():
        file_obj = open('cogs/questions.txt', 'a')
        file_obj.write(f'{arg}\n')
        file_obj.close()
        count = 0
        with open('cogs/questions.txt', 'r') as f:
            f.readlines()
            count += 1
        print(f'Added statement as #{count}: {arg}')
    else:
        print("**Error:** You must write a question. It must start with a capital letter end with a \'?\'")


# @commands.command()
# async def quest_amnt(self, ctx):
def quest_amnt():
    with open('cogs/questions.txt') as f:
        line_count = 0
        for line in f:
            line_count += 1
        print(f'There are {line_count} questions.')


# @commands.command(aliases=['list'])
# async def write_out(self, ctx):
def write_out():
    with open('cogs/questions.txt') as f:
        output = '**These are all the icebreaker questions we currently have:** \n'
        line_count = 0
        for line in f:
            output += f'{line_count}. {line}\n'
            line_count += 1
        print(output)


# @commands.command()
# async def rand_quest(self, ctx):
def rand_quest(ctx):
    lines = open('cogs/questions.txt').read().splitlines()
    quest = random.choice(lines)
    index = lines.index(quest)
    print(f'Question #{index}: {quest}')


def remove(quest: int):
    with open('cogs/questions.txt', 'r') as f:
        lines = f.readlines()
    if quest < 0:
        print('**Error:**Number must be an integer greater than or equal to 0.')
    else:
        statement = ''


        # This then writes it down and takes out the specific count number we need to take out
        with open('cogs/questions.txt', 'w') as f:
            for line in lines:
                count = 0
                if count != val:
                    f.write(line)
                else:
                    statement
        await ctx.send

# @commands.command()
#     @commands.has_permissions(manage_messages=True)
#     async def remove(self, ctx, quest: int):
#         if quest < 0:
#             await ctx.send('**Error:**Number must be an integer greater than or equal to 0.')
#         else:
#             statement = questions1.pop(quest)
#             await ctx.send(f'You have removed question #{quest}: \"{statement}\"')


def question(quest: int):
    if quest < 0:
        print('**Error:** Number must be an integer greater than or equal to 0.')
    else:
        count = 0
        with open('cogs/questions.txt', 'r') as f:
            lines = f.readlines()
            if count  == quest:
                print(f'Question #{count}: {lines[count]}')
            count += 1

# @commands.command()
#     async def question(self, ctx, quest: int):
#         if quest < 0:
#             await ctx.send('**Error:** Number must be an integer greater than or equal to 0.')
#         else:
#             await ctx.send(f'Question #{quest}: {questions1[quest]}')


add('This is a question?')



