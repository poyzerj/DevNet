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

###################### GET CLIENT HEALTH STATS #######################
url = "https://sandboxdnac.cisco.com/dna/intent/api/v1/client-health"

querystring = {
    "timestamp": ""
    }

headers = {
    'X-Auth-Token': token
}

response = requests.get(url, headers=headers, data=payload, params=querystring, verify=False).json()
# print(json.dumps(response, indent=2, sort_keys=True))

print(f"Clients: {response['response'][0]['scoreDetail'][0]['clientCount']}")

scores = response['response'][0]['scoreDetail']

for score in scores:
    if score['scoreCategory']['value'] == "WIRED":
        print(f"Wired Clients: {score['clientCount']}")
        score_values = score['scoreList']
        for score_value in score_values:
            print(f"   {score_value['scoreCategory']['value']}: {score_value['clientCount']}")
    elif score['scoreCategory']['value'] == "WIRELESS":
        print(f"Wireless Clients: {score['clientCount']}")
        score_values = score['scoreList']
        for score_value in score_values:
            print(f"   {score_value['scoreCategory']['value']}: {score_value['clientCount']}")
        