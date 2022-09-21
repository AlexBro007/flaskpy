import requests

import api_weather

city_id = "Moscow,RU"
apikey = api_weather.OPEN_WEATHER_API

def get_weather(city_id, apikey):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_id}&appid={apikey}&units=metric'
    result = requests.get(url).json()
    return result



if __name__ == "__main__":
    data = get_weather(city_id, apikey)
    print(data)
