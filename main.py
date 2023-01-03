import requests
import json
import datetime


url = "http://logtime-med.1337.ma/api/get_log"
payload = "{\"name\": \""
finish = "\", \"start_date\": \"\", \"end_date\": \"\"}"

print("")
user = str(input("user : "))

print("")
user = "aech-che"


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
left_hours = 120 - hours

print(f"Your total hours : {hours}")

print(f"Your need {left_hours} hours")

print(f"left days : {left_day}")

print(f"~= {left_hours / left_day} hours per day")

print("")