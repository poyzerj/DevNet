import requests
import json

# Get your token here after loggin in: https://developer.webex.com/docs/getting-started
token = 'NWNkYTI0NzItOTdhMi00ZjAxLTg1OGQtYWEwYWZlNTQ0YzM0YTM0YzZiZmQtMDk0_P0A1_ca0eddbe-7060-445d-9128-1246a8ac7a49'

### Create a Team ###
url = "https://api.ciscospark.com/v1/teams"
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

body = {
    "name" : "Joe's Team"
}

# post_response = requests.post(url, headers=headers, data=json.dumps(body)).json()
# print(post_response)

get_response = requests.get(url, headers=headers).json()
#print(json.dumps(get_response, indent=2, sort_keys=True))
teams = get_response['items']
for team in teams:
    if team['name'] == "Joe's Team":
        teamId = team['id']

###### CREATE A ROOM #########
room_url = 'https://api.ciscospark.com/v1/rooms'
room_body = {
    "title": "Joe's Room",
    "teamId": teamId
}

# room_post = requests.post(room_url, headers=headers, data=json.dumps(room_body)).json()
#print(room_post)

get_rooms = requests.get(room_url, headers=headers).json()
rooms = get_rooms['items']
for room in rooms:
    if room['title'] == "Joe's Room":
        roomId = room['id']

##### POST A MESSAGE TO THE ROOM ######
msg_url = 'https://api.ciscospark.com/v1/messages'
msg_body = {
    "roomId": roomId,
    "text": "ALERT: Interface on device XYZ is down!"
}

msg_response = requests.post(msg_url, headers=headers, data=json.dumps(msg_body)).json()
print(msg_response)