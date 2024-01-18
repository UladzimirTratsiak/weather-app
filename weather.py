import requests
import os

from dotenv import load_dotenv


def get_weather(city):
    load_dotenv()
    api_key = os.getenv("API_KEY")
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            return data
        else:
            print(f"Ошибка: {data['message']}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    print(get_weather("Wroclaw"))
