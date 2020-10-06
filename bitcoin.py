import requests
from pprint import pprint

coindesk_url = 'https://api.coindesk.com/v1/bpi/currentprice.json'

#powered by Coindesk
try:
    response = requests.get(coindesk_url)

    print(response.status_code)  #if in 200s - successful; see HTTP response codes
    print(response.json())
    response.raise_for_status() #raises an exception for 400 or 500 status code
    data = response.json() #convert response to json (like python dictionary)
    #print(data)
    pprint(data) #more easily readible
  
    dollars_exchange_rate = data['bpi']['USD']['rate_float']
    print(dollars_exchange_rate)
    #add validation
    bitcoin =float(input('Enter the number of bitcoins: '))
    bitcoin_value_in_dollars= bitcoin * dollars_exchange_rate
    print(f'$ {bitcoin_value_in_dollars} is the equivalent of {bitcoin} bitcoins')
    #add formatting w/ decimals
except Exception as e:
    print(e)
    print('There was an error making the request')