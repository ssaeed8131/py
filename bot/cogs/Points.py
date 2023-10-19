# All modules here:
import discord, json
from discord import app_commands
from discord.ext import commands
from functions.gen_image import gen_image
from functions.check_user import check_user



# Our add command cog:
class Points(commands.Cog):
  def __init__(self , bot):
    self.bot = bot

  @app_commands.command()
  async def points(self , interaction: discord.Interaction):
    await interaction.response.defer()
    user_id = interaction.user.id
    avatar_saved = True
    selected_user = {}

    avatar_url = interaction.user.avatar
    try:
      await avatar_url.save("./images/avatar.png")
    except:
      avatar_saved = False

    user_exists = check_user(user_id=user_id , full_user=interaction.user)
    if user_exists:
      with open(f"./database/all_users.json" , "r") as file:
        all_users = json.load(file)

      sorted_users = sorted(all_users, key=lambda x: x['TotalPoints'], reverse=True)

      file_path = await gen_image(user_id=user_id , sorted_users=sorted_users , server_name=str(interaction.user.guild.name) , interaction=interaction , avatar_saved=avatar_saved)

      for user in all_users:
        if str(user_id) in user.values():
          selected_user = user
          break
        else:
          pass

      total_points = selected_user['TotalPoints']
      points_history = selected_user['PointsHistory']

      embed = discord.Embed(title=f"User Point Details:" , color=discord.Color.yellow())

      image = discord.File(file_path , filename="points.png")
      embed.set_image(url="attachment://points.png")

      await interaction.followup.send(embed=embed , file=image)
      return
    else:
      await interaction.followup.send(content="**Sorry! There Was An Error While Fetching Points.**")

    







# Our add command setup:
async def setup(bot):
  await bot.add_cog(Points(bot=bot))