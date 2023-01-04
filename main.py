from datetime import date
import requests
import json
import os

today = date.today()
url = "http://logtime-med.1337.ma/api/get_log"
payload = "{\"name\": \""
payload2 = "{\"name\": \""
finish = "\", \"start_date\": \"" + str(today) + "\", \"end_date\": \"" + str(today) + "\"}"
finish2 = "\", \"start_date\": \"\", \"end_date\": \"\"}"
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
payload2 += user
payload2 += finish2

headers = {
  	'Content-Type': 'application/json'
}
response = requests.request("POST", url, headers=headers, data = payload)
response2 = requests.request("POST", url, headers=headers, data = payload2)
today_hours = int((json.loads(response.text)['hydra:member'])[0]['totalHours'])
total_hours = int((json.loads(response2.text)['hydra:member'])[0]['totalHours'])
from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%d")
print(f"\033[1;35;40mYour total hours for today       : {today_hours}")
print(f"\033[1;32;40mYour total hours for this month  : {total_hours}")
print(f"\033[1;33;40mLeft days                        : {28 - int(dt_string)}")