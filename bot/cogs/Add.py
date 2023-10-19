# All modules here:
import discord, json
from discord import app_commands
from discord.ext import commands
from functions.check_user import check_user
from functions.update_points import update_points



# Our add command cog:
class Add(commands.Cog):
  def __init__(self , bot):
    self.bot = bot

  @app_commands.command()
  async def add(self , interaction: discord.Interaction , user: discord.User , points: int , event_name: str):
    await interaction.response.defer()

    user_id = user.id
    role = discord.utils.get(interaction.guild.roles, name="Event Host")
    if role in interaction.user.roles:
      folder_exist = check_user(user_id=user_id , full_user=user)
      if folder_exist:
        update_points(user_id=user_id , points=points , event_name=event_name)
        embed = discord.Embed(title="Points Update" , description=f"{points} Points Have Been Added Successfuly For {user.mention}." , color=discord.Color.yellow())
        await interaction.followup.send(embed=embed)
      else:
        await interaction.followup.send(content="**Sorry! There Was An Error While Adding The Points.**")
    else:
      await interaction.followup.send(content="**Sorry! You Don't Have The Required Role To Use this Command.**")

# Our add command setup:
async def setup(bot):
  await bot.add_cog(Add(bot=bot))