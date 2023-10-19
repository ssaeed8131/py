import  discord
from discord.ext import commands
from discord import app_commands
from important.bot_token import TOKEN

# Setting all intents and making our bot:
bot_intents = discord.Intents.all()
my_bot = commands.Bot(command_prefix="!" , intents=bot_intents)

# Setting up our on ready event:
@my_bot.event
async def on_ready():
    print(f"The Bot Has Been Loaded.")
    print(f"Name: {my_bot.user.name}.\n")
    
    print("Loading All Cogs:")
    await my_bot.load_extension("cogs.Add")
    print("Loaded Add Cog!")
    await my_bot.load_extension("cogs.Leaderboard")
    print("Loaded Leaderboard Cog!")
    await my_bot.load_extension("cogs.Points")
    print("Loaded Points Cog!")
    await my_bot.load_extension("cogs.Refresh")
    print("Loaded Refresh Cog!")
    await my_bot.load_extension("cogs.ResetPoints")
    print("Loaded ResetPoints Cog!")


    await my_bot.tree.sync()


# Running our bot:
my_bot.run(TOKEN)