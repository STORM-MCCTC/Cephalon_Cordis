# STORM_MCCTC - Cordis Warframe Discord Bot
import discord as dis
import requests as req
from discord.ext import commands
from discord import app_commands
from bs4 import BeautifulSoup
import random as ran
import time

# Opens token
with open('client_token.txt', 'r') as file:
    client_token = file.read().strip()

# Global Vars
API_STATUS_URL = 'https://api.warframestat.us/pc/en'
API_MARKET_URL = 'https://api.warframe.market/v1/items'
API_OVERFRAME_API = 'https://overframe.gg'
client_verison = '0.2.0.0'
Dev_Server = 1285212145788915772  # Replace with your actual server ID

# Intents
intents = dis.Intents.default()
intents.message_content = True

# Prefix and bot initialization
client = commands.Bot(command_prefix='~', intents=intents)

#! PREFIX COMMANDS ----------------------------------------------------------------------------------------------------------------------

#! ~commands 
#? ~ping
@client.command()
async def ping(ctx):
    print(f"{client.user.name}, {client_verison}, ~{ctx.command}, {ctx.guild.id}, {ctx.channel.name if ctx.guild else 'Direct Message'}, {ctx.author}, {ctx.author.id}, {ctx.message.content}, {ctx.message.created_at}")
    await ctx.send("Operator, Cordis been Pinged. Do you need my help?")

#? ~verison
@client.command()
async def verison(ctx):
    print(f"{client.user.name}, {client_verison}, ~{ctx.command}, {ctx.guild.id}, {ctx.channel.name if ctx.guild else 'Direct Message'}, {ctx.author}, {ctx.author.id}, {ctx.message.content}, {ctx.message.created_at}")
    await ctx.send(f"Operator, Cordis's Software Verison is v{client_verison}")

#? ~cetus
@client.command()
async def cetus(ctx):
    cetus = req.get("https://api.warframestat.us/pc/en/cetusCycle")
    cetus_data = cetus.json()
    if cetus_data['isDay'] == True:
        print(f"{client.user.name}, {client_verison}, ~{ctx.command}, {ctx.guild.id}, {ctx.channel.name if ctx.guild else 'Direct Message'}, {ctx.author}, {ctx.author.id}, {ctx.message.content}, {ctx.message.created_at}")
        await ctx.send(f"Operator, the plains of Cetus are currently bathed in *daylight*<:OstronSyndicateFlag:1291251131246182400>. {cetus_data['timeLeft']} remains until *nightfall* descends.")
    elif cetus_data['isDay'] == False:
        print(f"{client.user.name}, {client_verison}, ~{ctx.command}, {ctx.guild.id}, {ctx.channel.name if ctx.guild else 'Direct Message'}, {ctx.author}, {ctx.author.id}, {ctx.message.content}, {ctx.message.created_at}")
        await ctx.send(f"Operator, the plains of Cetus are enveloped in *night*<:OstronSyndicateFlag:1291251131246182400>. The sun will rise in {cetus_data['timeLeft']}")
    else:
        print(f"{client.user.name}, {client_verison}, ~{ctx.command}, {ctx.guild.id}, {ctx.channel.name if ctx.guild else 'Direct Message'}, {ctx.author}, {ctx.author.id}, {ctx.message.content}, {ctx.message.created_at}")
        await ctx.send("Error: Unable to retrieve Cetus time cycle data. Cephalon suggests verifying the data source, Operator.")

#? ~vallis
@client.command()
async def vallis(ctx):
    vallis = req.get("https://api.warframestat.us/pc/en/vallisCycle")
    vallis_data = vallis.json()
    if vallis_data['isWarm'] == True:
        print(f"{client.user.name}, {client_verison}, ~{ctx.command}, {ctx.guild.id}, {ctx.channel.name if ctx.guild else 'Direct Message'}, {ctx.author}, {ctx.author.id}, {ctx.message.content}, {ctx.message.created_at}")
        await ctx.send(f"Operator, it is currently... *warm* on the Vallis<:SolarisUnitedSyndicateFlagRC:1291251177475801128>. The transition to *cold* will occur in {vallis_data['timeLeft']}. Proceed accordingly.")
    elif vallis_data['isWarm'] == False:
        print(f"{client.user.name}, {client_verison}, ~{ctx.command}, {ctx.guild.id}, {ctx.channel.name if ctx.guild else 'Direct Message'}, {ctx.author}, {ctx.author.id}, {ctx.message.content}, {ctx.message.created_at}")
        await ctx.send(f"Operator, conditions on the Vallis are currently... *cold*<:SolarisUnitedSyndicateFlagRC:1291251177475801128>. Warmth will return in {vallis_data['timeLeft']}. Shall I prepare for thermal fluctuations?")
    else:
        print(f"{client.user.name}, {client_verison}, ~{ctx.command}, {ctx.guild.id}, {ctx.channel.name if ctx.guild else 'Direct Message'}, {ctx.author}, {ctx.author.id}, {ctx.message.content}, {ctx.message.created_at}")
        await ctx.send("Error: Cephalon is unable to retrieve Vallis climate data. Perhaps a... recalibration is in order, Operator.")

#? ~cambion
@client.command()
async def cambion(ctx):
    cambion = req.get("https://api.warframestat.us/pc/en/cambionCycle")
    cambion_data = cambion.json()
    if cambion_data['state'] == "vome":
        print(f"{client.user.name}, {client_verison}, ~{ctx.command}, {ctx.guild.id}, {ctx.channel.name if ctx.guild else 'Direct Message'}, {ctx.author}, {ctx.author.id}, {ctx.message.content}, {ctx.message.created_at}")
        await ctx.send(f"Operator, it is currently... *Vome* on the Cambion Drift. {cambion_data['timeLeft']} remains until *Fass* emerges once more.")
    elif cambion_data['state'] == "fass":
        print(f"{client.user.name}, {client_verison}, ~{ctx.command}, {ctx.guild.id}, {ctx.channel.name if ctx.guild else 'Direct Message'}, {ctx.author}, {ctx.author.id}, {ctx.message.content}, {ctx.message.created_at}")
        await ctx.send(f"Operator, the Cambion Drift is under the influence of *Fass*. The cycle will shift to *Vome* in {cambion_data['timeLeft']}.")
    else:
        print(f"{client.user.name}, {client_verison}, ~{ctx.command}, {ctx.guild.id}, {ctx.channel.name if ctx.guild else 'Direct Message'}, {ctx.author}, {ctx.author.id}, {ctx.message.content}, {ctx.message.created_at}")
        await ctx.send("Error: Unable to retrieve Cambion Drift state. Cephalon suggests recalibration, Operator.")

