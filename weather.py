import streamlit as st
import requests

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # for Celsius, use 'imperial' for Fahrenheit
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Streamlit application
st.title("Weather App")
st.write("Enter a city name to get the current weather.")

# Input for city name
city = st.text_input("City Name:")

# Your OpenWeatherMap API key
api_key = "86f2fcf0ef80738d847825e233078c73"  # Replace with your actual key

if st.button("Get Weather"):
    if city:
        weather_data = get_weather(city, api_key)
        
        if weather_data:
            temp = weather_data['main']['temp']
            description = weather_data['weather'][0]['description']
            humidity = weather_data['main']['humidity']
            st.success(f"Temperature: {temp}°C")
            st.success(f"Weather: {description}")
            st.success(f"Humidity: {humidity}%")
        else:
            st.error("City not found or an error occurred.")
    else:
        st.warning("Please enter a city name.")




