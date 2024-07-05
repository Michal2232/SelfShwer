import speech_recognition as sr

from shower import Shower


def get_voice_command():
    # Initialize recognizer class (for recognizing the speech)
    r = sr.Recognizer()

    # Reading Microphone as source
    with sr.Microphone() as source:
        print("Please say something...")
        audio_text = r.listen(source)
        print("Recording complete")

        try:
            # Using google speech recognition
            text = r.recognize_google(audio_text).lower()
            return text

        except sr.UnknownValueError:
            print("Sorry, I did not get that")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

    return None  # במקרה שלא הושגה פקודה קולית


# רשימת המילים המותרות
code_words = ["shower on", "hot", "cold", "strong", "weak", "up", "down", "shampoo", "hair conditioner", "body wash",
              "finish", "end"]


def main():
    command = get_voice_command()

    if command == "shower on":
        shower = Shower(max_height=200)  # יצירת אובייקט של המקלחת
        print("Shower system initialized. Ready for commands.")
        command = get_voice_command()

        while True:
            command = get_voice_command()
            if command in code_words:

                if command in ["hot", "cold"]:
                    shower.set_water_temperature(command)

                elif command in ["strong", "weak"]:
                    shower.set_water_flow(command)

                elif command in ["up", "down"]:
                    shower.set_height(command)

                elif command in ["shampoo", "hair conditioner", "body wash", "finish"]:
                    shower.dispense_soap(command)

                elif command == "end":
                    shower.finish_shower()
                    break  # יציאה מהלולאה

            else:
                print(f"The word '{command}' is not a recognized code word. Please try again.")
    else:
        print("Please start by saying 'shower on' to initialize the system.")


# הרצת התוכנית הראשית
if __name__ == "__main__":
    main()