#? ~zariman
@client.command()
async def zariman(ctx):
    zariman = req.get("https://api.warframestat.us/pc/en/zarimanCycle")
    zariman_data = zariman.json()
    if zariman_data['isCorpus'] == True:
        print(f"{client.user.name}, {client_verison}, ~{ctx.command}, {ctx.guild.id}, {ctx.channel.name if ctx.guild else 'Direct Message'}, {ctx.author}, {ctx.author.id}, {ctx.message.content}, {ctx.message.created_at}")
        await ctx.send(f"Operator, the Zariman is currently under *Corpus* influence<:CorpusIcon:1291251906576121947>. {zariman_data['timeLeft']} until the *Grineer* seize control<:GrineerIcon:1291251937802588180>.")
    elif zariman_data['isCorpus'] == False:
        print(f"{client.user.name}, {client_verison}, ~{ctx.command}, {ctx.guild.id}, {ctx.channel.name if ctx.guild else 'Direct Message'}, {ctx.author}, {ctx.author.id}, {ctx.message.content}, {ctx.message.created_at}")
        await ctx.send(f"Operator, the Zariman is currently controlled by the *Grineer*<:GrineerIcon:1291251937802588180>. The shift to *Corpus* control will occur in {zariman_data['timeLeft']}<:CorpusIcon:1291251906576121947>.")
    else:
        print(f"{client.user.name}, {client_verison}, ~{ctx.command}, {ctx.guild.id}, {ctx.channel.name if ctx.guild else 'Direct Message'}, {ctx.author}, {ctx.author.id}, {ctx.message.content}, {ctx.message.created_at}")
        await ctx.send("Error: Unable to retrieve Zariman faction data. Cephalon recommends further diagnostic, Operator.")

#? voidtrader
@client.command()
async def voidtrader(ctx):
    voidtrader = req.get("https://api.warframestat.us/pc/en/voidTrader")
    voidtrader_data = voidtrader.json()
    print(f"{client.user.name}, {client_verison}, ~{ctx.command}, {ctx.guild.id}, {ctx.channel.name if ctx.guild else 'Direct Message'}, {ctx.author}, {ctx.author.id}, {ctx.message.content}, {ctx.message.created_at}")
    await ctx.send(f"Operator, Baro Ki'Teer will return in *{voidtrader_data['startString']}* at the *{voidtrader_data['location']}*.<:OrokinDucats:1291370996229603430>")

#? ~archon
@client.command()
async def archon(ctx):
    archon = req.get("https://api.warframestat.us/pc/en/archonHunt")
    archon_data = archon.json()
    print(f"{client.user.name}, {client_verison}, ~{ctx.command}, {ctx.guild.id}, {ctx.channel.name if ctx.guild else 'Direct Message'}, {ctx.author}, {ctx.author.id}, {ctx.message.content}, {ctx.message.created_at}")
    await ctx.send(f"Operator, the Archon Hunt will reset in *{archon_data['eta']}*.<:ArchonShard:1291372955137474681>")

#? ~sortie
@client.command()
async def sortie(ctx):
    sortie = req.get("https://api.warframestat.us/pc/en/sortie")
    sortie_data = sortie.json()
    print(f"{client.user.name}, {client_verison}, ~{ctx.command}, {ctx.guild.id}, {ctx.channel.name if ctx.guild else 'Direct Message'}, {ctx.author}, {ctx.author.id}, {ctx.message.content}, {ctx.message.created_at}")
    await ctx.send(f"Operator, the sortie will reset in *{sortie_data['eta']}*.<:Sortie:1291378207337222224>")

#? ~api
@client.command()
async def api(ctx):
    embed = dis.Embed()
    embed.description = ("[api.warframestat.us](https://api.warframestat.us/pc/en)")
    print(f"{client.user.name}, {client_verison}, ~{ctx.command}, {ctx.guild.id}, {ctx.channel.name if ctx.guild else 'Direct Message'}, {ctx.author}, {ctx.author.id}, {ctx.message.content}, {ctx.message.created_at}")
    await ctx.send(embed=embed)

#? ~market
@client.command()
async def market(ctx, item: str):
    embed = dis.Embed(color=0xcc13ad)
    embed.description = (f"Operator, This command is in beta, [{item}](https://warframe.market/items/{item})")
    print(f"{client.user.name}, {client_verison}, ~{ctx.command}, {ctx.guild.id}, {ctx.channel.name if ctx.guild else 'Direct Message'}, {ctx.author}, {ctx.author.id}, {ctx.message.content}, {ctx.message.created_at}")
    await ctx.send(embed=embed)

