import requests
import json
import datetime
import os

url = "http://logtime-med.1337.ma/api/get_log"
payload = "{\"name\": \""
finish = "\", \"start_date\": \"\", \"end_date\": \"\"}"


os.system("users >> username.txt")
with open('username.txt','r') as file:
    readed = file.read()
os.system("rm -rf username.txt")

user = ""

for i in readed:
	if(i >= 'a' and i <= 'z' or i == '-'):
		user += i

payload += user
payload += finish

headers = {
  	'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data = payload)

hours = int((json.loads(response.text)['hydra:member'])[0]['totalHours'])

print(f"\033[1;32;40mYour total hours this month  : {hours}")

