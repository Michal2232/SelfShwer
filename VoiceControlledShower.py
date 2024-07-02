class VoiceControlledShower:
    def __init__(self):
        self.height = 0  # Initial height of the rod
        self.water_flow = 0  # Initial water flow strength
        self.water_temp = 0  # Initial water temperature

    def set_height(self, height):
        self.height = height
        print(f"Rod height set to {height} units")

    def set_delay(self, duration):
        print(f"Delaying for {duration} seconds")
        time.sleep(duration)

    def set_water_flow(self, strength):
        self.water_flow = strength
        print(f"Water flow strength set to {strength}")

    def dispense_soap(self, duration):
        print(f"Dispensing soap for {duration} seconds")
        time.sleep(duration)

    def set_water_temperature(self, temperature):
        self.water_temp = temperature
        print(f"Water temperature set to {temperature} degrees")

    def disinfect_sponges(self):
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
shower = VoiceControlledShower()
commands = [
    {'action': 'set_height', 'value': 10},
    {'action': 'set_delay', 'value': 5},
    {'action': 'set_water_flow', 'value': 3},
    {'action': 'dispense_soap', 'value': 2},
    {'action': 'set_water_temperature', 'value': 37},
    {'action': 'disinfect_sponges'}
]

for command in commands:
    shower.execute_command(command)
