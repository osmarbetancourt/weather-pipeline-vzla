import requests
import os
from dotenv import load_dotenv
import logging
import pandas as pd

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
load_dotenv()

# Enviroment variables
api_key = os.getenv("WEATHER_API_KEY")
city = os.getenv("TARGET_CITY")
forecast_days = os.getenv("FORECAST_DAYS")
api_url = "https://api.weatherapi.com/v1/forecast.json"

if city:
    logging.info("The enviroment variables were loaded succesfully")
else:
    logging.warning("The enviroment variables weren't loaded")

print("Enviroment variables:",city,forecast_days)
params = {
    "key":api_key,
    "q":city,
    "days":forecast_days,
    "alerts":"no",
    "aqi":"no"
}

forecast_response = requests.get(url=api_url,params=params)
forecast_array = forecast_response.json()["forecast"]["forecastday"]

df_hourly_forecast = pd.json_normalize(
    data=forecast_array,
    record_path='hour',
)

print(df_hourly_forecast.columns)