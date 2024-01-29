import os
from dotenv import load_dotenv

load_dotenv()

KEY = os.getenv("WEATHER_KEY")
BASE =  "http://api.weatherapi.com/v1" #base API url


class Weather:

    def __init__(self) -> None:
        pass

    def current_weather():
        request = BASE + f"/current.json?key={KEY}&q={'melbourne'}"