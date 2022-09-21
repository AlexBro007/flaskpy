import requests

city_id = "Moscow,RU"
apikey = 'adbe8370405f8eaee967007b6a516a59'

def get_weather(city_id, apikey):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_id}&appid={apikey}&units=metric'
    result = requests.get(url).json()
    return result



if __name__ == "__main__":
    data = get_weather(city_id, apikey)
    print(data)
