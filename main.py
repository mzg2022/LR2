from own_key import owm_api_key
import json
import requests


def get_weather_data(place, APIKey=None):
    URL = "http://api.openweathermap.org/data/2.5/weather?"
    response = requests.get(f"{URL}appid={APIKey}&q={place}")
    result_json = response.json()
    time = result_json['timezone'] // 3600

    data = {
        'name': result_json['name'],
        'coord': result_json['coord'],
        'country': result_json['sys']['country'],
        'feels_like': result_json['main']['feels_like'],
        'timezone': f'UTC+{time}'
    }

    with open('all_data.json', 'w') as f:
        json.dump(result_json, f, ensure_ascii=False, indent=4)

    with open('data.json', 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    with open('data.json', 'r') as r:
        print(json.load(r))


if __name__ == '__main__':
    get_weather_data('Moscow', APIKey=owm_api_key)
