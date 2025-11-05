
import discord
from discord.ext import commands
import os
import sys
import psutil

def restart_bot():
    os.execv(sys.executable, ['python'] + sys.argv)

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="github")
    async def github(self, ctx):
        await ctx.send("You can review my code here: https://github.com/rdPrommie/cosmicBot")

    @commands.command()
    async def greet(self, ctx, name: str):
        await ctx.send(f"Hello, {name}!")

    @commands.command()
    @commands.is_owner()
    async def shutdown(self, ctx):
        await ctx.send(f"Ok, I'm shutting down!")
        await self.bot.close()

    @commands.command()
    async def padoru(self, ctx):
        await ctx.send("https://tenor.com/view/meme-padoru-christmas-joke-anime-gif-16368098")

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("pong")

    @commands.command(name= 'restart')
    async def restart(self, ctx):
        await ctx.send("Restarting bot...")   
        restart_bot()

    @commands.command(name='check_server')
    async def check_server(self, ctx):
        await ctx.send("The Minecraft server has been shut down indefinetly. Idk when we are going to set it up again. Sorry.")

async def setup(bot):
    await bot.add_cog(General(bot))