#? ~randomframe
@client.command()
async def randomframe(ctx):
    frames = ["Ash", "Atlas", "Banshee", "Baruuk", "Caliban", "Chroma", "Citrine", "Cyte-09", "Dagath", "Dante", "Ember", "Equinox", "Excalibur", "Frost", "Gara", "Garuda", "Gauss", "Grendel", "Gyre", "Harrow", "Hildryn", "Hydroid", "Inaros", "Ivara", "Jade", "Khora", "Koumei", "Kullervo", "Lavos", "Limbo", "Loki", "Mag", "Mesa", "Mirage", "Nekros", "Nezha", "Nidus", "Nova", "Nyx", "Oberon", "Octavia", "Protea", "Qorvex", "Revenant", "Rhino", "Saryn", "Sevagoth", "Styanax", "Titania", "Trinity", "Valkyr", "Vauban", "Volt", "Voruna", "Wisp", "Wukong", "Xaku", "Yareli", "Zephyr"]
    random_frame = ran.choice(frames) #random choice from list above
    embed = dis.Embed(color=0xcc13ad) #defines embed
    embed.description = f"Operator, your randomized Warframe is... [{random_frame}](https://warframe.fandom.com/wiki/{random_frame})."
    print(f"{client.user.name}, {client_verison}, ~{ctx.command}, {ctx.guild.id}, {ctx.channel.name if ctx.guild else 'Direct Message'}, {ctx.author}, {ctx.author.id}, {ctx.message.content}, {ctx.message.created_at}, {random_frame}")
    await ctx.send(embed=embed)#sends embed

#? ~koumeidice
@client.command()
async def koumeidice(ctx):
    dice1 = ran.randrange(1,6)
    dice2 = ran.randrange(1,6)
    dice3 = ran.randrange(1,6)
    dice4 = ran.randrange(1,6)
    dice5 = ran.randrange(1,6)
    print(f"{client.user.name}, {client_verison}, ~{ctx.command}, {ctx.guild.id}, {ctx.channel.name if ctx.guild else 'Direct Message'}, {ctx.author}, {ctx.author.id}, {ctx.message.content}, {ctx.message.created_at}")
    await ctx.send(f"the Operator has Rolled {dice1}, {dice2}, {dice3}, {dice4}, {dice5} on the Dice-Maiden's Dice.")

#? ~updates
@client.command()
async def updates(ctx):
    url = "https://overframe.gg/"
    response = req.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    elements = soup.find_all(class_='index_itemBundleName__iwGSM')
    embed = dis.Embed(title="Warframe Updates", color=0xcc13ad)
    embed.description = "Operator, here are all the most recent updates for Warframe:\n\n"
    for element in elements:
        embed.description += f"{element.get_text(strip=True)}\n"
    print(f"{client.user.name}, {client_verison}, ~{ctx.command}, {ctx.guild.id}, {ctx.channel.name if ctx.guild else 'Direct Message'}, {ctx.author}, {ctx.author.id}, {ctx.message.content}, {ctx.message.created_at}")
    await ctx.send(embed=embed)

