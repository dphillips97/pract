# python3
# quickWeather.py - Prints the weather for a location from the command line

import json, requests, sys

# Get location from command line arguments
if len(sys.argv) < 2:
	print('Usage: quickWeather.py location')
	sys.exit()

location = ' '.join(sys.argv[1:])
# 'default' api
api = ''

url = 'http://api.openweathermap.org/data/2.5/forecast?q=%s&appid=%s' % (location, api)
print("Contacting %s\n" % url)
response = requests.get(url)
response.raise_for_status()

#load json data into a python variable
weatherData = json.loads(response.text)

# Print current weather descriptions
w = weatherData['list']
print('Current weather in %s: ' % location)
print(w[0]['weather'][0]['main'], '-', w[0]['weather'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
