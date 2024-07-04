#בדיקת תקינות הפונקציות על ידי קלט מהמשתמש ולא על ידי פקודות קוליות
import time

class Shower:
    def __init__(self, max_height):
        self.water_flow = 0.5  # עוצמת זרימת מים התחלתית
        self.water_hot = 0.2 * self.water_flow
        self.water_cold = 0.8 * self.water_flow
        self.height = 150  # גובה התחלתי של המקלחת
        self.max_height = max_height  # גובה מקסימלי של המקלחת
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
        increment = 0.1
        if command == "strong":
            self.water_flow += increment
            if self.water_flow > 1.0:
                self.water_flow = 1.0
        elif command == "weak":
            self.water_flow -= increment
            if self.water_flow < 0.0:
                self.water_flow = 0.0

        print(f"Water flow strength set to {self.water_flow:.2f}")

    def set_height(self, command):
        increment = 5
        if command == "up":
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
        self.soap_vector = [0, 0, 0, 0]
        print("Water flow stopped.")
        print("Soap vector reset.")
        
        print("Waiting 10 minutes for disinfection...")
        time.sleep(1)  # להחליף את 1 ב-600 למצב אמת
        self.disinfect()

    def disinfect(self):
        print("Starting disinfection...")
        self.set_height("up")
        self.soap_vector[3] = 1
        print(f"Soap vector (disinfection): {self.soap_vector}")

# פונקציה שמאפשרת לבדוק את המחלקה על ידי קלט מהמשתמש
def interactive_test():
    shower = Shower(max_height=200)  # ליצור אובייקט של המקלחת עם גובה מקסימלי של 200 ס"מ

    while True:
        print("\nAvailable commands:")
        print("1. Set water temperature (hot/cold)")
        print("2. Set water flow (strong/weak)")
        print("3. Set rod height (up/down)")
        print("4. Dispense soap (shampoo/conditioner/body wash/finish)")
        print("5. Finish shower")
        print("6. Exit")
        
        command = input("\nEnter command number: ").strip()

        if command == '1':
            temp_command = input("Enter temperature command (hot/cold): ").strip()
            shower.set_water_temperature(temp_command)

        elif command == '2':
            flow_command = input("Enter flow command (strong/weak): ").strip()
            shower.set_water_flow(flow_command)

        elif command == '3':
            height_command = input("Enter height command (up/down): ").strip()
            shower.set_height(height_command)

        elif command == '4':
            soap_command = input("Enter soap type (shampoo/conditioner/body wash/finish): ").strip()
            shower.dispense_soap(soap_command)

        elif command == '5':
            shower.finish_shower()

        elif command == '6':
            print("Exiting test.")
            break

        else:
            print("Invalid command. Please try again.")

# הרצת הבדיקה
if __name__ == "__main__":
    interactive_test()
