import requests
#my api key bf007db681493973937e2ffe315863bd

# ---------Taking Input from Front-end user
api_key = input("Enter your API key here: ")
city_name = input("Enter City name to find info: ").capitalize()

# using openweather website to get information
request = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
response = requests.get(request).json()

# checking if it's successfull or not
if response.get("cod") != 200:
    print(f"Error: {response.get('message', 'Unknown error occurred')}")
else:
    # Extract temperature and weather description
    temp_in_kelvin = response["main"]["temp"]
    description = response["weather"][0]["description"]

    # Convert temperature from Kelvin to Celsius
    celsius = int(temp_in_kelvin - 273.15)
    print(f"The city is: {city_name}, Temperature: {round(celsius, 1)}°C. The weather condition is: {description}.")
#