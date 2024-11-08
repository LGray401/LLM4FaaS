# To create a smart home application based on the provided source code and functional description, we'll first need to interpret the functional description. Since the description given is in Chinese ("控制"), which translates to "control," we can assume that the application should focus on controlling the smart home devices using the provided sensor and actuator classes.
# 
# Let's implement a simple command-line application that allows users to interact with various rooms, sensors, and actuators. This application will allow us to turn devices on or off, get sensor readings, and perform any actions available for actuators.
# 
# We'll create a new script called `smart_home.py` that utilizes the existing classes to implement this functionality.
# 
# ### smart_home.py
# 
# ```python
import sys
from home.home_plan import home_plan, get_room, print_home_plan

def main():
    home = home_plan()

    while True:
        print("\nWelcome to the Smart Home Control System")
        print("1. View Home Plan")
        print("2. Control a Room")
        print("3. Exit")
        choice = input("Please select an option: ")

        if choice == "1":
            print_home_plan(home)
        
        elif choice == "2":
            room_name = input("Enter the name of the room you wish to control: ")
            room = get_room(home, room_name)
            if room:
                control_room(room)
        
        elif choice == "3":
            print("Exiting the application. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

def control_room(room):
    while True:
        print(f"\nControlling {room.name}")
        print("1. View Sensors")
        print("2. View Actuators")
        print("3. Go Back")
        choice = input("Please select an option: ")

        if choice == "1":
            for sensor in room.sensors:
                sensor.get_status()
                if sensor.status == "on":
                    sensor.get_reading()
        
        elif choice == "2":
            for actuator in room.actuators:
                actuator.get_status()
                # You can add additional interaction with actuators here
                # For example, turning them on/off or performing specific actions.
        
        elif choice == "3":
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
# ```
# 
# ### Running the Application
# 
# To run the application in a Linux terminal, you can use the following command:
# 
# ```bash
# python smart_home.py
# ```
# 
# ### Explanation
# 
# - **Home Plan**: The application initializes the home plan using the `home_plan()` function.
# - **Main Menu**: The user is presented with options to view the home plan, control a room, or exit the application.
# - **Room Control**: When controlling a room, users can view the status of sensors and actuators. You can extend this functionality to allow users to turn devices on or off and interact with them further.
# - **Sensors and Actuators**: The script uses the existing methods provided in `sensor.py` and `actuator.py` to get the status and readings of sensors and actuators.