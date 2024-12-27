from pyowm import OWM
from datetime import datetime

# Initialize PyOWM with your API key
owm = OWM("ea27f111bc09d056cd2c8772b2caa63b")
mgr = owm.weather_manager()

def extract_7_day_min_max_temps(lat, lon):
    # Fetch the 7-day forecast using the One Call API
    one_call = mgr.one_call(lat=lat, lon=lon)

    print(f"7-Day Weather Forecast with Min/Max Temperatures:\n")

    # Process daily data
    for daily in one_call.forecast_daily:
        date = datetime.utcfromtimestamp(daily.reference_time()).strftime('%Y-%m-%d')
        min_temp = daily.temperature('celsius')['min']
        max_temp = daily.temperature('celsius')['max']
        print(f"Date: {date}")
        print(f"  Min Temp: {min_temp}°C, Max Temp: {max_temp}°C\n")

# Example: Coordinates for Los Angeles, US
extract_7_day_min_max_temps(lat=34.052235, lon=-118.243683)
