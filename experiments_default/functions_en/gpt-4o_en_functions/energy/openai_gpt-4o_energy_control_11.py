# Here's the `function.py` file you requested, which will be located in the `functions` folder. This file will contain the main function to open windows when the temperature is above 26 degrees.
# 
# ### `function.py`

from home.sensor import IndoorTemperatureSensor
from home.actuator import Window
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, TEMP_CHANGE_DURATION_WINDOW

def main():
    # Initialize the home plan
    home = home_plan()

    # Get all indoor temperature sensors
    temp_sensors = get_all_sensors(home, "IndoorTemperature")

    # Get all window actuators
    windows = get_all_actuators(home, "Window")

    # Turn on all sensors and actuators
    for sensor in temp_sensors:
        sensor.turn_on()
    
    for window in windows:
        window.turn_on()

    # Monitor temperature and control windows accordingly
    for sensor in temp_sensors:
        temperature = sensor.get_reading()
        if temperature is not None and temperature > 26:  # Opening windows if temp > 26 degrees
            for window in windows:
                window.turn_on()
                print(f"Opening {window.id} due to high temperature: {temperature}°C")
        else:
            for window in windows:
                window.turn_off()
                print(f"Closing {window.id}, current temperature: {temperature}°C")

if __name__ == "__main__":
    main()