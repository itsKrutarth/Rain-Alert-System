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

city_home = "Northbridge"
state_home = "MA"
country_home = "USA"

city_work1 = "Merrimack"
state_work1 = "NH"
country_work1 = "USA"

city_work2 = "Raynham"
state_work2= "MA"
country_work2 = "USA"

weather_by_city_home = "https://api.openweathermap.org/data/2.5/weather?"
parameters_home = {"q": f"{city_home},{city_home},{city_home}", "appid": api_key}
response_home = requests.get(weather_by_city_home, params=parameters_home)
data_home = response_home.json()
lat_home = data_home["coord"]["lat"]
lon_home = data_home["coord"]["lon"]

weather_by_city_work2 = "https://api.openweathermap.org/data/2.5/weather?"
parameters_work2 = {"q": f"{city_work2},{city_work2},{city_work2}", "appid": api_key}
response_work2 = requests.get(weather_by_city_work2, params=parameters_work2)
data_work2 = response_home.json()
lat_work2 = data_work2["coord"]["lat"]
lon_work2 = data_work2["coord"]["lon"]

weather_by_city_work1 = "https://api.openweathermap.org/data/2.5/weather?"
parameters_work1 = {"q": f"{city_work1},{city_work1},{city_work1}", "appid": api_key}
response_work1 = requests.get(weather_by_city_work1, params=parameters_work1)
data_work1 = response_work1.json()
lat_work1 = data_work1["coord"]["lat"]
lon_work1 = data_work1["coord"]["lon"]

weather_five_days = "https://api.openweathermap.org/data/2.5/forecast?"
parameters = {"lat": lat_home, "lon": lon_home, "appid": api_key, "cnt": 4}
response = requests.get(weather_five_days, params=parameters)
print(response.json())