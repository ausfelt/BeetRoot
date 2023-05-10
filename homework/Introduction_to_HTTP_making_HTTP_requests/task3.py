import requests
import json

api_key = "b11d77db0bc38cbca942d3a84f1d7e50"

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.text)
        weather = data["weather"][0]["description"].capitalize()
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        return f"The weather in {city} is {weather}. The temperature is {temp}°C, and it feels like {feels_like}°C."
    else:
        return "Error: Failed to retrieve weather data."

city = input("Enter a city name: ")
result = get_weather(city)
print(result)

# Something is buggy with either their API key or i must pay for it. Code works though