import requests
import os
from dotenv import load_dotenv, dotenv_values
load_dotenv() 

def weather_checker():
    print("\n=== Weather Checker ===")
    city = input("Enter the city name: ")
    api_key="48733f7654aeed178c014c5290e33db0"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()
        if data["cod"] == 200:
            print(f"Weather in {city}:")
            print(f"Temperature: {data['main']['temp']}°C")
            print(f"Condition: {data['weather'][0]['description']}")
        else:
            print(f"Error: {data['message']}")
    except Exception as e:
        print("Failed to retrieve weather data. Please check your internet connection.")
