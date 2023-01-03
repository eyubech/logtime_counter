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

current_time = datetime.datetime.now()

today = current_time.day
left_day = 28 - today

print("\033[1;36;40m*"*22)

print(f"\033[1;32;40mYour total hours   : {hours}")

print(f"\033[1;31;40mleft days          : {left_day}")

print("\033[1;36;40m*"*22)
