import discord
import os, sys
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True 

cow_count = 20

bot = commands.Bot(command_prefix='!', intents=intents)

fantomland_general_id = 1151188965412589662

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    channel = bot.get_channel(1151188965412589662)
    await channel.send("Hey, cuties, i'm alive again!")

@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message):
        await message.channel.send('Hey, ', bot.user)

@bot.command()
async def greet(ctx, name: str):
    await ctx.send(f"Hello, {name}!")

@bot.command()
@commands.is_owner()
async def shutdown(ctx):
    await ctx.send(f"Ok, I'm shutting down!")
    await bot.close()

@bot.command()
async def padoru(ctx):
    print("command itsworking has been called")
    await ctx.send("https://tenor.com/view/meme-padoru-christmas-joke-anime-gif-16368098")

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

def restart_bot(): 
  os.execv(sys.executable, ['python'] + sys.argv)

@bot.command(name= 'restart')
async def restart(ctx):
  await ctx.send("Restarting bot...")
  restart_bot()

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