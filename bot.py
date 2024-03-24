import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True 

cow_count = 20

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

@bot.command()
async def greet(ctx, name: str):
    await ctx.send(f"Hello, {name}!")

@bot.command()
@commands.is_owner()
async def shutdown(ctx):
    await ctx.send(f"Ok, I'm shutting down!")
    await bot.close()

@bot.command()
async def itsworking(ctx):
    print("command itsworking has been called")
    await ctx.send("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZG43bmR1cWx0cWFja3c3a25pZ2s3cDE2NHRjejJ3b3R4cXNxMnF4bSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/CuMiNoTRz2bYc/giphy.gif")

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

@bot.event
async def on_message(message):
    global cow_count

    if 'cow' in message.content.lower() and message.author != bot.user:
        cow_mentions = message.content.lower().count('cow')

        cow_count += 5 * cow_mentions

        response = f'prommie has eaten {cow_count} cows'
        await message.channel.send(response)

    await bot.process_commands(message)

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot.run('MTE4NTU3NDgxNDYxNDgyMjkzMw.G_-fKT.OL1lb17kjeVzdO-A86Vx3CQCWCPoi19GrvsDUM')