import requests

#data = requests.get('https://catfact.ninja/fact').json()
#print(data)
try:
    response = requests.get('https://catfact.ninja/fact')

    print(response.status_code)  #if in 200s - successful; see HTTP response codes
    print(response.text)
    print(response.json())
    response.raise_for_status() #raises an exception for 400 or 500 status code
    data = response.json()
    fact = data['fact']
    print(f'A random cat fact is : {fact}')

except Exception as e:
    print(e)
    print('There was an error making the request')