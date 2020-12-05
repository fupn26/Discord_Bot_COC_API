import discord
import coc
import traceback
from discord.ext import commands
from pyjavaproperties import Properties

bot = commands.Bot(command_prefix="!")
p = Properties()
p.load(open('bot.properties'))

#coc_client = coc.login(p['coc_email'], p['coc_pass'], key_count=5, key_names="Bot key", client=coc.EventsClient)
coc_client = coc.login(p['coc_email'], p['coc_pass'], key_count=5, key_names="Bot key", client=coc.EventsClient)


@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")

@bot.command()
async def heroes(ctx, player_tag):
    print("Used player_tag: {}".format(player_tag))
    player = await coc_client.get_player(str(player_tag))
    print("Player's name: {}".format(player.name))

    to_send = ""
    for hero in player.heroes:
        to_send += "{}: Level {}/{}\n".format(str(hero), hero.level, hero.max_level)

    try:
        await ctx.send(to_send)
    except:
        await ctx.send("Heroes not found")

@bot.command()
async def troops(ctx, player_tag):
    print("Used player_tag: {}".format(player_tag))
    player = await coc_client.get_player(str(player_tag))
    print("Player's name: {}".format(player.name))

    to_send = ""
    for troop in player.troops:
        to_send += "{}: Level {}/{}\n".format(str(troop), troop.level, troop.max_level)

    try:
        await ctx.send(to_send)
    except:
        await ctx.send("Troops not found")

@bot.command()
async def members(ctx, clan_tag):
    print("Used clan_tag: {}".format(clan_tag))
    members = await coc_client.get_members(clan_tag)

    to_send = "Memebers are\n"
    for member in members:
        to_send += "{}\t{}\n".format(member.name, member.tag)

    try:
        await ctx.send(to_send)
    except:
        await ctx.send("Members not found")

bot.run(p['bot_token'])