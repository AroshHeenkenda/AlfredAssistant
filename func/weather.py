from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
import os
from dotenv import load_dotenv

load_dotenv()

KEY = os.getenv("WEATHER_KEY")


class Weather:

    def __init__(self) -> None:
        #Configure the API key
        self.configuration = swagger_client.Configuration()
        self.configuration.api_key['key'] = KEY

        # create an instance of the API class
        self.api_instance = swagger_client.APIsApi(swagger_client.ApiClient(self.configuration))

    def current_weather(self):
        
        try:
            api_resp = self.api_instance.realtime_weather("melbourne")
            pprint(api_resp)
        except ApiException as e:
            print("Exception when calling APIsApi->realtime_weather: %s\n" % e)



if __name__ == "__main__":

    weather = Weather()
    weather.current_weather()
