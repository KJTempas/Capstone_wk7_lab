import os
import logging
import requests
from pprint import pprint
from datetime import datetime

#configuring the logger - tell it what file to write to, 
#what level of logging to record(DEBUG means everything), and
#format of string that is recorded for each log eveng
logging.basicConfig(filename='debug.log', level=logging.DEBUG, format=f'%(asctime)s - %(levelname)s - %(message)s')


key = os.environ.get('WEATHER_KEY')
url = 'http://api.openweathermap.org/data/2.5/forecast'

def main():
    location = get_location()
    forecast_data, error= get_forecast(location,key)
    if error:
        print('Sorry, could not get the forecast')
    else:
        show_forecast(forecast_data)
        


def get_location():
    city,country= '',''
    while len(city)==0:
        city = input('Enter the name of the city:  ').strip().title() #remove white spaces and make title case
    while len(country) !=2 or not country.isalpha():
        country = input('Enter the 2-letter country code:  ').strip().upper()
    location = f'{city},{country}'
    logging.info(f'User has entered valid location "{location}"')
    return location


def get_forecast(location,key):
    try:
        query= {'q': location, 'units': 'imperial', 'appid': key}
        response = requests.get(url, params=query)
        response.raise_for_status()  #will raise an exception for 400(client) or 500(server) errors
        forecast_data = response.json() #convert the response to json 
        logging.debug(f'response received from API and converted to JSON')
        return forecast_data, None
    
    except Exception as ex:
        logging.exception(f'Error requesting URL {url}')
        logging.info(ex)
        logging.info(response.text)
        return None,ex
        
def show_forecast(forecast_data):
    try:
        list_of_forecasts = forecast_data['list']
        for forecast in list_of_forecasts:   
            temp = forecast['main']['temp']
            timestamp = forecast['dt']
            forecast_date = datetime.fromtimestamp(timestamp)
            weather_description = forecast['weather'][0]['description']
            wind_speed = forecast['wind']['speed']
            print(f'At {forecast_date:%m-%d-%Y %H:%M}, the temperature will be {temp:.1f}F, the windspeed will be {wind_speed:.0f} mph, and the forecast is {weather_description}.')
        
    except KeyError:
        #print('This data is not in the format expected')  #change this to logging
        logging.exception(f' The data is not in the format expected - {forecast_data}')
        return 'Unknown'

    
if __name__ == '__main__':
    main()