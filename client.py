import discord as dis
import requests as req
from discord.ext import commands
from bs4 import BeautifulSoup
import random as ran
import time

#! opens token
with open('client_token.txt', 'r') as file:
    client_token = file.read().strip()

#! Globle Vars
API_URL = 'https://api.warframestat.us/pc/en'
API_market_URL = 'https://api.warframe.market/v1/items/'
client_verison = '0.1.9.1'

#! client_verison info
#? first number is for if the bot is out of beta or not 0 = beta, 1 = launched
#? second number is for major verisons that change alot about the bot
#? third number is for minor verisons such as small features
#? forth number is for very minor verisons bug fixs and comments

#! Intents
intents = dis.Intents.default()
intents.message_content = True

#! prefix
client = commands.Bot(command_prefix='~', intents=intents)

#! ~commands

#? ~ping
@client.command()
async def ping(ctx):
    await ctx.send("Operator, Cordis been Pinged. Do you need my help?")

#? ~verison
@client.command()
async def verison(ctx):
    await ctx.send(f"Operator, Cordis's Software Verison is v{client_verison}")

#? ~cetus
@client.command()
async def cetus(ctx):
    cetus = req.get("https://api.warframestat.us/pc/en/cetusCycle")
    cetus_data = cetus.json()
    if cetus_data['isDay'] == True:
        await ctx.send(f"Operator, the plains of Cetus are currently bathed in *daylight*<:OstronSyndicateFlag:1291251131246182400>. {cetus_data['timeLeft']} remains until *nightfall* descends.")
    elif cetus_data['isDay'] == False:
        await ctx.send(f"Operator, the plains of Cetus are enveloped in *night*<:OstronSyndicateFlag:1291251131246182400>. The sun will rise in {cetus_data['timeLeft']}")
    else:
        await ctx.send("Error: Unable to retrieve Cetus time cycle data. Cephalon suggests verifying the data source, Operator.")

#? ~vallis
@client.command()
async def vallis(ctx):
    vallis = req.get("https://api.warframestat.us/pc/en/vallisCycle")
    vallis_data = vallis.json()
    if vallis_data['isWarm'] == True:
        await ctx.send(f"Operator, it is currently... *warm* on the Vallis<:SolarisUnitedSyndicateFlagRC:1291251177475801128>. The transition to *cold* will occur in {vallis_data['timeLeft']}. Proceed accordingly.")
    elif vallis_data['isWarm'] == False:
        await ctx.send(f"Operator, conditions on the Vallis are currently... *cold*<:SolarisUnitedSyndicateFlagRC:1291251177475801128>. Warmth will return in {vallis_data['timeLeft']}. Shall I prepare for thermal fluctuations?")
    else:
        await ctx.send("Error: Cephalon is unable to retrieve Vallis climate data. Perhaps a... recalibration is in order, Operator.")

#? ~cambion
@client.command()
async def cambion(ctx):
    cambion = req.get("https://api.warframestat.us/pc/en/cambionCycle")
    cambion_data = cambion.json()
    if cambion_data['state'] == "vome":
        await ctx.send(f"Operator, it is currently... *Vome* on the Cambion Drift. {cambion_data['timeLeft']} remains until *Fass* emerges once more.")
    elif cambion_data['state'] == "fass":
        await ctx.send(f"Operator, the Cambion Drift is under the influence of *Fass*. The cycle will shift to *Vome* in {cambion_data['timeLeft']}.")
    else:
        await ctx.send("Error: Unable to retrieve Cambion Drift state. Cephalon suggests recalibration, Operator.")

#? ~zariman
@client.command()
async def zariman(ctx):
    zariman = req.get("https://api.warframestat.us/pc/en/zarimanCycle")
    zariman_data = zariman.json()
    if zariman_data['isCorpus'] == True:
        await ctx.send(f"Operator, the Zariman is currently under *Corpus* influence<:CorpusIcon:1291251906576121947>. {zariman_data['timeLeft']} until the *Grineer* seize control<:GrineerIcon:1291251937802588180>.")
    elif zariman_data['isCorpus'] == False:
        await ctx.send(f"Operator, the Zariman is currently controlled by the *Grineer*<:GrineerIcon:1291251937802588180>. The shift to *Corpus* control will occur in {zariman_data['timeLeft']}<:CorpusIcon:1291251906576121947>.")
    else:
        await ctx.send("Error: Unable to retrieve Zariman faction data. Cephalon recommends further diagnostic, Operator.")

