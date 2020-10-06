import requests
from pprint import pprint

import os

key = os.environ.get('WEATHER_KEY')
print(key)

#def main():
url = 'http://api.openweathermap.org/data/2.5/weather?'

city = input('Enter a city:  ')
country = input('Enter a country code - 2 letters:  ')
location = f'{city},{country}'

query = {'q':location, 'units': 'imperial', 'appid': key}

data = requests.get(url, params=query).json()

pprint(data)

temp = data['main']['temp']

print(f' The current temperature is {temp} F')

#if __name__ == '__main__':
 #   main()