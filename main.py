import requests



def checkWeather(id):
    weather = ""
    if(id>=200 and id<=299):
        weather = "Thunderstorm"
    elif (id>=300 and id<=399):
        weather = "Drizzle"
    elif (id>=500 and id<=599):
            weather = "Rain"
    elif (id>=600 and id<=699):
         weather="Snow"
    else: 
        weather=""

    return weather


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

# city_home = "Northbridge"
# state_home = "MA"
# country_home = "USA"

# city_work1 = "Merrimack"
# state_work1 = "NH"
# country_work1 = "USA"

# city_work2 = "Raynham"
# state_work2= "MA"
# country_work2 = "USA"

locations = ["Northbridge,MA,USA", "Merrimack,NH,USA", "Raynham,MA,USA"]

# weather_by_city_home = "https://api.openweathermap.org/data/2.5/weather?"
# parameters_home = {"q": parameters[0], "appid": api_key}
# response_home = requests.get(weather_by_city_home, params=parameters_home)
# response_home.raise__for_status()
# data_home = response_home.json()
# lat_home = data_home["coord"]["lat"]
# lon_home = data_home["coord"]["lon"]

# weather_by_city_work1 = "https://api.openweathermap.org/data/2.5/weather?"
# parameters_work1 = {"q": parameters[1], "appid": api_key}
# response_work1 = requests.get(weather_by_city_work1, params=parameters_work1)
# response_work1.raise_for_status()
# data_work1 = response_work1.json()
# lat_work1 = data_work1["coord"]["lat"]
# lon_work1 = data_work1["coord"]["lon"]

# weather_by_city_work2 = "https://api.openweathermap.org/data/2.5/weather?"
# parameters_work2 = {"q": parameters[2], "appid": api_key}
# response_work2 = requests.get(weather_by_city_work2, params=parameters_work2)
# response_work2.raise_for_status()
# data_work2 = response_home.json()
# lat_work2 = data_work2["coord"]["lat"]
# lon_work2 = data_work2["coord"]["lon"]




for location in locations: 
    weather_by_city = "https://api.openweathermap.org/data/2.5/weather?"
    parameters1 = {"q": location, "appid": api_key}
    response = requests.get(weather_by_city, params=parameters1)
    response.raise_for_status()
    data = response.json()
    lat = data["coord"]["lat"]
    lon = data["coord"]["lon"]

    weather_five_days = "https://api.openweathermap.org/data/2.5/forecast?"
    parameters2 = {"lat": lat, "lon": lat, "appid": api_key, "cnt": 4}
    response2 = requests.get(weather_five_days, params=parameters2)

    data2 = response2.json()
    id = data2["list"][0]["weather"][0]["id"]
    condition = data2["list"][0]["weather"][0]["description"]
    weather = checkWeather(id)
    msg = ""
    if (weather!=""):
         msg = f"Hello, Today there will be an occurrence of {weather} around {location} area, with the condition of {condition}. Please prepare for your day accordingly. Have a wonderfull day!"

    else:
         msg = f"Hello, No major weather update for today for {location}. Have a great day"

    print(msg)
    