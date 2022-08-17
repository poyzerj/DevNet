from pstats import SortKey
import requests
import json

url = "https://sandboxapicdc.cisco.com:443/api/aaaLogin.json"

payload = json.dumps({
  "aaaUser": {
    "attributes": {
      "name": "admin",
      "pwd": "!v3G@!4@Y"
    }
  }
})
headers = {
  'Content-Type': 'application/json',
}

response = requests.post(url, headers=headers, data=payload, verify=False).json()
print(json.dumps(response, indent=2, sort_keys=True))

token = response['imdata'][0]['aaaLogin']['attributes']['token']
cookie = {}
cookie['APIC-cookie'] = token
# print(cookie)

tenant_url = "https://sandboxapicdc.cisco.com:443/api/class/fvTenant.json"

tenant_response = requests.get(tenant_url, headers=headers, data=payload, cookies=cookie, verify=False).json()
print(json.dumps(tenant_response, indent=2, sort_keys=True))

#############  GET APN ###################
# GET APPLICATION PROFILE

url = "https://sandboxapicdc.cisco.com:443/api/node/mo/uni/tn-Heroes/ap-Save_The_Planet.json"

get_response = requests.get(url, headers=headers, cookies=cookie, verify=False).json()

print(json.dumps(get_response, indent=2, sort_keys=True))

#############  UPDATE APN DESCRIPTION ###################
# SET DESCRIPTION

post_payload = {
  "fvAp": {
    "attributes": {
      "descr": "",
      "dn": "uni/tn-Heroes/ap-Save_The_Planet"
    }
  }
}

post_response = requests.post(url, headers=headers, data=json.dumps(post_payload), cookies=cookie, verify=False).json()
print(json.dumps(post_response, indent=2, sort_keys=True))

get_response = requests.get(url, headers=headers, cookies=cookie, verify=False).json()
print(json.dumps(get_response, indent=2, sort_keys=True))