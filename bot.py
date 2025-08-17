import discord
import os, sys, re
import time, datetime
import psutil
import json
import platform, subprocess
from discord.ext import commands
from mcstatus import JavaServer
from ezgiphy import GiphyPublicAPI

intents = discord.Intents.default()
intents.message_content = True 

bot = commands.Bot(command_prefix='!', intents=intents)

fantomland_general_id = 1151188965412589662
fantomland_server_ip = "ready-motors.joinmc.link" # OUTDATED SERVER ADDRESS

with open('counters.json', 'r') as file:
    counter_data = json.load(file)
    cow_count = counter_data["counters"]["cow"]
    cat_count = counter_data["counters"]["cat"]
    bored_count = counter_data["counters"]["bored"]
    sigh_count = counter_data["counters"]["sigh"]

def ping_server(host):
    # returns True is host responds to a ping request
    # please make sure if the host name is valid smh
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', host]

    return subprocess.call(command) == 0

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
    await bot.change_presence(activity=discord.Game(name="Path of Exile"))

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
    await ctx.send("The Minecraft server has been shut down indefinetly. Idk when we are going to set it up again. Sorry.")

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

@bot.command(name="cherryfast")
async def cherryfast(ctx):
    get_who_called(ctx, "cherryfast")
    await ctx.send("https://tenor.com/by9Zs.gif")

@bot.command(name="cres")
async def cres(ctx):
    get_who_called(ctx, "cres")
    await ctx.send("https://tenor.com/view/saltobears-gif-19924022")
    
@bot.command(name="dust")
async def dust(ctx):
    get_who_called(ctx, "dust")
    await ctx.send("https://tenor.com/view/peachvitty-gif-24343442")

@bot.command(name="gay")
async def gay(ctx):
    get_who_called(ctx, "gay")
    await ctx.send("https://media1.tenor.com/images/bd0db1b5fe2cf233439a0758c5b12186/tenor.gif?itemid=12334071")

@bot.command(name="retard")
async def retard(ctx):
    get_who_called(ctx, "retard")
    await ctx.send("https://media.tenor.com/-OoOt1G8q-AAAAAC/gordo-no.gif")


@bot.command(name="pengy")
async def pengy(ctx):
    get_who_called(ctx, "pengy")
    await ctx.send("https://tenor.com/view/charge-penguin-highway-gif-21457682")
    
@bot.command(name="ban")
async def ban(ctx):
    await ctx.send(f"{ctx.author.mention}https://tenor.com/view/bongocat-banhammer-ban-hammer-bongo-gif-18219363")

@bot.command(name="whos_playing")
async def whos_playing(ctx):
    get_who_called(ctx, "who_playing")
    if ping_server(fantomland_server_ip):
        await ctx.send("Checking who is playing right now...")
        server = JavaServer.lookup(fantomland_server_ip)
        if not server.query().players.names == "":
            await ctx.send("The server has the following players online: {0}".format(", ".join(server.query().players.names)))
        else:
            await ctx.send("Noone is playing right now.")
    else:
        await ctx.send("No Minecraft server is running at the moment.")
    

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
    global bored_count
    global sigh_count
    
    
    #pimo cat counter
    if 'cat' in message.content.lower() and str(message.author.id) == "567731558153453570" and re.search(r'\bcat\b', message.content.lower()) and message.author != bot.user:
        cat_mentions = message.content.lower().count('cat')
        
        cat_count += 1 * cat_mentions
        

        response = f'pimo has mentioned cats {cat_count} times so far'
        await message.channel.send(response)

        counter_data['counters']['cat'] = cat_count
        
    
    #pengy bored counter
    if 'bored' in message.content.lower() and str(message.author.id) == "338630349087309826" and re.search(r'\bbored\b', message.content.lower()) and message.author != bot.user:
        bored_mentions = message.content.lower().count('bo+red')
        
        bored_count += 1 * bored_mentions
        
        response = f'Pengy has been bored {bored_count} times so far'
        await message.channel.send(response)

        counter_data['counters']['bored'] = bored_count
    
    #cres sigh counter
    if 'sigh' in message.content.lower() and str(message.author.id) == "420597874812780555" and re.search(r'\bsi+gh\b', message.content.lower()) and message.author != bot.user:
        sigh_mentions = message.content.lower().count('si+gh')
        
        sigh_count += 1 * sigh_mentions

        response = f'Cres has sighed {sigh_count} times so far'
        await message.channel.send(response)

        counter_data['counters']['sigh'] = sigh_count
        
    # prommie 173108969118760962
    # cres 420597874812780555
          
    #prommie is a cow counter
    if 'cow' in message.content.lower() and message.author != bot.user and re.search(r'\bc+ow\b', message.content.lower()):
        cow_mentions = message.content.lower().count('cow')

        cow_count += 1 * cow_mentions
        

        response = f'prommie has eaten {cow_count} cows and counting'
        await message.channel.send(response)

    
        counter_data['counters']['cow'] = cow_count

    with open('counters.json', 'w') as file:
        json.dump(counter_data, file)

    await bot.process_commands(message)

# I'm storing the bot token :)
bot.run(token = open('token.txt', 'r').read())
