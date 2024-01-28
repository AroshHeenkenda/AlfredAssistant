import speech_recognition as sr

def test():

    #The recogniser, will use Google Web Speech API
    r = sr.Recognizer()
    mic = sr.Microphone() #Hard coded the working microphone

    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

            # set up the response object
        response = {
        "success": True,
        "error": None,
        "transcription": None
        }

        try:
            response["transcription"] = r.recognize_google(audio)
        except sr.RequestError:
            # API was unreachable or unresponsive
            response["success"] = False
            response["error"] = "API unavailable"
        except sr.UnknownValueError:
            # speech was unintelligible
            response["error"] = "Unable to recognize speech"
        
        print(response)



if __name__ == "__main__":

    test()
