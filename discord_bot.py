import discord
import coc
from discord.ext import commands
from pyjavaproperties import Properties

bot = commands.Bot(command_prefix="!")
p = Properties()
p.load(open('bot.properties'))

coc_client = coc.login(p['coc_email'], p['coc_pass'], key_count=5, key_names="Bot key", client=coc.EventsClient)

@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")


bot.run(p['bot_token'])