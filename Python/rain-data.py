""" rain data in LV """

import requests

# API key for OpenWeatherMap
api_key = "YOUR_API_KEY"

# city for which to get weather information
city = "Las Vegas, NV, USA"

# URL for the OpenWeatherMap API
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

# Make a request to the API
response = requests.get(url)

# If the request was successful, then retrieve the weather information
if response.status_code == 200:
    # Convert the response to a dictionary
    weather_data = response.json()

    # Extract the temperature (in Kelvin)
    temperature = weather_data["main"]["temp"]

    # Convert the temperature to Celsius
    temperature = temperature - 273.15

    # Print the temperature
    print(f"The temperature in {city} is {temperature:.2f}°C")
else:
    # If the request was unsuccessful, then print an error message
    print("Could not retrieve weather information.")
