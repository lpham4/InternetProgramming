import requests
import json

r = requests.get("http://api.openweathermap.org/data/2.5/forecast?id=4203696&APPID=651a9687c6af356f78b99978523b20db")
# city id 4203696
# api key 651a9687c6af356f78b99978523b20db
print(r)
print(r.status_code)
#print(r.status)
print(r.headers)
print(r.headers['date'])
#print(r.text)
