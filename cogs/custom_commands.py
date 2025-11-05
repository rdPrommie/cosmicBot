
import discord
from discord.ext import commands

class Memes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="runki")
    async def runki(self, ctx):
        await ctx.send("https://tenor.com/view/reee-pepe-frog-angry-angery-gif-18421495")

    @commands.command(name="runkai")
    async def runkai(self, ctx):
        await ctx.send("https://tenor.com/view/luntry-gif-26563186")

    @commands.command(name="prommie")
    async def prommie(self, ctx):
        await ctx.send("https://tenor.com/view/peepofat-gif-24867194")

    @commands.command(name="fantom")
    async def fantom(self, ctx):
        await ctx.send("https://tenor.com/view/blue-cat-giga-chad-giga-cat-blue-cat-gif-26520616")

    @commands.command(name="elf")
    async def elf(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/1151188965412589662/1234971172266053692/rita-rossweisse-rita.gif?ex=6632ac08&is=66315a88&hm=a5104958b5676bb731887e410a3d2ec9490e89e6db8fac932aa3a621dc662c1f&")

    @commands.command(name="pimo")
    async def pimo(self, ctx):
        await ctx.send("https://tenor.com/view/controlmypc-cat-screaming-discord-gif-20582295")

    @commands.command(name="job")
    async def job(self, ctx):
        await ctx.send("https://tenor.com/view/im-afraid-the-time-has-come-for-you-to-get-a-job-al-bundy-married-with-children-go-find-some-work-you-need-to-get-a-job-gif-23009203")

    @commands.command(name="cherry")
    async def cherry(self, ctx):
        await ctx.send("https://tenor.com/view/peepo-peepoleave-gif-20075315")

    @commands.command(name="cherryfast")
    async def cherryfast(self, ctx):
        await ctx.send("https://tenor.com/by9Zs.gif")

    @commands.command(name="cres")
    async def cres(self, ctx):
        await ctx.send("https://tenor.com/view/saltobears-gif-19924022")
    
    @commands.command(name="dust")
    async def dust(self, ctx):
        await ctx.send("https://tenor.com/view/peachvitty-gif-24343442")

    @commands.command(name="gay")
    async def gay(self, ctx):
        await ctx.send("https://media1.tenor.com/images/bd0db1b5fe2cf233439a0758c5b12186/tenor.gif?itemid=12334071")

    @commands.command(name="retard")
    async def retard(self, ctx):
        await ctx.send("https://media.tenor.com/-OoOt1G8q-AAAAAC/gordo-no.gif")

    @commands.command(name="pengy")
    async def pengy(self, ctx):
        await ctx.send("https://tenor.com/view/charge-penguin-highway-gif-21457682")
    
    @commands.command(name="ban")
    async def ban(self, ctx):
        await ctx.send(f"{ctx.author.mention}https://tenor.com/view/bongocat-banhammer-ban-hammer-bongo-gif-18219363")

async def setup(bot):
    await bot.add_cog(Memes(bot))
