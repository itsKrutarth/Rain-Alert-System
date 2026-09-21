import requests

api_key = "f3ba8a6851e81ce35debe52bf1d265f5"

"""
https://openweathermap.org/api/current?collection=current_forecast#name
Built-in API request by city name
You can call by city name or city name, state code and country code. Please note that searching by states available only for the USA locations.

API call
https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
Copy Icon
API call
https://api.openweathermap.org/data/2.5/weather?q={city name},{country code}&appid={API key}
Copy Icon
API call
https://api.openweathermap.org/data/2.5/weather?q={city name},{state code},{country code}&appid={API key}
"""

city = input("Please enter your city: ")
state = input("Please enter the state: ")
country = input("Please enter you country code: ")

weather_by_city = "https://api.openweathermap.org/data/2.5/weather?"
parameters = {"q": f"{city},{state},{country}", "appid": api_key}
response = requests.get(weather_by_city, params=parameters)
data_city = response.json()
lat = data_city["coord"]["lat"]
lon = data_city["coord"]["lon"]

weather_five_days = "https://api.openweathermap.org/data/2.5/forecast?"
parameters = {"lat": lat, "lon": lon, "appid": api_key}
response = requests.get(weather_five_days, params=parameters)
print(response.json())