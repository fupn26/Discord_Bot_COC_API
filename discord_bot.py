import discord
from discord.ext import commands
from pyjavaproperties import Properties

bot = commands.Bot(command_prefix="!")

@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")

bot.run('Nzg0NzIwNDk3NTA5NDAwNTc2.X8tZ6g.FMw0bPF4u_qRpZgDcAZ055byWdU')