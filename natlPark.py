import os
import requests
import logging

#this file is for testing the natl parks api
key = os.environ.get('NATLPARKS_KEY')
url = 'https://developer.nps.gov/api/v1/parks'
logging.basicConfig(filename='degug.log', level=logging.DEBUG, format=f'%(asctime)s - %(name)s - %(levelname)s - %(message)s ')


def main():
    state = get_state()
    data = get_response(state)
    get_info(data)
    #results = get_info(data)
    #show_results(results)

def get_state():
    #make this a while loop
    state = input('Enter a two-letter state code  ')
    return state.upper()

def get_response(state):
    try:
        query= { 'stateCode': state, 'api_key': key}
        response = requests.get(url, params=query)
        response.raise_for_status()  #will raise an exception for 400(client) or 500(server) errors
        data = response.json() 
        return data
    except Exception as ex:
        logging.exception(ex)

def get_info(data):
    list_of_act = []
    list_of_parks = data['data']
    for park in list_of_parks: 
        parkName = park['fullName']  
        #description = park['description']
        lat = park['latitude']
        longitude = park['longitude']
        designation = park['designation']
        list_of_activities = park['activities']
        for activity in list_of_activities:
            act = activity['name']
            list_of_act.append(act)
              # get the first image - 
        #image_url = park['images'][0]
        #image_response = requests.get(image_url)
        #image_caption = park['images'][0]['caption']
        #with open('image.jgp', 'wb') as file:
         #   for chunk in image_response.iter_content():
          #      file.write(chunk)
           # file.write(image_caption)
        #image = park['images'][0]
        #results = (parkName, lat, longitude, designation, activities)
        #return results

#def show_results(results):
        print(f'{parkName}, a {designation}; a few activities {list_of_act[0:5]} Image caption: {image_caption} Location: latitude {lat} and longitude{longitude} \n')

if __name__ == '__main__':
    main()
