import requests
import pandas as pd

def extract_data(api_key,city,forecast_days,api_url):
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

    return df_hourly_forecast