#? voidtrader
@client.command()
async def voidtrader(ctx):
    voidtrader = req.get("https://api.warframestat.us/pc/en/voidTrader")
    voidtrader_data = voidtrader.json()
    await ctx.send(f"Operator, Baro Ki'Teer will return in *{voidtrader_data['startString']}* at the *{voidtrader_data['location']}*.<:OrokinDucats:1291370996229603430>")

#? ~archon
@client.command()
async def archon(ctx):
    archon = req.get("https://api.warframestat.us/pc/en/archonHunt")
    archon_data = archon.json()
    await ctx.send(f"Operator, the Archon Hunt will reset in *{archon_data['eta']}*.<:ArchonShard:1291372955137474681>")

#? ~sortie
@client.command()
async def sortie(ctx):
    sortie = req.get("https://api.warframestat.us/pc/en/sortie")
    sortie_data = sortie.json()
    await ctx.send(f"Operator, the sortie will reset in *{sortie_data['eta']}*.<:Sortie:1291378207337222224>")

#? ~api
@client.command()
async def api(ctx):
    embed = dis.Embed()
    embed.description = ("[api.warframestat.us](https://api.warframestat.us/pc/en)")
    await ctx.send(embed=embed)

#? ~marketprice
@client.command()
async def marketprice(ctx, item: str):
    embed = dis.Embed()
    embed.description = (f"Operator, This command is in beta, [{item}](https://warframe.market/items/{item})")
    await ctx.send(embed=embed)

#? ~randomframe
@client.command()
async def randomframe(ctx):
    frames = ["Ash", "Atlas", "Banshee", "Baruuk", "Caliban", "Chroma", "Citrine", "Dagath", "Dante", "Ember", "Equinox", "Excalibur", "Frost", "Gara", "Garuda", "Gauss", "Grendel", "Gyre", "Harrow", "Hildryn", "Hydroid", "Inaros", "Ivara", "Jade", "Khora", "Koumei", "Kullervo", "Lavos", "Limbo", "Loki", "Mag", "Mesa", "Mirage", "Nekros", "Nezha", "Nidus", "Nova", "Nyx", "Oberon", "Octavia", "Protea", "Qorvex", "Revenant", "Rhino", "Saryn", "Sevagoth", "Styanax", "Titania", "Trinity", "Valkyr", "Vauban", "Volt", "Voruna", "Wisp", "Wukong", "Xaku", "Yareli", "Zephyr"]
    random_frame = ran.choice(frames) #random choice from list above
    print(f"random choice = {random_frame}") #prints to console *just for debug*
    embed = dis.Embed() #defines embed
    embed.description = f"Operator, your randomized Warframe is... [{random_frame}](https://warframe.fandom.com/wiki/{random_frame})."
    await ctx.send(embed=embed)#sends embed

#? ~guilds
@client.command()
async def guilds(ctx):
    await ctx.send('Operator, Cordis is working on this command it is not ready')

#? ~relics
@client.command()
async def relics(ctx):
    relics = []
    await ctx.send('Operator, Cordis is working on this command it is not ready')

#! admin commands

#? ~kick
@client.command()
@commands.has_permissions(kick_members=True)  #user needs perissions to run
async def kick(ctx, member: dis.Member, *, reason=None):
    await member.kick(reason=reason) #kicks named user
    await ctx.send(f'Operator, {member} has been kicked for {reason}.')

#? ~ban
@client.command()
@commands.has_permissions(ban_members=True) #user needs perissions to run
async def ban(ctx, member: dis.Member, *, reason=None):
    await member.ban(reason=reason) #kicks named user
    await ctx.send(f'Operator, {member} has been Banned for {reason}.')

#! login msg
@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')

#! run client
client.run(client_token)