import requests
import json
import urllib3
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Set URL and login body
# Note the body is a python dict - NOT a JSON body
url = "https://sandbox-sdwan-2.cisco.com:443/j_security_check"
login_body = {
    'j_username': 'devnetuser',
    'j_password': 'RG!_Yw919_83'
}

# MUST use a session for SD-WAN
session = requests.session()

response = session.post(url, data=login_body, verify=False)

# print(response)

# Response returns a 200 OK no matter what
# If the response body contains any text then auth failed

if not response.ok or response.text:
    print('Login failure')
    import sys
    sys.exit(1)
else:
    print('Login worked! Yay!')

# Get Devices
url = "https://sandbox-sdwan-2.cisco.com:443/dataservice/device"

device_response = session.get(url, verify=False).json()['data']
print(device_response)
for device in device_response:
    print(f"Hostname: {device['host-name']}")
    print(f"IP: {device['local-system-ip']}")
    print(f"Model: {device['device-model']}")
    print(' ')

