import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from shower import Shower  # אמור להיות באותה תיקייה עם קובץ המקלחת

# יצירת אובייקט מקלחת
shower = Shower(max_height=200)

# תחילית עמודה המקלחת
shower_position = 5  # אמצע הסולם מ-0 עד 10

# פונקציה להזזת ראש המקלחת
def move_shower(command):
    global shower_position
    if command == "up":
        shower_position = min(10, shower_position + 1)
    elif command == "down":
        shower_position = max(0, shower_position - 1)
    # אם הפקודה היא "עצירה" או אחרת, המיקום יישאר ללא שינוי

# פונקציה לעדכון האנימציה
def update(frame):
    global shower_position

    # Clear the plot and redraw
    plt.clf()
    plt.ylim(0, 10)
    plt.xlim(0, 1)
    plt.title("Shower System Simulation")
    plt.ylabel("Height")

    # Determine line thickness based on water flow strength
    if shower.water_flow == 'strong':
        line_width = 10
    elif shower.water_flow == 'weak':
        line_width = 2
    else:
        line_width = 5  # Default thickness

    # Draw shower head line and label
    plt.plot([0, 1], [shower_position, shower_position], 'b-', linewidth=line_width)
    plt.text(0.5, shower_position, f"Shower Head", ha='center', va='bottom')

    # Update and display soap types
    soap_types = ["Shampoo", "Conditioner", "Body Wash", "Finish"]
    for i, soap in enumerate(soap_types):
        if shower.soap_vector[i] == 1:
            plt.text(0.1, 9 - i, f"{soap} Dispensed", fontsize=8)

    return plt.gca()


# יצירת האנימציה
fig = plt.figure(figsize=(6, 8))
ani = FuncAnimation(fig, update, frames=range(100), interval=500, blit=False)

# פונקציה לשליטה באנימציה
def control_shower(commands):
    for command in commands:
        move_shower(command)
        if command in ['up', 'down']:
            shower.set_height(command)
        elif command == 'stop':
            continue
        elif command in ['shampoo', 'conditioner', 'body wash', 'finish']:
            shower.dispense_soap(command)
        elif command in ['strong', 'weak']:
            shower.set_water_flow(command)
        plt.pause(0.5)

# שימוש דוגמתי
while True:
    print("\nAvailable commands:")
    print("1. Move shower head (up/down)")
    print("2. Dispense soap (shampoo/conditioner/body wash/finish)")
    print("3. Set water flow (strong/weak)")
    print("4. Finish shower")
    print("5. Exit")

    command = input("\nEnter command number: ").strip()

    if command == '1':
        move_command = input("Enter movement command (up/down): ").strip()
        control_shower([move_command])

    elif command == '2':
        soap_command = input("Enter soap type (shampoo/conditioner/body wash/finish): ").strip()
        control_shower([soap_command])

    elif command == '3':
        flow_command = input("Enter flow command (strong/weak): ").strip()
        control_shower([flow_command])

    elif command == '4':
        control_shower(['finish'])
        break

    elif command == '5':
        print("Exiting simulation.")
        break

    else:
        print("Invalid command. Please try again.")

plt.show()
