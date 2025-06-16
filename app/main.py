import os
from dotenv import load_dotenv
import logging
import pandas as pd
from extract import extract_data
from transform import transform_data
from load import load_data

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
load_dotenv()

# Enviroment variables
api_key = os.getenv("WEATHER_API_KEY")
city = os.getenv("TARGET_CITY")
forecast_days = os.getenv("FORECAST_DAYS")
api_url = "https://api.weatherapi.com/v1/forecast.json"

# Validating the enviroment variables
if city:
    logging.info("The enviroment variables were loaded succesfully")
else:
    logging.warning("The enviroment variables weren't loaded")

df_hourly_forecast = extract_data(api_key,city,forecast_days,api_url)
df_hourly_forecast = transform_data(df_hourly_forecast)
load_data(df=df_hourly_forecast,table_name="hourly_weather_forecast")