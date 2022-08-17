from urllib import response
import requests
import json
from pprint import pprint

switchuser = 'admin'
switchpassword = "K1pe3kjt!"

url = 'https://192.168.1.251/ins'

myheaders = {
    'content-type' : 'application/json'
}

payload = {
  "ins_api": {
    "version": "1.0",
    "type": "cli_show",
    "chunk": "0",
    "sid": "sid",
    "input": "show cdp neighbors",
    "output_format": "json"
  }
}

response = requests.post(url, data=json.dumps(payload), headers=myheaders, auth=(switchuser, switchpassword), verify=False).json
#print(response)

############################### LOGIN WITH NX-API REST

auth_url = "https://192.168.1.251/api/aaaLogin.json"

auth_body = {
  "aaaUser": {
    "attributes": {
      "name": "admin",
      "pwd": "K1pe3kjt!"
    }
  }
}


auth_response = requests.post(auth_url, data=json.dumps(auth_body), timeout=5, verify=False).json()
# pprint(auth_response)
token = auth_response['imdata'][0]['aaaLogin']['attributes']['token']
cookies = {}
cookies['APIC-cookie'] = token
# print(cookies)

counter = 0
nei_count = response['ins_api']['outputs']['output']['body']['neigh_count']
print(nei_count)

while counter < nei_count:
    hostname = ['ins_api']['outputs']['output']['body']['TABLE_cdp_neighbor_brief_info']['ROW_cdp_neighbor_brief_info'][counter]['device_id']
    local_int = ['ins_api']['outputs']['output']['body']['TABLE_cdp_neighbor_brief_info']['ROW_cdp_neighbor_brief_info'][counter]['intf_id']
    remote_int = ['ins_api']['outputs']['output']['body']['TABLE_cdp_neighbor_brief_info']['ROW_cdp_neighbor_brief_info'][counter]['port_id']

    body = {
        "l1PhysIf": {
            "attributes": {
                "descr": 'Connected to " '+hostname+' Remote interface is '+remote_int+'
            }
        }
    }
    counter += 1