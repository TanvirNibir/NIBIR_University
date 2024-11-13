import requests

my_api = "bf007db681493973937e2ffe315863bd"

def weather():
    api_key = input("Enter your Api first")
    city_name = input("Enter city name: ").capitalize()
    requst = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    response = requests.get(requst)
    if response != 200:
        print(f"Error: {response.get('message', 'Unknown error occurred')}")

weather()

