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

# Validating the enviroment variables
if city:
    logging.info("The enviroment variables were loaded succesfully")
else:
    logging.warning("The enviroment variables weren't loaded")

params = {
    "key":api_key,
    "q":city,
    "days":forecast_days,
    "alerts":"no",
    "aqi":"no"
}

# Request to get the forecast from the weather API
forecast_response = requests.get(url=api_url,params=params)
forecast_array = forecast_response.json()["forecast"]["forecastday"]

# Normalizing the JSON, we only need the hourly records for our DB
df_hourly_forecast = pd.json_normalize(
    data=forecast_array,
    record_path='hour',
)

# Selecting only columns with international measures and applicable to Venezuela
columns_to_select_from_raw_output = [
    'time_epoch', 'time', 'temp_c',
    'is_day', 'wind_kph', 'wind_degree', 'wind_dir',
    'pressure_mb', 'precip_mm', 'will_it_rain', 'chance_of_rain',
    'vis_km', 'uv', 'humidity', 'cloud',
    'feelslike_c', 'windchill_c', 'heatindex_c', 'dewpoint_c',
    'gust_kph', 'condition.text', 'condition.code'
]

# Cleaning the data
df_hourly_forecast = df_hourly_forecast[columns_to_select_from_raw_output]

# Renaming the 
rename_map = {
    'condition.text': 'condition_text',
    'condition.code': 'condition_code',
}
df_hourly_forecast = df_hourly_forecast.rename(columns=rename_map)

df_hourly_forecast.info()