# Weather CLI Tool 🌤️

A command-line weather tool that fetches real-time weather data for any city using the OpenWeatherMap API, built with Python.

## Features
- Get real-time weather data for any city in the world
- Displays temperature, feels like, min/max temperature
- Shows humidity, pressure, sea level and ground level
- Simple one-command usage

## How to Use
Run the script:

python weather_tool.py

Then follow the prompt:

Which city would you like to check its weather today? London

## Example Output

Data retrieved!
City name: London
Condition: light rain
Temperature: 15.3
Feels like: 13.8
Temperature min: 13.0
Temperature max: 17.1
Pressure: 1012
Humidity: 82
Sea level: 1012
Ground level: 1005

## Setup
1. Get a free API key from https://openweathermap.org/api
2. Open weather_tool.py
3. Replace YOUR_API_KEY_HERE with your actual key

## Requirements
- Python 3.x
- requests

## Installation
pip install requests
