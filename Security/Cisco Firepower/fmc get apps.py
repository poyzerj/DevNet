import json
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://fmcrestapisandbox.cisco.com"
login_url = '/api/fmc_platform/v1/auth/generatetoken'
headers = {
    'Content-Type': 'application/json'
}
user = 'poyzerj'
pw = '8YFuH97c'

login_response = requests.post(f'{url}{login_url}', auth=(user, pw), verify=False)
# Parse out the headers
resp_headers = login_response.headers
# Grab the token from the response headers
token = resp_headers.get('X-auth-access-token', default=None)
# Set the token in the headers to be used in the next call
headers['X-auth-access-token'] = token

apps_url = '/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/object/applications'
apps_response = requests.get(f'{url}{apps_url}', headers=headers, verify=False).json()

print(json.dumps(apps_response, indent=2, sort_keys=True))