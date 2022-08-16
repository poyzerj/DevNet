import requests
import json

target = "https://192.168.1.251:443/ins"
username = "admin"
password = "K1pe3kjt!"

requestheaders = {
  'Content-Type': 'application/json',
}


showcmd = {
  "ins_api": {
    "version": "1.0",
    "type": "cli_show",
    "chunk": "0",
    "sid": "sid",
    "input": "show ip interface brief",
    "output_format": "json"
  }
}

response = requests.post(
    target,
    data=json.dumps(showcmd),
    headers=requestheaders,
    auth=(username, password),
    verify=False
).json()

print(json.dumps(response, indent=2, sort_keys=True))
