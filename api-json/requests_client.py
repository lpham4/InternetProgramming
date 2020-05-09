import requests
import json
from datetime import datetime

# send in request to API, with zipcode id, api id, and units as imperial
r = requests.get("http://api.openweathermap.org/data/2.5/weather?zip=30144,us&APPID=651a9687c6af356f78b99978523b20db&units=imperial")

# checking status of request
print("Status: ", r.status_code)
print()
# print request
print(r.headers)
print()
# response in json
data = r.json()
print()
# print out json
print(data)
print()
# extract and print contents from response
city = data['name']
print("City Name: ", city)
temp = data['main']['temp']
print("Current Temperature: ", temp, " degrees Fahrenheit")
pressure = data['main']['pressure']
print("Atmospheric Pressure: ", pressure, " hPa")
speed = data['wind']['speed']
print("Wind Speed: ", speed, " mph")
degree = data['wind']['deg']
print("Wind Direction: ", degree, " degrees")
dt = data['dt']
time = datetime.fromtimestamp(dt)
print("Time of Report: ", time)

