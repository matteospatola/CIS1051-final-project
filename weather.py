import datetime
import requests
import weatherkey
import json



def get_weather(api_key, city_name):
    url =f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    return requests.get(url).json()
    #print(response)
    #print(json.dumps(response, indent=2)



def org_data():
    data = get_weather(weatherkey.api_key, input("What is your location: "))
    keys = ['weather', 'main', 'wind']

    for k,v in data.items():
        if k in keys:












org_data()







print(org_data())







