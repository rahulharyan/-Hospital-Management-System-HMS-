import requests
api_key='4be5c277cc93562237fdffef3c8e8218'

weather_api='https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}'



weather_data=requests.get(f'https://api.openweathermap.org/data/2.5/weather?q=bangalore&appid={api_key}')

print(weather_data.json())