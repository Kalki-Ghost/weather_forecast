
from datetime import datetime, timedelta

import pyowm
import streamlit as st
from matplotlib import pyplot as plt

owm = pyowm.OWM("ea27f111bc09d056cd2c8772b2caa63b")
mgr = owm.weather_manager()


st.title("7 Day Weather Forecast")
st.write("###Write the name of a City and selected Temperature Unit and Graph Type from the sidebar")
place = st.text_input("NAME OF THE CITY:", "")
unit = st.selectbox("Select Temperature Unit", ("Celsius", "Fahrenheit"))
g_type = st.selectbox("Select Graph Type", ("Line Graph", "Bar Graph"))


def extract_data():
    forecast_by_day = {}
    for weather in forecast.forecast:
        date = datetime.utcfromtimestamp(weather.reference_time()).date()
        if date not in forecast_by_day:
            forecast_by_day[date] = []
        forecast_by_day[date].append(weather)

    # Extract today's date
    today = datetime.utcnow().date()

    # Process Today + 5 Future Days
    temp_min = []
    temp_max = []
    days = []
    for i in range(7):  # Today + Next 5 Days
        day = today + timedelta(days=i)
        if day in forecast_by_day:
            temps = [w.temperature('celsius' if unit == "Celsius" else 'fahrenheit')['temp']
                     for w in forecast_by_day[day]]
            temp_min.append(min(temps))
            temp_max.append(max(temps))
            days.append(day)
    return days, temp_min, temp_max


def line_graph(days, temp_min, temp_max, unit):
    fig, ax = plt.subplots()
    ax.plot(days, temp_min)
    ax.plot(days, temp_max)
    ax.set_xlabel('Days')
    ax.set_ylabel("°"+unit)
    st.pyplot(fig)


def bar_graph(dates, temp_min, temp_max, unit):
    fig, ax = plt.subplots()
    ax.bar(dates, temp_min, label="Min Temp", color='blue', alpha=0.7)
    ax.bar(dates, temp_max, label="Max Temp", color='red', alpha=0.7)
    ax.set_title("7-Day Weather Forecast")
    ax.set_xlabel("Days")
    ax.set_ylabel(f"Temperature (°{unit[0]})")
    ax.legend()
    ax.set_ylim(bottom=min(temp_min))
    plt.xticks(rotation=45)
    st.pyplot(fig)


try:
    if place:
        # Fetch the 3-hourly forecast
        forecast = mgr.forecast_at_place(place, '3h')

        # Extract data
        dates, min_temp, max_temp = extract_data()

        if g_type == "Line Graph":
            line_graph(dates, min_temp, max_temp, unit)
        elif g_type == "Bar Graph":
            bar_graph(dates, min_temp, max_temp, unit)


except Exception as e:
    st.error(f"An error occurred: {e}")
