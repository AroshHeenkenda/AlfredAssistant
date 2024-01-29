import os
from dotenv import load_dotenv

load_dotenv()

KEY = os.getenv("WEATHER_KEY")



class Weather:

    def __init__(self) -> None:
        pass