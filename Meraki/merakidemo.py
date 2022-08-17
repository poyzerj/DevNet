from pstats import SortKey
import requests
import json

url = "https://api.meraki.com/api/v1/organizations"

payload={}
headers = {
  'X-Cisco-Meraki-API-Key': '0ffea45ee6b641aea823e78025264061e955b802'
}

response = requests.get(url, headers=headers, data=payload, verify=False).json()

print(json.dumps(response, indent=2, sort_keys=True))

for response_org in response:
  if response_org["name"] == "DevNet Sandbox":
    orgId = response_org["id"]
print(orgId)

net_url = f"https://api.meraki.com/api/v0/organizations/{orgId}/networks"
networks = requests.get(net_url, headers=headers, data=payload, verify=False).json()

print(json.dumps(networks, indent=2, sort_keys=True))

for network in networks:
  if network['name'] == "Cisco Meraki Test LAB Noa":
    netId = network['id']
print(netId)

vlan_url = f'https://api.meraki.com/api/v1/networks/{netId}/appliance/vlans'
vlans = requests.get(vlan_url, headers=headers, data=payload, verify=False).json()
print(json.dumps(vlans, indent=2, sort_keys=True))

# for vlan in vlans:
#   if vlan['name'] == "Default":
#     vlanId = vlan['id']
# print(vlanId)

# vlan1_url = f'https://api.meraki.com/api/v1/networks/{netId}/appliance/vlans{vlanId}'
# vlan1body = {
#     "name": "My VLAN",
#     "applianceIp": "192.168.1.2",
#     "subnet": "192.168.1.0/24",
#     "groupPolicyId": "101",
#     "fixedIpAssignments": {
#         "22:33:44:55:66:77": {
#             "ip": "1.2.3.4",
#             "name": "Some client name"
#         }
#     },
#     "reservedIpRanges": [
#         {
#             "start": "192.168.1.0",
#             "end": "192.168.1.1",
#             "comment": "A reserved IP range"
#         }
#     ],
#     "dnsNameservers": "google_dns",
#     "dhcpHandling": "Run a DHCP server",
#     "dhcpLeaseTime": "1 day",
#     "dhcpBootOptionsEnabled": False,
#     "dhcpBootNextServer": "1.2.3.4",
#     "dhcpBootFilename": "sample.file",

# }
# update_vlan = requests.put(vlan1_url, headers=headers, data=vlan1body, verify=False).json()
# print(json.dumps(update_vlan, indent=2, sort_keys=True))