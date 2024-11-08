# Great! I see you have provided a functional description and source code for a smart home application. Based on the provided code, it seems you have a system with sensors and actuators in a smart home environment.
# 
# To create a Python application that runs in a Linux terminal, we can create a main script that utilizes the components you have in the `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py` files. This script will initialize a home setup and allow you to interact with the sensors and actuators.
# 
# Let's create a main script called `smart_home.py` that ties everything together:
# 
# ```python
from home.home_plan import home_plan, print_home_plan, get_room_sensors, get_room_actuators
from home.sensor import IndoorTemperatureSensor
from home.actuator import Heater, AC, Light

def main():
    # Initialize the home setup
    home = home_plan()
    print_home_plan(home)

    # Example of interacting with the components
    # Let's take "LivingRoom" as an example
    room_name = "LivingRoom"

    # Get sensors and actuators in the Living Room
    sensors = get_room_sensors(home, room_name)
    actuators = get_room_actuators(home, room_name)

    # Turn on all sensors and get readings
    for sensor in sensors:
        sensor.turn_on()
        sensor.get_reading()

    # Turn on all actuators
    for actuator in actuators:
        actuator.turn_on()

    # Adjust temperature using Heater and AC based on sensor readings
    for sensor in sensors:
        if isinstance(sensor, IndoorTemperatureSensor):
            current_temp = sensor.get_reading()
            for actuator in actuators:
                if isinstance(actuator, Heater):
                    actuator.set_target_temperature(22)  # Set a target temperature
                    actuator.adjust_temperature(current_temp)
                elif isinstance(actuator, AC):
                    actuator.set_target_temperature(22)
                    actuator.adjust_temperature(current_temp)

    # Adjust light brightness if Light actuator is present
    for actuator in actuators:
        if isinstance(actuator, Light):
            actuator.set_brightness_level("medium")

if __name__ == "__main__":
    main()
# ```
# 
# ### How to Run the Application
# 
# 1. Ensure all the Python files (`sensor.py`, `actuator.py`, `home_plan.py`, `config.py`, and `smart_home.py`) are in the appropriate directory structure, like so:
# 
# ```
# home/
#     sensor.py
#     actuator.py
#     home_plan.py
#     config.py
# smart_home.py
# ```
# 
# 2. Make sure you have Python installed on your Linux system.
# 
# 3. Open a terminal and navigate to the directory containing these files.
# 
# 4. Run the application using the following command:
# 
# ```bash
# python3 smart_home.py
# ```
# 
# This will initialize the smart home setup, print the home plan, and demonstrate interaction with the sensors and actuators in the Living Room. You can expand this script to include more functionality based on your requirements or the functional description you provided.