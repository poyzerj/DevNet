import requests
import json

url = "https://192.168.1.250:443/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces"

payload={}
headers = {
  'Accept': 'application/yang-data+json',
  'Content-Type': 'application/yang-data+json',
  'Authorization': 'Basic Y2lzY286Y2lzY28='
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
