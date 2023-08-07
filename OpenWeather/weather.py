import requests
from config import WEATHER_API_KEY

BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'

def get_weather(city_name):
    complete_url = BASE_URL + "q=" + city_name + "&appid=" + WEATHER_API_KEY
    response = requests.get(complete_url) 
    data = response.json() 

    if data["cod"] != "404":
        main_data = data["main"]
        weather_data = data["weather"][0]
        
        temperature = main_data["temp"] - 273.15  # Convert from Kelvin to Celsius
        pressure = main_data["pressure"]
        humidity = main_data["humidity"]
        weather_description = weather_data["description"]

        print(f"Weather in {city_name}:")
        print(f"Temperature: {temperature:.2f}°C")
        print(f"Pressure: {pressure} hPa")
        print(f"Humidity: {humidity}%")
        print(f"Description: {weather_description.capitalize()}\n")
    else:
        print("City Not Found!")

if __name__ == "__main__":
    city_name = input("Enter city name: ")
    get_weather(city_name)
