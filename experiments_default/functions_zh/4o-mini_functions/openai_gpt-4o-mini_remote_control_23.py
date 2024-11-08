# Based on your functional description and the provided source code files, I will create a `function.py` file that serves as the main entry point for your smart home project. This file will initialize the smart home system, setting up the various rooms with their sensors and actuators, and will provide a way to interact with them.
# 
# Here is the `function.py` file:

# function.py
from home.home_plan import home_plan, print_home_plan, get_room, get_room_sensors, get_room_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH
import time

def main():
    # Initialize the home with the defined plan
    home = home_plan()

    # Print the home plan for reference
    print_home_plan(home)

    # Example interaction with the home system
    while True:
        room_name = input("Enter a room name to interact with (or 'exit' to quit): ")
        if room_name.lower() == 'exit':
            break

        room = get_room(home, room_name)
        if room is not None:
            # Get sensors in the room
            sensors = get_room_sensors(home, room_name)
            if sensors:
                for sensor in sensors:
                    sensor.turn_on()  # Turn on the sensor
                    reading = sensor.get_reading()  # Get a reading
                    print(f"{sensor.id} reading: {reading}")

            # Get actuators in the room
            actuators = get_room_actuators(home, room_name)
            if actuators:
                for actuator in actuators:
                    actuator.turn_on()  # Turn on the actuator
                    print(f"{actuator.id} is turned on.")

            # Example of controlling a specific type of actuator or sensor
            # This can include specific logic based on readings and thresholds
            time.sleep(2)  # Simulate a delay for user interaction
        else:
            print(f"No room named '{room_name}' found.")

if __name__ == "__main__":
    main()