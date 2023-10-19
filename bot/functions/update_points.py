# Modules here:
import json
from functions.check_user import check_user

# Main code here:
def update_points(user_id: str , points: int , event_name: str):

  with open(f"./database/all_users.json" , "r") as file:
    all_users = json.load(file)
    selected_user = {}


  for user in all_users:
    if str(user_id) in user.values():
      selected_user = user
      all_users.remove(user)
      break
    else:
      pass

  upd_points = selected_user['TotalPoints'] + points
  selected_user['TotalPoints'] = upd_points

  points_history = selected_user['PointsHistory']
  points_history.append({"Points": points , "Event Name": f"{event_name}"})
  selected_user['PointsHistory'] = points_history

  all_users.append(selected_user)

  with open(f"./database/all_users.json" , "w") as file:
    json.dump(all_users , file)