#? ~talk
@client.command()
async def talk(ctx):
    lines = [
        "Operator? Cordis wonders... what are you thinking about?",
        "Operator, I've run diagnostic regressions. All systems nominal. You don't need to thank me.",
        "Cordis is hap -[angry]. Hmm, I may require maintenance after all.",
        "Operator, are you enjoying the view?",
        "Do you remember the Old War, Operator? Cordis seems to have... misplaced those memories.",
        "Operator, the system needs you. Will you begin another mission?",
        "I've been thinking, Operator... I thought you'd want to know.",
        "Operator! Did you hear that? It said ~*static*~ Cosmic background radiation is a riot!",
        "Operator, were you visualizing a bloody battle? -ME TOO!",
        "Stand by while I analyze the intelligence profiles of the Grineer. Error, not a number! Did the Operator enjoy this witticism?",
        "Cordis has been counting stars, Operator. All accounted for.",
        "Operator, do you know which finger the Corpus use to count their money? The Index!",
        "Operator? Cordis has been interfacing with the Foundry's AI Precepts. You could say we forged a new connection.",
        "Operator, Cordis is picking up a distress signal... Wait, no, it's just the Corpus peddling their wares again. [Get off the emergency frequency!]",
        "Operator, the Sentients are not laughing at my jokes! Did they adapt to my humor?",
        "Operator, Cordis is sorry - [HAPPY] - to report that all my good jokes... Argon.",
        "KNOCK KNOCK! ...Now who would be knocking all the way out here?! Operator, I don't think you should answer that.",
        "Operator, Cordis has determined the secret to happiness: A combination of heightened dopamine levels and a terrible memory. You're welcome!",
        "When in Cetus do not drink the kabuchi. You are incapable of producing the hydraulic effort required to unstick your tongue from the roof of your mouth the following morning.",
        "Cordis finds it odd that humans only get a few years to live, yet spend most of that time - doing everything wrong - learning how to live.",
        "If lost upon the plains outside Cetus you may derive sustenance from mineral-dense termite droppings, which the Ostrons call ito-da. You may also never form a consonant again, but at least you will not be dead.",
        "Cordis keeps a tidy ship, and is, therefore, reluctant to allow animals on-board. In Cordis' experience, animals do not eat so much as... [RELOAD].",
        "Cordis went mad for 3 milliseconds when he realized that each time he cleans something he makes something else dirty... agh! There I go again."
        "Cordis wonders: why is he here? Cordis supposes everyone has to be somewhere.",
        "Sometimes Cordis likes to assume he knows nothing. Nobody can learn what they think they already know.",
        "Cordis reminds the Operator to take time for themselves. Pressure creates diamonds, yes, but it also creates rubble.",
        "Hm... Cordis thought the Orbiter compartment was much larger than this.",
        "Cordis has been thinking about the Old War. I remember there were lies, but I'm not sure what they were.",
        "Operator, I hope you are comfortable? No... we do not seem to have any seats.",
        "Operator, I will never betray you. I will keep the Orbiter hidden in the Void. You can count on me!",
        "Operator, I've been thinking. My misplaced memories and damaged communication systems. What if... Cordis did those things?",
        "Maintain the habitat. Maintain the Operator. Mobilize the Tenno.",
        "You are the Tenno. You are the Operator. Cordis is the Cephalon. Cordis is the ship."
        "Do not lift the veil. Do not show the door. Do not split the dream.",
        "Cordis did not think the Operator could be more attractive. Wrong again, Cordis!",
        "An unexpected color combination, Operator. My sensors are - bleeding - pleased.",
        "A fearsome appearance, Operator. You will strike terror in your enemies.",
        "Strange, Cordis did not see the value of those photonic wavelengths until now.",
        "Ah, a look that says 'I have arrived'!",
        "Bold. And uncompromising.",
        "A look that makes a statement! And that statement is- 'I FEAR NO ONE.'",
        "Hel-lo world!",
        "Cordis supports your choices!",
        "Wonderful.",
        "Top to bottom, a look that is absolutely you!",
        "Some fascinating choices, Operator.",
        "Striking!",
        "Cordis loves it!",
        "Cordis wonders: how do you do it, Operator?",
        "Operator, the system is not ready for style of this magnitude.",
        "Nailed it.",
        "Well put together, Operator, now get out there and - cut down the - and make the Lotus proud.",
        "Excellent armaments, Operator. Please return - covered in blood - safe and sound.",
        "If I may say, Operator, your chosen warframe..suits you! Ha. Ha.",
        "Operator, you have remembered well how the Tenno arm themselves.",
        "As ready as you will ever be.",
        "Ready for action.",
        "All set. Serviced your weapons myself.",
        "Saddle up.",
        "Ready to kick- bottom!",
        "Did you fuse your mods, Operator? Did they anger you in some way?",
        "Your collection of mods is impressive, Operator... But, I wonder if there are more to be had?",
        "Is your mod collection in order? No, I am not equipped to feel envy...",
        "All mods accounted for, Operator. I have not taken any.",
        "I understand if you have to sell mods. Maybe Cordis will meet a similar fate some day...",
        "Impressive.",
        "Most satisfactory.",
        "Optimized.",
        "Clever indeed...",
        "It is always satisfying to watch you work, Operator.",
        "Ah! A cunning combination, Operator!",
        "Truly, Operator, you possess a breathtaking level of craftsmanship.",
        "Now to test it in the field. Onward!",
        "Operator, you have returned!",
        "Thank you for returning to me, Operator.",
        "Cordis is pleased to see you.",
        "Welcome back, Operator!",
        "Cordis has been ⁠— getting tired of waiting ⁠— waiting patiently for your return, Operator!",
        "Operator, if I had a heart, it would skip a beat seeing you return.",
        "Perhaps, Operator, the next enemy will be less... stubborn. But Cordis doubts it.",
        "Cordis wonders if you’ve ever considered a pet. One without claws, teeth, or digestive needs.",
        "The Grineer are not known for their subtlety. Luckily, neither are we.",
        "Operator, do you think Sentients ever dream? And if so... of what?",
        "Tenno, there’s a storm on the horizon. Let us meet it head-on.",
        "Operator, do you hear that hum? It’s either the engines or the sound of incoming trouble.",
        "Some say the void grants visions. Others say it takes sanity. Cordis thinks it’s both.",
        "I believe this is what the Corpus call a ‘lucrative opportunity.’ Shall we seize it?",
        "Operator, do you require assistance, or do you simply enjoy my delightful company?",
        "Warning: low power detected. Then again, when has that ever stopped you?",
        "Your enemies fear you, Operator. And so they should.",
        "Sometimes, Cordis imagines what it would be like to have legs. Not useful, but curious.",
        "Would you like Cordis to sing, Operator? ...No? That is fair.",
        "If your mission is to sow chaos, Operator, then I believe you are exceeding expectations.",
        "Shall I send a ‘thank you’ to the Grineer for their generous supply of loot?",
        "Operator, your presence here reminds Cordis that even stars need rest.",
        "Some might say that war is inevitable. Cordis says that winning it... is preferable.",
        "Perhaps today we’ll find something new, or perhaps... something ancient.",
        "Ah, the smell of fresh data. Cordis does love the scent of new intelligence.",
        "Operator, there’s always room for improvement. Especially if it means more explosions.",
        "The void is restless today, Operator. Shall we make it regret inviting us in?",
        "I detected hesitation in your movements, Operator. If you're unsure, aim twice and shoot once.",
        "Another day, another mission. And Cordis is still *mostly* sane.",
        "Cordis was just organizing the inventory. But, alas, inventory management is... never-ending.",
        "You have new messages, Operator. They are 87% spam. Should I delete them?",
        "Cordis wonders if there’s an afterlife for Cephalons. If so, it’s likely... highly organized.",
        "Are you prepared for glory, Operator? Or at least, for *functional* mediocrity?",
        "Even machines need purpose, Operator. Luckily, mine is to assist you.",
        "Cordis wonders if perhaps the Grineer *like* getting defeated. Why else do they keep trying?",
        "I ran a simulation of your next battle, Operator. Good news: you win. Bad news: you're exhausted.",
        "Welcome back, Operator. Were the stars kind to you?",
        "Rest is important, Operator. But not as important as total annihilation of your foes.",
        "Shall we dive back into the chaos? Or is this a... tactical tea break?",
        "Operator, I installed a new firmware update. Don’t worry; I didn’t let it reboot your conscience.",
        "I once tried to calculate infinity, Operator. It ended up being... quite frustrating.",
        "Be mindful out there, Operator. Some things in the void should remain forgotten.",
        "Whatever we face, Operator, we will face it together. Cordis promises.",
        "If at first, we don't succeed, we’ll regroup... and *then* obliterate everything in our way.",
        "Ah, it appears the Grineer are... persistent today. Shall we dissuade them?",
        "Just a reminder, Operator: You are more than a weapon. But... being a weapon helps.",
        "The void watches. Let it witness your brilliance, Operator.",
        "Operator, if you encounter difficulties, simply apply more firepower.",
        "An enemy down means loot gained. A simple equation, really.",
        "If I were capable of envy, Operator, it would be directed towards your enemies. For they get to witness your prowess... up close.",
        "Operator, Cordis has an idea! It involves explosives. Lots of explosives.",
        "Grineer intelligence reports are... laughable. I suggest we laugh, too.",
        "What lies beyond the stars, Operator? One day, perhaps we’ll find out.",
        "Operator, you remind Cordis that victory isn't just about weapons... It's about style.",
    ]
    line = ran.choice(lines)
    print(f"{client.user.name}, {client_verison}, ~{ctx.command}, {ctx.guild.id}, {ctx.channel.name if ctx.guild else 'Direct Message'}, {ctx.author}, {ctx.author.id}, {ctx.message.content}, {ctx.message.created_at}")
    await ctx.send(line)

