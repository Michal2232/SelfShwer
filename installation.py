import speech_recognition as sr

def get_voice_command():
    # Initialize recognizer class (for recognizing the speech)
    r = sr.Recognizer()

    # Reading Microphone as source
    # Listening the speech and store in audio_text variable
    with sr.Microphone() as source:
        print("Please say something...")
        audio_text = r.listen(source)
        print("Recording complete")

        # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
        try:
            # Using google speech recognition
            text = r.recognize_google(audio_text)
            print("You said: " + text)
        except sr.UnknownValueError:
            print("Sorry, I did not get that")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

# Call the function
get_voice_command()