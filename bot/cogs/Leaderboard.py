# All modules here:
import discord, json, time
from discord import app_commands
from discord.ext import commands
from functions.check_user import check_user
from functions.update_points import update_points



# Our add command cog:
class Leaderboard(commands.Cog):
  def __init__(self , bot):
    self.bot = bot

  @app_commands.command()
  async def leaderboard(self , interaction: discord.Interaction):
    await interaction.response.defer()
    with open(f"./database/all_users.json" , "r") as file:
      leaderboard = json.load(file)

    embed = discord.Embed(title=f"```{(self.bot.user.name).upper()}``` | **Leaderboard**" , description=f"Top {len(leaderboard)}/{len(interaction.guild.members)} Ranking:" , color=discord.Color.yellow())

    sorted_data = sorted(leaderboard, key=lambda x: x['TotalPoints'], reverse=True)

    # Print the top 5 dictionaries
    for i, item in enumerate(sorted_data, start=1):
      embed.add_field(name=f"`#{i} • {item['UserName']} • {item['TotalPoints']} Points`" , value="" , inline=False)
                        
    message = await interaction.followup.send(embed=embed)

    

# Our add command setup:
async def setup(bot):
  await bot.add_cog(Leaderboard(bot=bot))