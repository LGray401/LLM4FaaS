# Based on your description and provided source code, I'll provide you with a `function.py` file. This file will include a `main` function that will allow you to execute a series of actions to simulate the opening of a temperature sensor, opening a window, and turning on the lights.
# 
# First, let's create a `function.py` file in the `functions` folder with the following content:

import os
import time
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor
from home.actuator import Window, Light
from home.home_plan import home_plan, get_room_sensors, get_room_actuators

def main():
    # Load the home plan
    home = home_plan()

    # Access the living room
    living_room = get_room(home, "LivingRoom")

    # Access the indoor temperature sensor in the living room
    indoor_temp_sensor = get_room_sensors(living_room, "IndoorTemperature")[0]

    # Access the window and light in the living room
    window = get_room_actuators(living_room, "Window")[0]
    light = get_room_actuators(living_room, "Light")[0]

    # Turn on the indoor temperature sensor
    indoor_temp_sensor.turn_on()
    print(f"Indoor Temperature Sensor is now ON.")

    # Wait for a short moment to simulate sensor reading
    time.sleep(2)

    # Get the temperature reading from the indoor temperature sensor
    indoor_temp = indoor_temp_sensor.get_reading()
    print(f"Indoor Temperature Reading: {indoor_temp}°C")

    # Open the window
    window.turn_on()
    print("Window is now OPEN.")

    # Turn on the light
    light.turn_on()
    print("Light is now ON.")

    # Wait for a short moment before turning off the light and window
    time.sleep(2)

    # Turn off the light
    light.turn_off()
    print("Light is now OFF.")

    # Close the window
    window.turn_off()
    print("Window is now CLOSED.")

# Check if this script is being run directly and not imported as a module
if __name__ == "__main__":
    main()