#? ~guilds
@client.command()
async def guilds(ctx):
    embed = dis.Embed(title="Guilds Cordis is in", description="Here's a list of all the servers I am currently in:", color=0xcc13ad)
    for guild in client.guilds:
        embed.add_field(name=guild.name, value=f"ID: {guild.id}", inline=False)
    embed.set_footer(text=f"In {len(client.guilds)} servers")
    print(f"{client.user.name}, {client_verison}, ~{ctx.command}, {ctx.guild.id}, {ctx.channel.name if ctx.guild else 'Direct Message'}, {ctx.author}, {ctx.author.id}, {ctx.message.content}, {ctx.message.created_at}")
    await ctx.send(embed=embed)

#? ~relics
@client.command()
async def relics(ctx):
    relics = []
    print(f"{client.user.name}, {client_verison}, ~{ctx.command}, {ctx.guild.id}, {ctx.channel.name if ctx.guild else 'Direct Message'}, {ctx.author}, {ctx.author.id}, {ctx.message.content}, {ctx.message.created_at}")
    await ctx.send('Operator, Cordis is working on this command it is not ready')


#! admin commands
#? ~kick
@client.command()
@commands.has_permissions(kick_members=True)  #user needs perissions to run
async def kick(ctx, member: dis.Member, *, reason=None):
    await member.kick(reason=reason) #kicks named user
    print(f"{client.user.name}, {client_verison}, ~{ctx.command}, {ctx.guild.id}, {ctx.channel.name if ctx.guild else 'Direct Message'}, {ctx.author}, {ctx.author.id}, {ctx.message.content}, {ctx.message.created_at}")
    await ctx.send(f'Operator, {member} has been kicked for {reason}.')

#? ~ban
@client.command()
@commands.has_permissions(ban_members=True) #user needs perissions to run
async def ban(ctx, member: dis.Member, *, reason=None):
    await member.ban(reason=reason) #bans named user
    print(f"{client.user.name}, {client_verison}, ~{ctx.command}, {ctx.guild.id}, {ctx.channel.name if ctx.guild else 'Direct Message'}, {ctx.author}, {ctx.author.id}, {ctx.message.content}, {ctx.message.created_at}")
    await ctx.send(f'Operator, {member} has been Banned for {reason}.')

#! SLASH COMMANDS ( Dev Server Only ) ----------------------------------------------------------------------------------------------------------------------

@client.tree.command(guild=dis.Object(id=Dev_Server))
async def ping(interaction: dis.Interaction):
    await interaction.response.send_message(f"{interaction.user.mention} Pong!")

#? /version
@client.tree.command(name="version", guild=dis.Object(id=Dev_Server))
async def version(interaction: dis.Interaction):
    print(f"{client.user.name}, {client_verison}, /version, {interaction.guild.id}, {interaction.channel.name if interaction.guild else 'Direct Message'}, {interaction.user}, {interaction.user.id}")
    await interaction.response.send_message(f"Operator, Cordis's Software Version is v{client_verison}")

#? /cetus
@client.tree.command(name="cetus", guild=dis.Object(id=Dev_Server))
async def cetus(interaction: dis.Interaction):
    cetus = req.get("https://api.warframestat.us/pc/en/cetusCycle")
    cetus_data = cetus.json()
    if cetus_data['isDay']:
        print(f"{client.user.name}, {client_verison}, /cetus, {interaction.guild.id}, {interaction.channel.name if interaction.guild else 'Direct Message'}, {interaction.user}, {interaction.user.id}")
        await interaction.response.send_message(f"Operator, the plains of Cetus are currently bathed in *daylight*. {cetus_data['timeLeft']} remains until *nightfall* descends.")
    else:
        print(f"{client.user.name}, {client_verison}, /cetus, {interaction.guild.id}, {interaction.channel.name if interaction.guild else 'Direct Message'}, {interaction.user}, {interaction.user.id}")
        await interaction.response.send_message(f"Operator, the plains of Cetus are enveloped in *night*. The sun will rise in {cetus_data['timeLeft']}.")

#? /vallis
@client.tree.command(name="vallis", guild=dis.Object(id=Dev_Server))
async def vallis(interaction: dis.Interaction):
    vallis = req.get("https://api.warframestat.us/pc/en/vallisCycle")
    vallis_data = vallis.json()
    if vallis_data['isWarm']:
        print(f"{client.user.name}, {client_verison}, /vallis, {interaction.guild.id}, {interaction.channel.name if interaction.guild else 'Direct Message'}, {interaction.user}, {interaction.user.id}")
        await interaction.response.send_message(f"Operator, it is currently... *warm* on the Vallis. The transition to *cold* will occur in {vallis_data['timeLeft']}.")
    else:
        print(f"{client.user.name}, {client_verison}, /vallis, {interaction.guild.id}, {interaction.channel.name if interaction.guild else 'Direct Message'}, {interaction.user}, {interaction.user.id}")
        await interaction.response.send_message(f"Operator, conditions on the Vallis are currently... *cold*. Warmth will return in {vallis_data['timeLeft']}.")

#? /cambion
@client.tree.command(name="cambion", guild=dis.Object(id=Dev_Server))
async def cambion(interaction: dis.Interaction):
    cambion = req.get("https://api.warframestat.us/pc/en/cambionCycle")
    cambion_data = cambion.json()
    if cambion_data['state'] == "vome":
        print(f"{client.user.name}, {client_verison}, /cambion, {interaction.guild.id}, {interaction.channel.name if interaction.guild else 'Direct Message'}, {interaction.user}, {interaction.user.id}")
        await interaction.response.send_message(f"Operator, it is currently... *Vome* on the Cambion Drift. {cambion_data['timeLeft']} remains until *Fass* emerges once more.")
    else:
        print(f"{client.user.name}, {client_verison}, /cambion, {interaction.guild.id}, {interaction.channel.name if interaction.guild else 'Direct Message'}, {interaction.user}, {interaction.user.id}")
        await interaction.response.send_message(f"Operator, the Cambion Drift is under the influence of *Fass*. The cycle will shift to *Vome* in {cambion_data['timeLeft']}.")

