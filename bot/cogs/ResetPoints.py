# All modules here:
import discord, json
from discord import app_commands
from discord.ext import commands
from functions.gen_image import gen_image
from functions.check_user import check_user



# Our add command cog:
class ResetPoints(commands.Cog):
  def __init__(self , bot):
    self.bot = bot

  @app_commands.command()
  async def reset_points(self , interaction: discord.Interaction):
    if interaction.user.id == interaction.guild.owner_id:


      await interaction.response.send_message(content="**Please Wait Resetting Points!**")


      with open("./database/all_users.json" , "w") as file:
        json.dump([] , file)

      await interaction.edit_original_response(content="**Points Resetted Successfully!**")
    else:
      await interaction.response.send_message(content="**Nah! You Need To Be Owner To Use This Command!**")



# Our add command setup:
async def setup(bot):
  await bot.add_cog(ResetPoints(bot=bot))