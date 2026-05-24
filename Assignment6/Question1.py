import requests

def weather_data(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=39a9beabe027e7523a0db456ae8aa4a5&units=metric"
    
    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        print("\nWeather Report")
        print("Temperature:", data['main']['temp'], "°C")
        print("Feels Like:", data['main']['feels_like'], "°C")
        print("Humidity:", data['main']['humidity'], "%")
        print("Pressure:", data['main']['pressure'], "hPa")
        print("Weather:", data['weather'][0]['description'])
        print("Wind Speed:", data['wind']['speed'], "m/s")

    except requests.exceptions.RequestException as e:
        print("Error:", e)

city = input("Enter city name: ")
weather_data(city)