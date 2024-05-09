import discord
import os, sys, re
import time, datetime
import psutil
import json
from discord.ext import commands
from mcstatus import JavaServer
from ezgiphy import GiphyPublicAPI

intents = discord.Intents.default()
intents.message_content = True 

bot = commands.Bot(command_prefix='!', intents=intents)

fantomland_general_id = 1151188965412589662
fantomland_server_ip = "ready-motors.joinmc.link"

f = open("cow_count.txt", "r")
cow_count = int(f.read())
f.close()

f = open("cat_count.txt", "r")
cat_count = int(f.read())
f.close()

def get_now_time():
    return datetime.datetime.now()

def get_who_called(ctx, function_name):
    print(ctx.author.name, f"called {function_name} at", get_now_time())

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    #channel = bot.get_channel(1151188965412589662)
    #await channel.send("Hey, cuties, i'm alive again!")
    #this feature is annoying when you restart the bot alot
    await bot.change_presence(activity=discord.Game(name="Minecraft"))

@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message):
        await message.channel.send('Hey, ', bot.user)

@bot.command(name="github")
async def github(ctx):
    get_who_called(ctx, "github")
    await ctx.send("You can review my code here: https://github.com/rdPrommie/cosmicBot")

@bot.command()
async def greet(ctx, name: str):
    get_who_called(ctx, "greet")
    await ctx.send(f"Hello, {name}!")

@bot.command()
@commands.is_owner()
async def shutdown(ctx):
    get_who_called(ctx, "shutdown")
    await ctx.send(f"Ok, I'm shutting down!")
    await bot.close()

@bot.command()
async def padoru(ctx):
    get_who_called(ctx, "padoru")
    await ctx.send("https://tenor.com/view/meme-padoru-christmas-joke-anime-gif-16368098")

@bot.command()
async def ping(ctx):
    get_who_called(ctx, "ping")
    await ctx.send("pong")

def restart_bot():
    os.execv(sys.executable, ['python'] + sys.argv)

@bot.command(name= 'restart')
async def restart(ctx):
    get_who_called(ctx, "restart")
    await ctx.send("Restarting bot...")   
    restart_bot()

def check_process(process_name):
    return process_name in (p.name() for p in psutil.process_iter())

@bot.command(name='check_server')
async def check_server(ctx):
    get_who_called(ctx, "check_server")
    await ctx.send("Checking Fantomland server...")
    server = JavaServer.lookup(fantomland_server_ip)
    try:
        status = server.status()
        await ctx.send("The server has {0} players and replied in {1} ms".format(status.players.online, status.latency))
    except TimeoutError:
        await ctx.send("Tunnel is dead. Either use !s-restart or tag Prommie.")
    
@bot.command(name='server_ping')
async def server_ping(ctx):
    get_who_called(ctx, "server_ping")
    server = JavaServer.lookup(fantomland_server_ip)
    await ctx.send("The server replied in {0} ms".format(server.ping()))

@bot.command(name="s-restart")
async def restart_server(ctx):
    get_who_called(ctx, "s-restart")
    if check_process("java.exe"):
        await ctx.send("Restarting server. Please wait.")
        os.system('taskkill /f /im java.exe')
        os.startfile("C:\\Users\\Mozigépész\\Desktop\\run.lnk")
        await ctx.send("Server is starting... Please wait 60 seconds.")
        time.sleep(60)
        server = JavaServer.lookup(fantomland_server_ip)
        await ctx.send("Server is up! Ping: {0}".format(server.status.latency))
    else:
        await ctx.send("I can't restart server. Please tag Prommie.")

@bot.command(name="runki")
async def runki(ctx):
    get_who_called(ctx, "runki")
    await ctx.send("https://tenor.com/view/reee-pepe-frog-angry-angery-gif-18421495")

@bot.command(name="runkai")
async def runkai(ctx):
    get_who_called(ctx, "runkai")
    await ctx.send("https://tenor.com/view/luntry-gif-26563186")

@bot.command(name="prommie")
async def prommie(ctx):
    get_who_called(ctx, "prommie")
    await ctx.send("https://tenor.com/view/peepofat-gif-24867194")

@bot.command(name="fantom")
async def fantom(ctx):
    get_who_called(ctx, "fantom")
    await ctx.send("https://tenor.com/view/blue-cat-giga-chad-giga-cat-blue-cat-gif-26520616")

@bot.command(name="elf")
async def elf(ctx):
    get_who_called(ctx, "elf")
    await ctx.send("https://cdn.discordapp.com/attachments/1151188965412589662/1234971172266053692/rita-rossweisse-rita.gif?ex=6632ac08&is=66315a88&hm=a5104958b5676bb731887e410a3d2ec9490e89e6db8fac932aa3a621dc662c1f&")

@bot.command(name="pimo")
async def pimo(ctx):
    get_who_called(ctx, "pimo")
    await ctx.send("https://tenor.com/view/controlmypc-cat-screaming-discord-gif-20582295")

@bot.command(name="job")
async def pimo(ctx):
    get_who_called(ctx, "job")
    await ctx.send("https://tenor.com/view/im-afraid-the-time-has-come-for-you-to-get-a-job-al-bundy-married-with-children-go-find-some-work-you-need-to-get-a-job-gif-23009203")

@bot.command(name="cherry")
async def cherry(ctx):
    get_who_called(ctx, "cherry")
    await ctx.send("https://tenor.com/view/peepo-peepoleave-gif-20075315")

@bot.command(name="cres")
async def cres(ctx):
    get_who_called(ctx, "cres")
    await ctx.send("https://tenor.com/view/saltobears-gif-19924022")
    
@bot.command(name="ban")
async def ban(ctx):
    await ctx.send(f"{ctx.author.mention}https://tenor.com/view/bongocat-banhammer-ban-hammer-bongo-gif-18219363")

@bot.command(name="whos_playing")
async def whos_playing(ctx):
    get_who_called(ctx, "who_playing")
    await ctx.send("Checking who is playing right now...")
    server = JavaServer.lookup(fantomland_server_ip)
    if not server.query().players.names == "":
        await ctx.send("The server has the following players online: {0}".format(", ".join(server.query().players.names)))
    else:
        await ctx.send("Noone is playing right now.")

@bot.command(name="cat")
async def cat(ctx):
    get_who_called(ctx, "cat")
    await ctx.send("CAAAAAATS!")
    giphy = GiphyPublicAPI('K4qD7QbTgPBKvAtmJ4h9zOd4UzrjWvt6')
    response = json.loads(giphy.random(tag='cat',rating='g')).get("data")
    await ctx.send(response["url"])

@bot.event
async def on_message(message):
    global cat_count
    global cow_count

    if 'cat' in message.content.lower() and str(message.author.id) == "567731558153453570" and re.search(r'\bcat\b', message.content.lower()) and message.author != bot.user:
        cat_mentions = message.content.lower().count('cat')
        
        cat_count += 1 * cat_mentions
        

        response = f'pimo has mentioned cats {cat_count} times so far'
        await message.channel.send(response)

        f = open("cat_count.txt", "w")
        f.write(str(cat_count))
        f.close()

    

    if 'cow' in message.content.lower() and message.author != bot.user and re.search(r'\bcow\b', message.content.lower()):
        cow_mentions = message.content.lower().count('cow')

        cow_count += 1 * cow_mentions
        

        response = f'prommie has eaten {cow_count} cows and counting'
        await message.channel.send(response)

    
        f = open("cow_count.txt", "w")
        f.write(str(cow_count))
        f.close()

    await bot.process_commands(message)

# I'm storing the bot token :)
bot.run(token = open('token.txt', 'r').read())
