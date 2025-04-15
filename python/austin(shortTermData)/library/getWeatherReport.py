#uses a API key to get a json of the openweathermap

import requests
import customModules.jsonSearch

def get_weather_report():
    weather_api = customModules.jsonSearch.search_keys_in_json_files("path/to/apiKey.json", "WeatherAPIKeys", "apiKey")
    rest = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api}&units=metric").json()
    weather = rest["weather"][0]["main"]
    temperature = rest["main"]["temp"]
    feels = rest["main"]["feels_like"]
    return weather, f"{temperature}℃", f"{feels}℃"