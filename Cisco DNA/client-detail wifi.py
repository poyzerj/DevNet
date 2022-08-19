import requests
import json

###################### LOGIN ########################################
url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"

payload={}
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='
}

response = requests.post(url, headers=headers, data=payload, verify=False).json()
# print(response)

token = response['Token']

###################### GET CLIENT DETAIL #######################
macAddress = 'ac:4a:56:6c:7c:00'
url = f"https://sandboxdnac.cisco.com/dna/intent/api/v1/client-detail?timestamp=&macAddress={macAddress}"

headers = {
    'X-Auth-Token': token
}

response = requests.get(url, headers=headers, data=payload, verify=False).json()
print(json.dumps(response, indent=2, sort_keys=True))

device_details = response['topology']['nodes']
for device_detail in device_details:
    if device_detail['id'] == device_details[0]['id']:
        print(f"Client IP: {device_detail['ip']}")
        print(f"MAC: {device_detail['id']}")
        print(f"Health Score: {device_detail['healthScore']}")
        print(" ")
    elif device_detail['id'] == device_details[2]['id']:
        print(f"Connected to {device_detail['deviceType']}")
        print(f"WAP IP {device_detail['ip']}")