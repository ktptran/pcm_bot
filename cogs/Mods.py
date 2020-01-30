import discord
import random
from discord.ext import commands, tasks
from discord.utils import get

gen_channel = 514612185578602532  # general of PCM discord


class Mods(commands.Cog):
    def __init__(self, client):
        self.client = client
        # self.post_msg.start()

    # When the cog is fully functioning, it runs this method.
    @commands.Cog.listener()
    async def on_ready(self):
        print('Commands for moderators are loaded')

    # Stops the loop for posting the daily message
    @commands.command()
    async def setup_post(self, ctx, start):
        if start == 'start':
            self.post_msg.start()
            await ctx.send('You have started the scheduled posting of the random question.')
        elif start == 'stop':
            self.post_msg.cancel()
            await ctx.send('You have stopped the scheduled posting of the random question.')
        else:
            await ctx.send('You must input either start or stop after the command.')

    # Adds a question to the list of questions
    # Inputs required:
    #   question = must include an uppercase letter at the beginning in addition to a question mark at the end
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def add(self, ctx, file_name, *, file_input):
        if file_name == 'climb':
            if file_input.startswith('https://'):
                file_obj = open(f'./cogs/{file_name}.txt', 'a')
                file_obj.write(f'{file_input}\n')
                file_obj.close()
                await ctx.send(f'Inputted link: <{file_input}>.')
            else:
                await ctx.send('**Error:** You did not input a link.')
        elif file_name == 'forms':
            if file_input.startswith('https://') and '|' in file_input:
                split_input = file_input.split(' | ')
                file_obj = open(f'./cogs/{file_name}.txt', 'a')
                file_obj.write(f'{split_input[1]}\n')
                file_obj.write(f'{split_input[0]}\n')
                file_obj.close()
                await ctx.send('Inputted form and description')
            else:
                await ctx.send(
                    '**Error:** You did not input a form followed by \' | \' to separate the description.')
        elif file_name == 'questions':
            if file_input.endswith('?') and file_input[0].isupper():
                within = False
                with open('./cogs/questions.txt') as file:
                    if any(line[:-1] == file_input for line in file):
                        within = True
                        await ctx.send('This question is already in the database.')
                if not within:
                    file_obj = open('./cogs/questions.txt', 'a')
                    file_obj.write(f'{file_input}\n')
                    file_obj.close()
                    with open('./cogs/questions.txt', 'r') as f:
                        lines = f.readlines()
                    count = len(lines)
                    await ctx.send(f'Added statement as #{count - 1}: {file_input}')
            else:
                await ctx.send("**Error:** You must write a question. "
                               "It must start with a capital letter end with a \'?\'")
        else:
            await ctx.send('You must enter either of these three options:\n'
                           '**file_name = climb** : %add climb <any_climbing_link>\n'
                           '**file_name = questions** : %add questions <question with capital and ?>\n'
                           '**file_name = forms** : %add forms <form_link> | <description>')

    # Error for 8ball or add function when the question field is not inputted.
    # This then returns a message to the user entering in the command about what they need to put in
    @add.error
    async def add_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('You must enter either of these three options:\n'
                           '**file_name = climb** : %add climb <any_climbing_link>\n'
                           '**file_name = questions** : %add questions <question with capital and ?>\n'
                           '**file_name = forms** : %add forms <form_link> | <description>')

    # Removes a specific index from the questions
    # Inputs:
    #   quest = index of question you want to remove
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def remove(self, ctx, file_name, remove_index: int):
        if file_name == 'questions' or file_name == 'climb':
            with open(f'./cogs/{file_name}.txt') as f:
                lines = f.readlines()
            if remove_index < 0 or len(lines) <= remove_index:
                await ctx.send(f'**Error:** Number must be an integer less than {len(lines)} but greater than zero.')
            else:
                with open(f'./cogs/{file_name}.txt', 'w') as f:
                    statement = ''
                    count = 0
                    for line in lines:
                        if count != remove_index:
                            f.write(line)
                        else:
                            statement = f'You have removed question #{count}: \"{line[:-1]}\"'
                        count += 1
        elif file_name == 'forms':
            with open(f'./cogs/{file_name}.txt') as f:
                lines = f.readlines()
            if remove_index < 0 or len(lines) / 2 <= remove_index:
                await ctx.send(f'**Error:** Number must be an integer '
                               f'less than {int(len(lines) / 2)} but greater than zero.')
            elif file_name == 'forms':
                with open(f'./cogs/{file_name}.txt', 'w') as f:
                    statement = ''
                    count = 0
                    for line in range(0, len(lines), 2):
                        if count != remove_index:
                            f.write(lines[line])
                            f.write(lines[line + 1])
                        else:
                            statement = f'You have removed question ' \
                                        f'#{count}: \"{lines[line][:-1]} - <{lines[line + 1]}>'
                        count += 1
            else:
                statement = 'The file_name you inputted does not match the files in the directory.'
        await ctx.send(statement)

    # Errors for putting in the wrong argument for the remove function.
    # Errors:
    #   BadArgument = when the value inputted is not an integer
    #   MissingRequiredArgument = not enough values inputted
    #   indexError = choosing an index that does not exist within the text file
    @remove.error
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

    # Prints out a question every 24 hours from when it was initialized.
    @tasks.loop(hours=24)
    async def post_msg(self):
        client = self.client
        channel = client.get_channel(int(gen_channel))
        lines = open('./cogs/questions.txt').read().splitlines()
        quest = random.choice(lines)
        await channel.send(f'Question of the day: {quest}')
        print('Ran through loop')

    # Clearing a channel of messages. This requires that the user must have
    # both the manage_channels and manage_message rights in the discord server.
    # Inputs:
    #   amount = the default amount is 5 messages, but any amount can be entered.
    @commands.command()
    @commands.has_permissions(manage_channels=True, manage_message=True)
    async def clear(self, ctx, amount=5):
        if amount <= 0:
            await ctx.send('You must enter a value greater than zero.')
        else:
            await ctx.channel.purge(limit=amount)

    # Banning a user from the server. The user must have the ban_members property.
    # Inputs:
    #   member = discord member identification
    #   Reason = defaulted to none, but puts in audit and states why the ban occurred
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.mention}')

    # Kicking a user from the server. The user must have the kick_members property.
    #   member = discord member identification
    #   Reason = defaulted to none, but puts in audit and states why the kick occurred
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'Kicked {member.mention}')

    # Unbanning a user from the server. The user must have the ban_members property.
    # Inputs:
    #   member = discord member identification
    #   Reason = defaulted to none, but puts in audit and states why the ban occurred
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

    # TODO: Revise this function
    # Changing a user's nickname on the server. The user must have the change_nickname property.
    # Inputs:
    #   member = discord member identification
    #   chg_name = nickname you want to change the user's identification on the server.
    @commands.command(pass_content=True)
    @commands.has_permissions(change_nickname=True)
    async def chg_nickname(self, ctx, member: discord.member, chg_name):
        await ctx.change_nickname(ctx.message.author, chg_name)
        role = get(ctx.message.server.roles, name=chg_name)  # Replace ARMA_ROLE as appropriate
        if role:  # If get could find the role
            await ctx.add_role(ctx.message.author, role)


def setup(client):
    client.add_cog(Mods(client))
