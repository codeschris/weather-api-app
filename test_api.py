import requests
api_key = 'your_api_key'

city = input('Enter city to check weather: ')
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    desc = data['weather'][0]['description']
    print("Temperature: {:.1f} Celcius".format(temp - 273.15))
    print(f'Description: {desc}')
    
    #storing JSON text in a .txt file for reference
    fo = open('storage_json.txt', 'w+')
    fo.write(str(data))
    fo.close()
else:
    print('Error fetching weather data')
