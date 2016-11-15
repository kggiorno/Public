#! python3
# quickWeather.py - Prints the weather for a location from the command line.

import json, requests, sys

# Compute location from command line arguments.

if len(sys.argv) < 2:
	print('Usage: quickWeather.py location')
	sys.exit()
location = ' '.join(sys.argv[1:])

# Download JSON data from OpenWeather API

url ='http://api.openweathermap.org/data/2.5/forecast/city?q=%s&APPID=79ce3369ab7c30776e388afa23f24337' % location
response = requests.get(url)
response.raise_for_status()

# Load JSON data into a Python variable

weatherData = json.loads(response.text)

# Print Weather descriptions.

w = weatherData['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])