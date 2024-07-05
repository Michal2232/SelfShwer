import time
import speech_recognition as sr
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import threading

class Shower:
    def __init__(self, max_height):
        self.water_flow = 0.5  # עוצמת זרימת מים התחלתית
        self.water_hot = 0.2 * self.water_flow
        self.water_cold = 0.8 * self.water_flow
        self.height = 150  # גובה התחלתי של המקלחת
        self.max_height = max_height  # גובה מקסימלי של המקלחת
        self.soap_vector = [0, 0, 0, 0]

        self.max_temp = 41
        self.min_temp = 20
        self.water_temp = (self.water_hot * self.max_temp) + (self.water_cold * self.min_temp)

    def set_water_temperature(self, command):
        increment = 1  # שינוי הטמפרטורה במעלה אחת כל פעם
        if command == "hotter":
            self.water_temp += increment
            if self.water_temp > self.max_temp:
                self.water_temp = self.max_temp
        elif command == "colder":
            self.water_temp -= increment
            if self.water_temp < self.min_temp:
                self.water_temp = self.min_temp

        self.water_hot = (self.water_temp - self.min_temp) / (self.max_temp - self.min_temp)
        self.water_cold = 1.0 - self.water_hot

        print(f"Current Water Temperature: {self.water_temp:.2f} degrees")
        print(f"Water Flow - Hot: {self.water_hot:.2f}, Cold: {self.water_cold:.2f}")

    def set_water_flow(self, command):
        increment = 0.2  # שינוי הקוטר ב-0.2
        if command == "stronger":
            self.water_flow += increment
            if self.water_flow > 1.0:
                self.water_flow = 1.0
        elif command == "weaker":
            self.water_flow -= increment
            if self.water_flow < 0.0:
                self.water_flow = 0.0

        print(f"Water flow strength set to {self.water_flow:.2f}")

    def set_height(self, command):
        increment = 5
        if command == "higher":
            self.height += increment
            if self.height > self.max_height:
                self.height = self.max_height
        elif command == "down":
            self.height -= increment
            if self.height < 0:
                self.height = 0

        print(f"Rod height set to {self.height} cm")

    def dispense_soap(self, soap_type):
        soap_map = {
            "shampoo": 0,
            "conditioner": 1,
            "body wash": 2
        }

        if soap_type in soap_map:
            self.soap_vector = [0, 0, 0, 0]
            self.soap_vector[soap_map[soap_type]] = 1
            print(f"Dispensing {soap_type}")
            print(f"Soap vector: {self.soap_vector}")

        elif soap_type == "finish":
            self.soap_vector = [0, 0, 0, 0]
            print("Stopping all soap dispensing")
            print(f"Soap vector: {self.soap_vector}")
        else:
            print("Invalid soap type")

    def finish_shower(self):
        print("Finishing shower...")
        self.water_flow = 0
        self.water_hot = 0
        self.water_cold = 0
        self.water_temp = 0
        self.soap_vector = [0, 0, 0, 0]
        print("Water flow stopped.")
        print("Water temperature reset.")
        print("Soap vector reset.")
        
        print("Waiting 10 minutes for disinfection...")
        time.sleep(1)  # Change 1 to 600 for real-time simulation
        self.disinfect()

    def disinfect(self):
        print("Starting disinfection...")
        self.set_height("higher")
        self.soap_vector[3] = 1
        print(f"Soap vector (disinfection): {self.soap_vector}")

shower = Shower(max_height=200)
shower_position = shower.height / shower.max_height * 10  # Initial position of the shower head, normalized to 0-10
circle_radius = 0.3  # Initial size of the shower head
circle_color = 'blue'  # Initial color of the shower head

fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(0, 10)

# Set equal aspect ratio
ax.set_aspect('equal', adjustable='box')

# Vertical line representing the rod
rod, = ax.plot([0, 0], [0, 10], 'k-', linewidth=2)

# Circle representing the shower head
shower_head = plt.Circle((0, shower_position), radius=circle_radius, color=circle_color, clip_on=False)
ax.add_patch(shower_head)

# Text representing the temperature
temp_text = ax.text(0.7, 9.8, f'{shower.water_temp:.1f}°C', ha='center', va='center')

# Function to update the shower head
def update_shower_head():
    global shower_position, circle_radius, circle_color
    
    shower_position = shower.height / shower.max_height * 10
    shower_head.set_center((0, shower_position))
    
    if shower.soap_vector[0] == 1:
        circle_color = 'pink'
    elif shower.soap_vector[1] == 1:
        circle_color = 'yellow'
    elif shower.soap_vector[2] == 1:
        circle_color = 'green'
    elif shower.water_flow == 0:
        circle_color = 'black'
    else:
        circle_color = 'blue'
    
    shower_head.set_color(circle_color)
    
    circle_radius = 0.3 + 0.3 * shower.water_flow  # שינוי הקוטר בהתאם לזרימת המים
    shower_head.set_radius(circle_radius)
    
    temp_text.set_text(f'{shower.water_temp:.1f}°C')


def update(frame):
    update_shower_head()
    return shower_head, temp_text

ani = FuncAnimation(fig, update, frames=range(100), interval=500, blit=True)

def get_voice_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please say something...")
        audio_text = r.listen(source)
        print("Recording complete")

        try:
            text = r.recognize_google(audio_text).lower()
            return text

        except sr.UnknownValueError:
            print("Sorry, I did not get that")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

    return None

code_words = ["shower on", "hotter", "colder", "stronger", "weaker", "higher", "down", "shampoo", "conditioner", "body wash", "finish", "end"]

def control_shower(command):
    if command in ['higher', 'down']:
        shower.set_height(command)
    elif command in ['hotter', 'colder']:
        shower.set_water_temperature(command)
    elif command in ['stronger', 'weaker']:
        shower.set_water_flow(command)
    elif command in ['shampoo', 'conditioner', 'body wash', 'finish']:
        shower.dispense_soap(command)
    elif command == 'end':
        shower.finish_shower()
    update_shower_head()

def voice_command_listener():
    while True:
        command = get_voice_command()
        
        if command == "shower on":
            print("Shower system initialized. Ready for commands.")
            while True:
                command = get_voice_command()
                if command in code_words:
                    control_shower(command)
                    if command == "end":
                        break
                else:
                    print(f"The word '{command}' is not a recognized code word. Please try again.")
        else:
            print("Please start by saying 'shower on' to initialize the system.")

voice_thread = threading.Thread(target=voice_command_listener)
voice_thread.start()

plt.show()
