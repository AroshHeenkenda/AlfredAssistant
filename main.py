import speech_recognition as sr
from func.weather import Weather
from func.phrases import Phrase

#Give a timeout to define how long we should wait for audio
TIMEOUT=10

def test():

    #The recogniser, will use Google Web Speech API
    r = sr.Recognizer()
    mic = sr.Microphone() #Hard coded the working microphone

    with mic as source:

        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source, timeout=TIMEOUT)

        # Set up the response object
        response = {
        "success": True,
        "error": None,
        "words": None
        }

        print("Recognising...")
        try:
            response["words"] = r.recognize_google(audio)

        #API was unreachable or unresponsive
        except sr.RequestError:
            response["success"] = False
            response["error"] = "API unavailable"
        
        #Speech was unintelligble
        except sr.UnknownValueError:
            response["error"] = "Unable to recognize speech"
        
        #Timeout user took too long to speak
        except sr.WaitTimeoutError:
            response["error"] = "Timeout, user took too long to speak"

        
        print(response)

        print(response["words"].upper())
        print(Phrase.WEATHER.value.upper())

        if response["words"].upper() == Phrase.WEATHER.value.upper():
            Weather().current_weather()





if __name__ == "__main__":

    test()
