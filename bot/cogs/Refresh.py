# All modules here:
import discord, json, time
from discord import app_commands
from discord.ext import commands
from functions.check_user import check_user
from functions.update_points import update_points



# Our add command cog:
class Refresh(commands.Cog):
  def __init__(self , bot):
    self.bot = bot

  @app_commands.command()
  async def refresh(self , interaction: discord.Interaction , message_id: str , channel_id: str):
    # await interaction.response.defer()
    try:

      with open(f"./database/all_users.json" , "r") as file:
        leaderboard = json.load(file)

      embed = discord.Embed(title=f"```{(self.bot.user.name).upper()}``` | **Leaderboard**" , description=f"Top {len(leaderboard)}/{len(interaction.guild.members)} Ranking:" , color=discord.Color.yellow())

      sorted_data = sorted(leaderboard, key=lambda x: x['TotalPoints'], reverse=True)

      # Print the top 5 dictionaries
      for i, item in enumerate(sorted_data, start=1):
        embed.add_field(name=f"`#{i} • {item['UserName']} • {item['TotalPoints']} Points`" , value="" , inline=False)

      channel = self.bot.get_channel(int(channel_id))
      message = await channel.fetch_message(int(message_id))

      await message.edit(embed=embed)
      await interaction.followup.send("**Message Have Been Edited Successfully.**")
    except:
      await interaction.followup.send("**There Was An Error In Your Message Or Channel ID.**")





# Our add command setup:
async def setup(bot):
  await bot.add_cog(Refresh(bot=bot))