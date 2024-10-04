import discord as dis
import requests as req
from discord.ext import commands
from bs4 import BeautifulSoup
import random as ran
import time

with open('client_token.txt', 'r') as file:
    client_token = file.read().strip()

API_URL = 'https://api.warframestat.us/pc/en'

intents = dis.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='~', intents=intents)

@client.command()
async def ping(ctx):
    await ctx.send("Client Pinged")

@client.command()
async def cetus(ctx):
    cetus = req.get("https://api.warframestat.us/pc/en/cetusCycle")
    cetus_data = cetus.json()
    if cetus_data['isDay'] == True:
        await ctx.send(f"it is day on cetus<:OstronSyndicateFlag:1291251131246182400>, {cetus_data['timeLeft']} to night")
    elif cetus_data['isDay'] == False:
        await ctx.send(f"it is night on cetus<:OstronSyndicateFlag:1291251131246182400>, {cetus_data['timeLeft']} to day")
    else:
        await ctx.send("couldn't request data")

@client.command()
async def vallis(ctx):
    vallis = req.get("https://api.warframestat.us/pc/en/vallisCycle")
    vallis_data = vallis.json()
    if vallis_data['isWarm'] == True:
        await ctx.send(f"it is warm on the Vallis<:SolarisUnitedSyndicateFlagRC:1291251177475801128>, {vallis_data['timeLeft']} to cold")
    elif vallis_data['isWarm'] == False:
        await ctx.send(f"it is cold on the Vallis<:SolarisUnitedSyndicateFlagRC:1291251177475801128>, {vallis_data['timeLeft']} to warm")
    else:
        await ctx.send("couldn't request data")

@client.command()
async def cambion(ctx):
    cambion = req.get("https://api.warframestat.us/pc/en/cambionCycle")
    cambion_data = cambion.json()
    if cambion_data['state'] == "vome":
        await ctx.send(f"it is vome on the Cambion Drift, {cambion_data['timeLeft']} to fass")
    elif cambion_data['state'] == "fass":
        await ctx.send(f"it is fass on the Cambion Drift, {cambion_data['timeLeft']} to vome")
    else:
        await ctx.send("couldn't request data")

@client.command()
async def zariman(ctx):
    zariman = req.get("https://api.warframestat.us/pc/en/zarimanCycle")
    zariman_data = zariman.json()
    if zariman_data ['isCorpus'] == True:
        await ctx.send(f"The Zariman is Corpus<:CorpusIcon:1291251906576121947>, {zariman_data ['timeLeft']} to Grineer<:GrineerIcon:1291251937802588180> ")
    elif zariman_data ['isCorpus'] == False:
        await ctx.send(f"The Zariman is Grineer<:GrineerIcon:1291251937802588180>, {zariman_data ['timeLeft']} to Corpus<:CorpusIcon:1291251906576121947>")
    else:
        await ctx.send("couldn't request data")

@client.command()
async def voidtrader(ctx):
    voidtrader = req.get("https://api.warframestat.us/pc/en/voidTrader")
    voidtrader_data = voidtrader.json()
    await ctx.send(f"Baro Ki'Teer will return in {voidtrader_data ['startString']} on the {voidtrader_data ['location']} <:OrokinDucats:1291370996229603430>")

@client.command()
async def archon(ctx):
    archon = req.get("https://api.warframestat.us/pc/en/archonHunt")
    archon_data = archon.json()
    await ctx.send(f"The Archon Hunt is going to reset in {archon_data ['eta']} <:ArchonShard:1291372955137474681>")

@client.command()
async def sortie(ctx):
    sortie = req.get("https://api.warframestat.us/pc/en/sortie")
    sortie_data = sortie.json()
    await ctx.send(f"The sortie is going to reset in {sortie_data ['eta']} <:Sortie:1291378207337222224>")

@client.command()
async def api(ctx):
    await ctx.send("api.warframestat.us/pc/en")

@client.command()
async def marketprice(ctx, item: str):
    # market = req.get(f"https://warframe.market/items/{item}/statistics")
    # bs = BeautifulSoup(market.text, "html.parser")
    # price = bs.find("span", class_="legend__avg").text
    # await ctx.send(price)
    await ctx.send("command broken rn")

@client.command()
async def randomframe(ctx):
    frames = ["Ash", "Atlas", "Banshee", "Baruuk", "Caliban", "Chroma", "Citrine", "Dagath", "Ember", "Equinox", "Excalibur", "Frost", "Gara", "Garuda", "Gauss", "Grendel", "Gyre", "Harrow", "Hildryn", "Hydroid", "Inaros", "Ivara", "Khora", "Kullervo", "Lavos", "Limbo", "Loki", "Mag", "Mesa", "Mirage", "Nekros", "Nezha", "Nidus", "Nova", "Nyx", "Oberon", "Octavia", "Protea", "Qorvex", "Revenant", "Rhino", "Saryn", "Sevagoth", "Styanax", "Titania", "Trinity", "Valkyr", "Vauban", "Volt", "Voruna", "Wisp", "Wukong", "Xaku", "Yareli", "Zephyr"]
    random_frame = ran.choice(frames)
    print(f"random choice = {random_frame}")
    embed = dis.Embed()
    embed.description = f"Your Random Warframe is [{random_frame}](https://warframe.fandom.com/wiki/{random_frame})"
    await ctx.send(embed=embed)

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')

client.run(client_token)
