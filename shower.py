import time;

class Shower:
    def __init__(self,max_height):
        self.water_flow = 0.5 # Initial water flow strength
        self.water_hot = 0.2*self.water_flow
        self.water_cold= 0.8*self.water_flow
        self.height = 150  # Initial height of the rod
        self.height = 150  # Initial height of the rod
        self.max_height = max_height  # Maximum height of the rod
        self.soap_vector=[0,0,0,0]

        self.max_temp = 60                                ####################
        self.min_temp = 10                                ####################

    def set_water_temperature(self, command):             ####################
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


    def set_water_flow(self, command):                    ####################
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

    def dispense_soap(self, duration):
        print(f"Dispensing soap for {duration} seconds")
        time.sleep(duration)


    def finish_shower(self):
        return


    def disinfect(self):
        print("Disinfecting sponges...")
        time.sleep(5)  # Assume disinfection takes 5 seconds
        print("Sponges disinfected")

    def execute_command(self, command):
        if command['action'] == 'set_height':
            self.set_height(command['value'])
        elif command['action'] == 'set_delay':
            self.set_delay(command['value'])
        elif command['action'] == 'set_water_flow':
            self.set_water_flow(command['value'])
        elif command['action'] == 'dispense_soap':
            self.dispense_soap(command['value'])
        elif command['action'] == 'set_water_temperature':
            self.set_water_temperature(command['value'])
        elif command['action'] == 'disinfect_sponges':
            self.disinfect_sponges()

    # Example usage

