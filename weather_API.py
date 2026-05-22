import requests

api_key = "5b62510c659d45a7c8c70d823028e1a7"

def get_weather_info(name):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={name}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        print("Data retrieved!")
        weather_data = response.json()

        return weather_data

    else:
        print(f"Failed to retrieved data {response.status_code}")



city_name = input("Which city would you like to check its weather today?  ")
weather_info = get_weather_info(city_name)

if weather_info:
    print(f"City name: {city_name}")
    print(f"Condition: {weather_info['weather'][0]['description']}")
    print(f"Temperature: {weather_info['main']['temp']}")
    print(f"Feels like: {weather_info['main']['feels_like']}")
    print(f"Temperature min: {weather_info['main']['temp_min']}")
    print(f"Temperature max: {weather_info['main']['temp_max']}")
    print(f"Pressure: {weather_info['main']['pressure']}")
    print(f"Humidity: {weather_info['main']['humidity']}")
    print(f"Sea level: {weather_info['main']['sea_level']}")
    print(f"Ground level: {weather_info['main']['grnd_level']}")
else:
    print("Opss, looks like we couldn't find a city with this name. Check the spelling! ")

