import requests
import json

token = 'NWNkYTI0NzItOTdhMi00ZjAxLTg1OGQtYWEwYWZlNTQ0YzM0YTM0YzZiZmQtMDk0_P0A1_ca0eddbe-7060-445d-9128-1246a8ac7a49'

### DELETE ROOM ###
room_url = 'https://api.ciscospark.com/v1/rooms'
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'}


get_rooms = requests.get(room_url, headers=headers).json()

rooms = get_rooms['items']
for room in rooms:
    if room['title'] == "Fusion Team 2":
        roomId = room['id']
del_room_url = f'{room_url}/{roomId}'
del_room = requests.delete(del_room_url, headers=headers)


####### DELETE TEAM ##############
url = 'https://api.ciscospark.com/v1/teams'

get_response = requests.get(url, headers=headers).json()

teams = get_response['items']
for team in teams:
    if team['name'] == "Fusion Team 2":
        teamId = team['id']
del_team_url = f'{url}/{teamId}'
del_team = requests.delete(del_team_url, headers=headers)