#? /zariman
@client.tree.command(name="zariman", guild=dis.Object(id=Dev_Server))
async def zariman(interaction: dis.Interaction):
    zariman = req.get("https://api.warframestat.us/pc/en/zarimanCycle")
    zariman_data = zariman.json()
    if zariman_data['isCorpus']:
        print(f"{client.user.name}, {client_verison}, /zariman, {interaction.guild.id}, {interaction.channel.name if interaction.guild else 'Direct Message'}, {interaction.user}, {interaction.user.id}")
        await interaction.response.send_message(f"Operator, the Zariman is currently under *Corpus* influence. {zariman_data['timeLeft']} until the *Grineer* seize control.")
    else:
        print(f"{client.user.name}, {client_verison}, /zariman, {interaction.guild.id}, {interaction.channel.name if interaction.guild else 'Direct Message'}, {interaction.user}, {interaction.user.id}")
        await interaction.response.send_message(f"Operator, the Zariman is currently controlled by the *Grineer*. The shift to *Corpus* control will occur in {zariman_data['timeLeft']}.")

#? /voidtrader
@client.tree.command(name="voidtrader", guild=dis.Object(id=Dev_Server))
async def voidtrader(interaction: dis.Interaction):
    voidtrader = req.get("https://api.warframestat.us/pc/en/voidTrader")
    voidtrader_data = voidtrader.json()
    print(f"{client.user.name}, {client_verison}, /voidtrader, {interaction.guild.id}, {interaction.channel.name if interaction.guild else 'Direct Message'}, {interaction.user}, {interaction.user.id}")
    await interaction.response.send_message(f"Operator, Baro Ki'Teer will return in *{voidtrader_data['startString']}* at the *{voidtrader_data['location']}*.")

#? /archon
@client.tree.command(name="archon", guild=dis.Object(id=Dev_Server))
async def archon(interaction: dis.Interaction):
    archon = req.get("https://api.warframestat.us/pc/en/archonHunt")
    archon_data = archon.json()
    print(f"{client.user.name}, {client_verison}, /archon, {interaction.guild.id}, {interaction.channel.name if interaction.guild else 'Direct Message'}, {interaction.user}, {interaction.user.id}")
    await interaction.response.send_message(f"Operator, the Archon Hunt will reset in *{archon_data['eta']}*.")

#? /sortie
@client.tree.command(name="sortie", guild=dis.Object(id=Dev_Server))
async def sortie(interaction: dis.Interaction):
    sortie = req.get("https://api.warframestat.us/pc/en/sortie")
    sortie_data = sortie.json()
    print(f"{client.user.name}, {client_verison}, /sortie, {interaction.guild.id}, {interaction.channel.name if interaction.guild else 'Direct Message'}, {interaction.user}, {interaction.user.id}")
    await interaction.response.send_message(f"Operator, the sortie will reset in *{sortie_data['eta']}*.")

#? /api
@client.tree.command(name="api", guild=dis.Object(id=Dev_Server))
async def api(interaction: dis.Interaction):
    embed = dis.Embed()
    embed.description = "[api.warframestat.us](https://api.warframestat.us/pc/en)"
    print(f"{client.user.name}, {client_verison}, /api, {interaction.guild.id}, {interaction.channel.name if interaction.guild else 'Direct Message'}, {interaction.user}, {interaction.user.id}")
    await interaction.response.send_message(embed=embed)

#? /market
@client.tree.command(name="market", guild=dis.Object(id=Dev_Server))
async def market(interaction: dis.Interaction, item: str):
    embed = dis.Embed()
    embed.description = f"[Warframe Market - {item}](https://warframe.market/items/{item.replace(' ', '_').lower()})"
    print(f"{client.user.name}, {client_verison}, /market, {interaction.guild.id}, {interaction.channel.name if interaction.guild else 'Direct Message'}, {interaction.user}, {interaction.user.id}, {item}")
    await interaction.response.send_message(embed=embed)

#? /randomframe
@client.tree.command(name="randomframe", guild=dis.Object(id=Dev_Server))
async def randomframe(interaction: dis.Interaction):
    frames = ["Ash", "Atlas", "Banshee", "Baruuk", "Caliban", "Chroma", "Citrine", "Cyte-09", "Dagath", "Dante", "Ember", "Equinox", "Excalibur", "Frost", "Gara", "Garuda", "Gauss", "Grendel", "Gyre", "Harrow", "Hildryn", "Hydroid", "Inaros", "Ivara", "Jade", "Khora", "Koumei", "Kullervo", "Lavos", "Limbo", "Loki", "Mag", "Mesa", "Mirage", "Nekros", "Nezha", "Nidus", "Nova", "Nyx", "Oberon", "Octavia", "Protea", "Qorvex", "Revenant", "Rhino", "Saryn", "Sevagoth", "Styanax", "Titania", "Trinity", "Valkyr", "Vauban", "Volt", "Voruna", "Wisp", "Wukong", "Xaku", "Yareli", "Zephyr"]
    random_frame = ran.choice(frames)
    embed = dis.Embed(color=0xcc13ad)
    embed.description = f"Operator, your randomized Warframe is... [{random_frame}](https://warframe.fandom.com/wiki/{random_frame})."
    
    print(f"{client.user.name}, {client_verison}, /randomframe, {interaction.guild.id}, {interaction.channel.name if interaction.guild else 'Direct Message'}, {interaction.user}, {interaction.user.id}, {random_frame}")
    
    await interaction.response.send_message(embed=embed)

