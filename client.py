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
        await ctx.send(f"Operator, the plains of Cetus are currently bathed in *daylight*<:OstronSyndicateFlag:1291251131246182400>. {cetus_data['timeLeft']} remains until *nightfall* descends.")
    elif cetus_data['isDay'] == False:
        await ctx.send(f"Operator, the plains of Cetus are enveloped in *night*<:OstronSyndicateFlag:1291251131246182400>. The sun will rise in {cetus_data['timeLeft']}")
    else:
        await ctx.send("Error: Unable to retrieve Cetus time cycle data. Cephalon suggests verifying the data source, Operator.")


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


@client.command()
async def voidtrader(ctx):
    voidtrader = req.get("https://api.warframestat.us/pc/en/voidTrader")
    voidtrader_data = voidtrader.json()
    await ctx.send(f"Operator, Baro Ki'Teer will return in *{voidtrader_data['startString']}* at the *{voidtrader_data['location']}*.<:OrokinDucats:1291370996229603430>")

@client.command()
async def archon(ctx):
    archon = req.get("https://api.warframestat.us/pc/en/archonHunt")
    archon_data = archon.json()
    await ctx.send(f"Operator, the Archon Hunt will reset in *{archon_data['eta']}*.<:ArchonShard:1291372955137474681>")

@client.command()
async def sortie(ctx):
    sortie = req.get("https://api.warframestat.us/pc/en/sortie")
    sortie_data = sortie.json()
    await ctx.send(f"Operator, the sortie will reset in *{sortie_data['eta']}*.<:Sortie:1291378207337222224>")

@client.command()
async def api(ctx):
    embed = dis.Embed()
    embed.description = ("[api.warframestat.us](https://api.warframestat.us/pc/en)")
    await ctx.send(embed=embed)

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
    embed.description = f"Operator, your randomized Warframe is... [{random_frame}](https://warframe.fandom.com/wiki/{random_frame})."
    await ctx.send(embed=embed)

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')

client.run(client_token)
