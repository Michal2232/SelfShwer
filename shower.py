import time


class Shower:
    def __init__(self, max_height):
        self.water_flow = 0.5  # Initial water flow strength
        self.water_hot = 0.2 * self.water_flow
        self.water_cold = 0.8 * self.water_flow
        self.height = 150  # Initial height of the rod
        self.max_height = max_height  # Maximum height of the rod
        self.soap_vector = [0, 0, 0, 0]

        self.max_temp = 60
        self.min_temp = 10

    def set_water_temperature(self, command):
        if command == "hot":
            increment = 0.1
            self.water_hot += increment
            if self.water_hot > 1.0:
                self.water_hot = 1.0
            self.water_cold = 1.0 - self.water_hot

        elif command == "cold":
            increment = 0.1
            self.water_cold += increment
            if self.water_cold > 1.0:
                self.water_cold = 1.0
            self.water_hot = 1.0 - self.water_cold

        self.water_temp = (self.water_hot * self.max_temp) + (self.water_cold * self.min_temp)
        print(f"Current Water Temperature: {self.water_temp:.2f} degrees")
        print(f"Water Flow - Hot: {self.water_hot:.2f}, Cold: {self.water_cold:.2f}")

    def set_water_flow(self, command):
        increment = 0.1  # שינוי של 10% בכל פקודה
        if command == "strong":
            self.water_flow += increment
            if self.water_flow > 1.0:
                self.water_flow = 1.0  # הגבלת עוצמת הזרימה ל-100%
        elif command == "weak":
            self.water_flow -= increment
            if self.water_flow < 0.0:
                self.water_flow = 0.0  # הגבלת עוצמת הזרימה ל-0%

        print(f"Water flow strength set to {self.water_flow:.2f}")

    def set_height(self, command):
        increment = 5  # שינוי של 5 ס"מ בכל פקודה
        if command == "up":
            self.height += increment
            if self.height > self.max_height:
                self.height = self.max_height  # הגבלת הגובה למקסימום
        elif command == "down":
            self.height -= increment
            if self.height < 0:
                self.height = 0  # הגבלת הגובה למינימום

        print(f"Rod height set to {self.height} cm")

    def dispense_soap(self, soap_type):
        # המרת מילת הסבון לווקטור המתאים
        soap_map = {
            "shampoo": 0,
            "conditioner": 1,
            "body wash": 2
        }

        if soap_type in soap_map:
            self.soap_vector = [0, 0, 0, 0]  # אתחול כל הוקטור
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
        self.water_flow = 0  # מאפסת את זרימת המים
        self.soap_vector = [0, 0, 0, 0]  # מאפסת את וקטור הסבונים
        print("Water flow stopped.")
        print("Soap vector reset.")

        # חיטוי המקלחת לאחר 10 דקות
        time.sleep(600)  # 10 דקות = 600 שניות
        self.disinfect()

    def disinfect(self):
        print("Starting disinfection...")
        self.water_flow=0.5

        # self.set_height("up")  # כוונון גובה מקסימלי של הטוש
        self.height = self.max_height
        self.water_flow=0.5
        self.water_hot = 0.6* self.water_flow
        self.water_cold = 0.4 * self.water_flow
        time.sleep(60) # for a minute only water flowing
        self.soap_vector[3] = 1  # הפעלת זרימת חומר חיטוי
        print(f"Soap vector (disinfection): {self.soap_vector}")
        time.sleep(180) # for 3 minutes water whith disinfectant flowing
        self.soap_vector = [0, 0, 0, 0] # stop disinfectant flowing
        print(f"Soap vector (disinfection): {self.soap_vector}")
        time.sleep(60) # for a minute only water flowing
        # turning off the water
        self.water_flow = 0
        self.water_hot = 0
        self.water_cold = 0