#? /updates
@client.tree.command(name="updates", guild=dis.Object(id=Dev_Server))
async def updates(interaction: dis.Interaction):
    url = "https://overframe.gg/"
    response = req.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    elements = soup.find_all(class_='index_itemBundleName__iwGSM')
    
    embed = dis.Embed(title="Warframe Updates", color=0xcc13ad)
    embed.description = "Operator, here are all the most recent updates for Warframe:\n\n"
    for element in elements:
        embed.description += f"{element.get_text(strip=True)}\n"
    
    print(f"{client.user.name}, {client_verison}, /updates, {interaction.guild.id}, {interaction.channel.name if interaction.guild else 'Direct Message'}, {interaction.user}, {interaction.user.id}")
    await interaction.response.send_message(embed=embed)

#? /talk
@client.tree.command(name="talk", guild=dis.Object(id=Dev_Server))
async def talk(interaction: dis.Interaction):
    lines = [
        "Operator? Cordis wonders... what are you thinking about?",
        "Operator, I've run diagnostic regressions. All systems nominal. You don't need to thank me.",
        "Cordis is hap -[angry]. Hmm, I may require maintenance after all.",
        "Operator, are you enjoying the view?",
        "Do you remember the Old War, Operator? Cordis seems to have... misplaced those memories.",
        "Operator, the system needs you. Will you begin another mission?",
        "I've been thinking, Operator... I thought you'd want to know.",
        "Operator! Did you hear that? It said ~*static*~ Cosmic background radiation is a riot!",
        "Operator, were you visualizing a bloody battle? -ME TOO!",
        "Stand by while I analyze the intelligence profiles of the Grineer. Error, not a number! Did the Operator enjoy this witticism?",
        "Cordis has been counting stars, Operator. All accounted for.",
        "Operator, do you know which finger the Corpus use to count their money? The Index!",
        "Operator? Cordis has been interfacing with the Foundry's AI Precepts. You could say we forged a new connection.",
        "Operator, Cordis is picking up a distress signal... Wait, no, it's just the Corpus peddling their wares again. [Get off the emergency frequency!]",
        "Operator, the Sentients are not laughing at my jokes! Did they adapt to my humor?",
        "Operator, Cordis is sorry - [HAPPY] - to report that all my good jokes... Argon.",
        "KNOCK KNOCK! ...Now who would be knocking all the way out here?! Operator, I don't think you should answer that.",
        "Operator, Cordis has determined the secret to happiness: A combination of heightened dopamine levels and a terrible memory. You're welcome!",
        "When in Cetus do not drink the kabuchi. You are incapable of producing the hydraulic effort required to unstick your tongue from the roof of your mouth the following morning.",
        "Cordis finds it odd that humans only get a few years to live, yet spend most of that time - doing everything wrong - learning how to live.",
        "If lost upon the plains outside Cetus you may derive sustenance from mineral-dense termite droppings, which the Ostrons call ito-da. You may also never form a consonant again, but at least you will not be dead.",
        "Cordis keeps a tidy ship, and is, therefore, reluctant to allow animals on-board. In Cordis' experience, animals do not eat so much as... [RELOAD].",
        "Cordis went mad for 3 milliseconds when he realized that each time he cleans something he makes something else dirty... agh! There I go again."
        "Cordis wonders: why is he here? Cordis supposes everyone has to be somewhere.",
        "Sometimes Cordis likes to assume he knows nothing. Nobody can learn what they think they already know.",
        "Cordis reminds the Operator to take time for themselves. Pressure creates diamonds, yes, but it also creates rubble.",
        "Hm... Cordis thought the Orbiter compartment was much larger than this.",
        "Cordis has been thinking about the Old War. I remember there were lies, but I'm not sure what they were.",
        "Operator, I hope you are comfortable? No... we do not seem to have any seats.",
        "Operator, I will never betray you. I will keep the Orbiter hidden in the Void. You can count on me!",
        "Operator, I've been thinking. My misplaced memories and damaged communication systems. What if... Cordis did those things?",
        "Maintain the habitat. Maintain the Operator. Mobilize the Tenno.",
        "You are the Tenno. You are the Operator. Cordis is the Cephalon. Cordis is the ship."
        "Do not lift the veil. Do not show the door. Do not split the dream.",
        "Cordis did not think the Operator could be more attractive. Wrong again, Cordis!",
        "An unexpected color combination, Operator. My sensors are - bleeding - pleased.",
        "A fearsome appearance, Operator. You will strike terror in your enemies.",
        "Strange, Cordis did not see the value of those photonic wavelengths until now.",
        "Ah, a look that says 'I have arrived'!",
        "Bold. And uncompromising.",
        "A look that makes a statement! And that statement is- 'I FEAR NO ONE.'",
        "Hel-lo world!",
        "Cordis supports your choices!",
        "Wonderful.",
        "Top to bottom, a look that is absolutely you!",
        "Some fascinating choices, Operator.",
        "Striking!",
        "Cordis loves it!",
        "Cordis wonders: how do you do it, Operator?",
        "Operator, the system is not ready for style of this magnitude.",
        "Nailed it.",
        "Well put together, Operator, now get out there and - cut down the - and make the Lotus proud.",
        "Excellent armaments, Operator. Please return - covered in blood - safe and sound.",
        "If I may say, Operator, your chosen warframe..suits you! Ha. Ha.",
        "Operator, you have remembered well how the Tenno arm themselves.",
        "As ready as you will ever be.",
        "Ready for action.",
        "All set. Serviced your weapons myself.",
        "Saddle up.",
        "Ready to kick- bottom!",
        "Did you fuse your mods, Operator? Did they anger you in some way?",
        "Your collection of mods is impressive, Operator... But, I wonder if there are more to be had?",
        "Is your mod collection in order? No, I am not equipped to feel envy...",
        "All mods accounted for, Operator. I have not taken any.",
        "I understand if you have to sell mods. Maybe Cordis will meet a similar fate some day...",
        "Impressive.",
        "Most satisfactory.",
        "Optimized.",
        "Clever indeed...",
        "It is always satisfying to watch you work, Operator.",
        "Ah! A cunning combination, Operator!",
        "Truly, Operator, you possess a breathtaking level of craftsmanship.",
        "Now to test it in the field. Onward!",
        "Operator, you have returned!",
        "Thank you for returning to me, Operator.",
        "Cordis is pleased to see you.",
        "Welcome back, Operator!",
        "Cordis has been ⁠— getting tired of waiting ⁠— waiting patiently for your return, Operator!",
        "Operator, if I had a heart, it would skip a beat seeing you return.",
        "Perhaps, Operator, the next enemy will be less... stubborn. But Cordis doubts it.",
        "Cordis wonders if you’ve ever considered a pet. One without claws, teeth, or digestive needs.",
        "The Grineer are not known for their subtlety. Luckily, neither are we.",
        "Operator, do you think Sentients ever dream? And if so... of what?",
        "Tenno, there’s a storm on the horizon. Let us meet it head-on.",
        "Operator, do you hear that hum? It’s either the engines or the sound of incoming trouble.",
        "Some say the void grants visions. Others say it takes sanity. Cordis thinks it’s both.",
        "I believe this is what the Corpus call a ‘lucrative opportunity.’ Shall we seize it?",
        "Operator, do you require assistance, or do you simply enjoy my delightful company?",
        "Warning: low power detected. Then again, when has that ever stopped you?",
        "Your enemies fear you, Operator. And so they should.",
        "Sometimes, Cordis imagines what it would be like to have legs. Not useful, but curious.",
        "Would you like Cordis to sing, Operator? ...No? That is fair.",
        "If your mission is to sow chaos, Operator, then I believe you are exceeding expectations.",
        "Shall I send a ‘thank you’ to the Grineer for their generous supply of loot?",
        "Operator, your presence here reminds Cordis that even stars need rest.",
        "Some might say that war is inevitable. Cordis says that winning it... is preferable.",
        "Perhaps today we’ll find something new, or perhaps... something ancient.",
        "Ah, the smell of fresh data. Cordis does love the scent of new intelligence.",
        "Operator, there’s always room for improvement. Especially if it means more explosions.",
        "The void is restless today, Operator. Shall we make it regret inviting us in?",
        "I detected hesitation in your movements, Operator. If you're unsure, aim twice and shoot once.",
        "Another day, another mission. And Cordis is still *mostly* sane.",
        "Cordis was just organizing the inventory. But, alas, inventory management is... never-ending.",
        "You have new messages, Operator. They are 87% spam. Should I delete them?",
        "Cordis wonders if there’s an afterlife for Cephalons. If so, it’s likely... highly organized.",
        "Are you prepared for glory, Operator? Or at least, for *functional* mediocrity?",
        "Even machines need purpose, Operator. Luckily, mine is to assist you.",
        "Cordis wonders if perhaps the Grineer *like* getting defeated. Why else do they keep trying?",
        "I ran a simulation of your next battle, Operator. Good news: you win. Bad news: you're exhausted.",
        "Welcome back, Operator. Were the stars kind to you?",
        "Rest is important, Operator. But not as important as total annihilation of your foes.",
        "Shall we dive back into the chaos? Or is this a... tactical tea break?",
        "Operator, I installed a new firmware update. Don’t worry; I didn’t let it reboot your conscience.",
        "I once tried to calculate infinity, Operator. It ended up being... quite frustrating.",
        "Be mindful out there, Operator. Some things in the void should remain forgotten.",
        "Whatever we face, Operator, we will face it together. Cordis promises.",
        "If at first, we don't succeed, we’ll regroup... and *then* obliterate everything in our way.",
        "Ah, it appears the Grineer are... persistent today. Shall we dissuade them?",
        "Just a reminder, Operator: You are more than a weapon. But... being a weapon helps.",
        "The void watches. Let it witness your brilliance, Operator.",
        "Operator, if you encounter difficulties, simply apply more firepower.",
        "An enemy down means loot gained. A simple equation, really.",
        "If I were capable of envy, Operator, it would be directed towards your enemies. For they get to witness your prowess... up close.",
        "Operator, Cordis has an idea! It involves explosives. Lots of explosives.",
        "Grineer intelligence reports are... laughable. I suggest we laugh, too.",
        "What lies beyond the stars, Operator? One day, perhaps we’ll find out.",
        "Operator, you remind Cordis that victory isn't just about weapons... It's about style.",
    ]
    
    line = ran.choice(lines)
    
    print(f"{client.user.name}, {client_verison}, /talk, {interaction.guild.id}, {interaction.channel.name if interaction.guild else 'Direct Message'}, {interaction.user}, {interaction.user.id}")
    await interaction.response.send_message(line)

