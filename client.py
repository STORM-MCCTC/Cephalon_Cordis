import discord as dis
import requests as req
from discord.ext import commands

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
        await ctx.send(f"it is day on cetus, {cetus_data['timeLeft']} to night")
    elif cetus_data['isDay'] == False:
        await ctx.send(f"it is night on the Vallis, {cetus_data['timeLeft']} to day")
    else:
        await ctx.send("couldn't request data")

@client.command()
async def vallis(ctx):
    vallis = req.get("https://api.warframestat.us/pc/en/vallisCycle")
    vallis_data = vallis.json()
    if vallis_data['isWarm'] == True:
        await ctx.send(f"it is warm on the Vallis, {vallis_data['timeLeft']} to cold")
    elif vallis_data['isWarm'] == False:
        await ctx.send(f"it is cold on the Vallis, {vallis_data['timeLeft']} to warm")
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

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')

client.run(client_token)
