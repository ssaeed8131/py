# Modules here:
import os
import json


# Main code here:
def check_user(user_id , full_user):
  with open(f"./database/all_users.json" , "r") as file:
    all_users = json.load(file)

  all_checked = True

  for user in all_users:
    if str(user_id) in user.values():
      all_checked = False
    else:
      pass

  new_user = {
    "UserName": full_user.name,
    "UserID": f"{user_id}",
    "TotalPoints": 0,
    "PointsHistory": []
  }
  if all_checked:
    all_users.append(new_user)

    with open(f"./database/all_users.json" , "w") as file:
      json.dump(all_users , file)

    return True
  else:
    return True