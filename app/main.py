import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Enviroment variables
api_key = os.getenv("WEATHER_API_KEY")
city = os.getenv("TARGET_CITY")
forecast_days = os.getenv("FORECAST_DAYS")
api_url = "https://api.weatherapi.com/v1/forecast.json"

params = {
    "key":api_key,
    "q":city,
    "days":forecast_days,
    "alerts":"no",
    "aqi":"no"
}

forecast_response = requests.get(url=api_url,params=params)

print(forecast_response.json())
