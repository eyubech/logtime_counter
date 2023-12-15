from datetime import date, timedelta
from datetime import datetime
import requests
import json
import os

today = date.today()
url = "https://logtime-med.1337.ma/api/get_log"
user = os.popen("users").read().strip()

first_day_of_current_month = today.replace(day=1)
last_day_of_last_month = first_day_of_current_month - timedelta(days=1)
start_date = last_day_of_last_month.replace(day=29)
end_date = today.replace(day=28)


payload = f'{{"login": "{user}", "startDate": "{today}T00:00:00.000Z", "endDate": "{today}T23:59:59.999Z"}}'
payload2 = f'{{"login": "{user}", "startDate": "{start_date}T00:00:00.000Z", "endDate": "{end_date}T23:59:59.999Z"}}'


headers = {
  	'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data = payload)
response2 = requests.request("POST", url, headers=headers, data = payload2)
today_hours = int((json.loads(response.text)['hydra:member'])[0]['totalHours'])
total_hours = int((json.loads(response2.text)['hydra:member'])[0]['totalHours'])
now = datetime.now()
dt_string = now.strftime("%d")

data = os.popen("who").read().strip()
components =  data.split()
month = components[2]
day = int(components[3])
time_str = components[4]
current_datetime = datetime.now()
parsed_datetime = datetime(current_datetime.year, datetime.strptime(month, '%b').month, day)
parsed_time = datetime.strptime(time_str, '%H:%M')
parsed_datetime += timedelta(hours=parsed_time.hour, minutes=parsed_time.minute)
time_difference = current_datetime - parsed_datetime
hours_difference = time_difference.total_seconds() / 3600

logtime_header = '\033[95m' + '''
.__                 __  .__                
|  |   ____   _____/  |_|__| _____   ____  
|  |  /  _ \\ / ___\\   __\\  |/     \\_/ __ \\ 
|  |_(  <_> ) /_/  >  | |  |  Y Y  \\  ___/ 
|____/\\____/\\___  /|__| |__|__|_|  /\\___  >
           /_____/               \\/     \\/
''' + '\033[0m'

print(logtime_header)

green_color = '\033[92m'
yellow_color = '\033[93m'
red_color = '\033[91m'
reset_color = '\033[0m'
brown_color = '\033[33m'
orange_color = '\033[38;5;208m'


print(f"{green_color}\tYour total hours for today       : {today_hours}\t\tafter logout ~  [{int(hours_difference + today_hours)}]{reset_color}")
print(f"{yellow_color}\tYour total hours for this month  : {total_hours}\t\tafter logout ~  [{int(hours_difference + total_hours)}]{reset_color}")



if (28 - int(dt_string) > 11) : 
    color = brown_color
if (28 - int(dt_string) >= 10):
	color = orange_color
else:
	color = red_color


est = (120 - total_hours) / (28 - int(dt_string))

if (28 - int(dt_string) > 0 and est > 0) :
	print(f"{color}\tLeft days                        : {28 - int(dt_string)}\t\tEstimated[{est:.1f}h/d] {reset_color}")
else : 
	print(f"{color}\tCHIPI CHIPI CHAPA CHAPA DUBI DUBI{reset_color}")

try :
	print(f"")
	ads_content = os.popen("curl -s https://raw.githubusercontent.com/eyubech/logtime_counter/master/data").read().strip()
	print(f"\033[95m\tAds section [{ads_content}]{reset_color}")
	print(f"")
	print(f"\t \033[95m< To put ur ads here please contact [aech-che] >{reset_color}")
except:
	print(f"\033[95m\tAds section [Not available]{reset_color}")