import discord
import os, sys
import psutil
import win32gui
from discord.ext import commands
<<<<<<< HEAD
from mcstatus import JavaServer

=======
import requests
>>>>>>> 9d897401a526fe77d3f11e6942898e340b80bb4c
intents = discord.Intents.default()
intents.message_content = True 

bot = commands.Bot(command_prefix='!', intents=intents)

fantomland_general_id = 1151188965412589662
fantomland_server_ip = "ready-motors.joinmc.link"

f = open("cow_count.txt", "r")
cow_count = int(f.read())
f.close()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    #channel = bot.get_channel(1151188965412589662)
    #await channel.send("Hey, cuties, i'm alive again!")
    await bot.change_presence(activity=discord.Game(name="world domination"))

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
    print("command padoru has been called")
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

def check_process(process_name):
    return process_name in (p.name() for p in psutil.process_iter())

@bot.command(name='check_server')
async def check_server(ctx):
    await ctx.send("Checking Fantomland server...")
    server = JavaServer.lookup("issues-experience.joinmc.link")
    status = server.status()
    await ctx.send("The server has {0} players and replied in {1} ms".format(status.players.online, status.latency))

@bot.command(name='server_ping')
async def server_ping(ctx):
    server = JavaServer.lookup("issues-experience.joinmc.link")
    await ctx.send("The server replied in {0} ms".format(server.ping()))

@bot.command(name="restart_server")
async def restart_server(ctx):
    if check_process("javaw.exe"):
        await ctx.send("Restarting server. Please wait.")
        pass
    else:
        await ctx.send("I can't restart server. Please tag Prommie.")

@bot.command(name="whos_playing")
async def whos_playing(ctx):
    await ctx.send("Checking who is playing right now...")
    server = JavaServer.lookup("issues-experience.joinmc.link")
    if not server.query().players.names == "":
        await ctx.send("The server has the following players online: {0}".format(", ".join(server.query().players.names)))
    else:
        await ctx.send("Noone is playing right now.")

@bot.event
async def on_message(message):
    global cow_count

    if 'cow' in message.content.lower() and message.author != bot.user:
        cow_mentions = message.content.lower().count('cow')

        cow_count += 1 * cow_mentions
        

        response = f'prommie has eaten {cow_count} cows'
        await message.channel.send(response)

    await bot.process_commands(message)
    f = open("cow_count.txt", "w")
    f.write(str(cow_count))
    f.close()

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot.run('MTE4NTU3NDgxNDYxNDgyMjkzMw.G_-fKT.OL1lb17kjeVzdO-A86Vx3CQCWCPoi19GrvsDUM')
