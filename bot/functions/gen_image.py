import discord
from PIL import Image, ImageDraw, ImageFont




async def gen_image(user_id: str , sorted_users: list , server_name: str , interaction: discord.Interaction , avatar_saved: bool):
  selected_user = {}
  user_position = 0

  for i, user in enumerate(sorted_users, start=1):
    if str(user_id) in user.values():
      selected_user = user
      user_position = i
      break
    else:
      pass

  user_events = selected_user['PointsHistory']

  image = Image.open("./images/background.png")
  if avatar_saved:
    avatar = Image.open("./images/avatar.png").resize((250 , 250))
  else:
    avatar = Image.open("./images/default_avatar.png").resize((250 , 250))

  image.paste(avatar , (1150-125 , 40))
  draw = ImageDraw.Draw(image)

  if len(interaction.user.name) > 15:
    font = ImageFont.truetype(font="/System/Library/Fonts/Supplemental/Arial.ttf", size=40)
  else:
    font = ImageFont.truetype(font="/System/Library/Fonts/Supplemental/Arial.ttf", size=60)

  bbox = draw.textbbox(xy=(1150 , 300) , text=interaction.user.name , font=font , align='center')
  text_width = bbox[2] - bbox[0]
  text_height = bbox[3] - bbox[1]

  draw.text(xy=(1150-(text_width/2) , 300) , text=interaction.user.name , fill=(255, 255, 255) , font=font , align='center')

  # Drawing server name:
  draw.text(xy=(40 , 20) , text=server_name , fill=(255, 255, 255) , font=ImageFont.truetype(font="arial.ttf" , size=80))

  # Drawing total points:
  draw.text(xy=(40 , 110) , text=f"Total Points: {selected_user['TotalPoints']}" , fill=(255, 195, 0) , font=ImageFont.truetype(font="arial.ttf" , size=50))

  # Drawing leaderboard rank:
  draw.text(xy=(40 , 170) , text=f"Leaderboard Rank: #{user_position}" , fill=(255, 195, 0) , font=ImageFont.truetype(font="arial.ttf" , size=50))

  # Drawing event heading:
  draw.text(xy=(40 , 270) , text="Events" , fill=(255, 255, 255) , font=ImageFont.truetype(font="arial.ttf" , size=80))

  selected_events_1 = user_events[:7]
  selected_events_2 = user_events[7:14]

  x = 40
  y = 360
  for event in selected_events_1:
    draw.text(xy=(x , y) , text=f"{event['Event Name']}: {event['Points']}" , fill=(255, 195, 0) , font=ImageFont.truetype(font="arial.ttf" , size=50))
    y += 60

  y = 360
  for event in selected_events_2:
    draw.text(xy=(700 , y) , text=f"{event['Event Name']}: {event['Points']}" , fill=(255, 195, 0) , font=ImageFont.truetype(font="arial.ttf" , size=50))
    y += 60


  image.save("./images/points.png")

  return "./images/points.png"






