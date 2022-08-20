import requests

url = "https://10.10.20.1/cucm-uds/users"

payload={}
headers = {
  'Accept': 'application/xml',
  'Content-Type': 'application/xml',
  'Authorization': 'Basic YWRtaW5pc3RyYXRvcjpjaXNjb3BzZHQ=',
  'Cookie': 'JSESSIONID=E36FFB48A774A238B86981622D9C5CD4; JSESSIONIDSSO=C997ADD95DFFDCD0B1644AB8E3B2614C'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)



# users = xmldata['users']['user']
# for user in users:
#     print(f"{user['lastName']} {user['firstName']}")
#     print(f"ID: {user['id']}")
#     print(" ")