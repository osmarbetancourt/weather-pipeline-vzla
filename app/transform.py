import pandas as pd

def transform_data(df_hourly_forecast):

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
    
    return df_hourly_forecast