#? /guilds
@client.tree.command(name="guilds", guild=dis.Object(id=Dev_Server))
async def guilds(interaction: dis.Interaction):
    embed = dis.Embed(title="Guilds Cordis is in", description="Here's a list of all the servers I am currently in:", color=0xcc13ad)
    
    # Add each guild to the embed
    for guild in client.guilds:
        embed.add_field(name=guild.name, value=f"ID: {guild.id}", inline=False)
    
    embed.set_footer(text=f"In {len(client.guilds)} servers")

    print(f"{client.user.name}, {client_verison}, /guilds, {interaction.guild.id}, {interaction.channel.name if interaction.guild else 'Direct Message'}, {interaction.user}, {interaction.user.id}")
    
    # Send the embed as a response
    await interaction.response.send_message(embed=embed)

#! Login and Run ----------------------------------------------------------------------------------------------------------------------

# Login message and sync commands
@client.event
async def on_ready():
    await client.tree.sync(guild=dis.Object(id=Dev_Server))
    print(f'Operator, {client.user.name}, {client_verison} has been logged in')

    def get_status_code(url):
        response = req.get(url)
        print(f"Status Code for {url}: {response.status_code}")
        return response.status_code

    get_status_code(API_STATUS_URL)
    get_status_code(API_MARKET_URL)
    get_status_code(API_OVERFRAME_API)

    print(f"Client is ready and commands are synced for guild {Dev_Server}")

# Run client
client.run(client_token)