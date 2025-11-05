
import discord
from discord.ext import commands
import json
import re
import os
from ezgiphy import GiphyPublicAPI

class Counters(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.giphy = GiphyPublicAPI(os.getenv('GIPHY_API_KEY'))
        with open('counters.json', 'r') as file:
            self.counter_data = json.load(file)

    def update_counters(self):
        with open('counters.json', 'w') as file:
            json.dump(self.counter_data, file)

    async def handle_counter(self, message, user_id, keyword, response_template, regex):
        if str(message.author.id) == user_id and re.search(regex, message.content, re.IGNORECASE) and message.author != self.bot.user:
            mentions = len(re.findall(regex, message.content, re.IGNORECASE))
            self.counter_data['counters'][keyword] += mentions
            response = response_template.format(count=self.counter_data['counters'][keyword])
            await message.channel.send(response)
            self.update_counters()

    @commands.Cog.listener()
    async def on_message(self, message):
        await self.handle_counter(message, os.getenv('PIMO_ID'), 'cat', 'pimo has mentioned cats {count} times so far', r'\b(+a+t+s\b')
        await self.handle_counter(message, os.getenv('PENGY_ID'), 'bored', 'Pengy has been bored {count} times so far', r'\bb+o+r+e+d+s\b')
        await self.handle_counter(message, os.getenv('CRES_ID'), 'sigh', 'Cres has sighed {count} times so far', r'(?i)\bs+i+gh+\w*\b')
        await self.handle_counter(message, os.getenv('PROMMIE_ID'), 'cow', 'prommie has eaten {count} cows and counting', r'\bc+o+w+s*\b')

    @commands.command(name="cat")
    async def cat(self, ctx):
        await ctx.send("CAAAAAATS!")
        response = json.loads(self.giphy.random(tag='cat',rating='g')).get("data")
        await ctx.send(response["url"])

async def setup(bot):
    await bot.add_cog(Counters(bot))
