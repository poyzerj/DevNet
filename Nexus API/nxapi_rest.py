import requests
import json
from pprint import pprint

url = "https://192.168.1.251/api/aaaLogin.json"

payload = json.dumps({
  "aaaUser": {
    "attributes": {
      "name": "admin",
      "pwd": "K1pe3kjt!"
    }
  }
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Basic YWRtaW46SzFwZTNranQh',
  'Cookie': 'APIC-cookie=19WrEDKfROII9LeWuufMzAoTitNHUnjJ9BI6FQwH/KRRiKPIinFdBSo8XRYWbsUUB8ewkuoUQWDwQkrBtQwyQjFcF5VSvVVGlykP+KkZwe8kZZV9QpeEw53YOo7hxrcbRGM/ptANcyQTRldf+LE/TLXbEMucnXLJnI37LI0zzsk=; nxapi_auth=dzqnf:Cfc39MOIFSJumalGS3VVU0+jlQU='
}

response = requests.post(url, headers=headers, data=payload, verify=False).json()
# pprint(response)

token = response['imdata'][0]['aaaLogin']['attributes']['token']
# print(token)

cookies = {}
cookies['APIC-cookie'] = token

url = "https://192.168.1.251/api/node/mo/sys/intf/phys-[eth1/33].json"

payload = json.dumps({
  "l1PhysIf": {
    "attributes": {
      "descr": "Python Demo."
    }
  }
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Basic YWRtaW46SzFwZTNranQh',
}

put_response = requests.put(url, headers=headers, data=payload, cookies=cookies, verify=False).json

pprint(put_response)