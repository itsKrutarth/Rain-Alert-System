import requests
from datetime import datetime

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

api_key = "f3ba8a6851e81ce35debe52bf1d265f5"


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

def military_to_standard(military_time_str):
    # %H = 24-hour, %M = minutes, %S = seconds
    time_obj = datetime.strptime(military_time_str, "%H:%M:%S")
    
    # %I = 12-hour, %M = minutes, %S = seconds, %p = AM/PM
    return time_obj.strftime("%I:%M:%S %p")

def getForecast(locations, user):
    msg1 = f"Hello, {user}"
    print(msg1)
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
        date_text = data2["list"][0]["dt_txt"].split()

        time = military_to_standard(date_text[1])
        weather = checkWeather(id)
        
        if (weather!=""):
            msg2 = f"\n Today there will be an occurrence of {weather} around {location} area, with the condition of {condition}, around {time}. Please prepare for your day accordingly. Have a wonderfull day!"

        else:
            msg2 = f"\n No major weather update for today for {location}. Have a great day"

        print(msg2)



Krutarth = ["Northbridge,MA,USA", "Lowell,MA,USA", "Merrimack,NH,USA"]
Janki = ["Northbridge,MA,USA", "Franklin,MA,USA", "Raynham,MA,USA"]

getForecast(Krutarth, "Krutarth")
getForecast(Janki, "Janki")


    