# To create a smart home application based on your functional description, we will integrate the provided modules (`sensor.py`, `actuator.py`, `home_plan.py`, and `config.py`) and implement the required functionality. Here's how you can achieve this:
# 
# 1. When the AC is turned on, automatically close all doors and windows.
# 2. If the indoor temperature is higher than a threshold and the outdoor temperature is lower, prompt the user to decide whether to open the windows for cooling.
# 
# Let's write the main application code to achieve this behavior:
# 
# ```python
# main.py

from home.actuator import AC, Window, Door
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor
from home.home_plan import home_plan, get_all_actuators, get_room_sensors
from home.config import TEMP_HIGH

def main():
    home = home_plan()

    # Get all ACs in the home
    acs = get_all_actuators(home, "AC")

    # Turn on all ACs
    for ac in acs:
        ac.turn_on()

    # When ACs are turned on, close all doors and windows
    doors = get_all_actuators(home, "Door")
    windows = get_all_actuators(home, "Window")

    for door in doors:
        door.turn_off()  # Assuming turn_off means close

    for window in windows:
        window.turn_off()  # Assuming turn_off means close

    # Check the temperature inside and outside
    for room in home:
        indoor_sensors = get_room_sensors(home, room.name)
        for sensor in indoor_sensors:
            if isinstance(sensor, IndoorTemperatureSensor):
                indoor_temp = sensor.get_reading()

        for sensor in indoor_sensors:
            if isinstance(sensor, OutdoorTemperatureSensor):
                outdoor_temp = sensor.get_reading()

        if indoor_temp > TEMP_HIGH and outdoor_temp < indoor_temp:
            response = input(f"The indoor temperature in {room.name} is higher than {TEMP_HIGH}°C "
                             f"and the outdoor temperature is lower. Would you like to open the windows to cool down? (yes/no): ")
            if response.lower() == "yes":
                for window in windows:
                    if window.room_name == room.name:
                        window.turn_on()  # Open the window

if __name__ == "__main__":
    main()
# ```
# 
# ### Command to Run the Application
# 
# To run this application from a Linux terminal, you would execute the following command, assuming all files are in a folder named `home` and the main script is named `main.py`:
# 
# ```bash
# python3 main.py
# ```
# 
# ### Explanation
# 
# - **AC Control**: We iterate through all AC actuators and turn them on. When the AC is turned on, we also iterate through all doors and windows, turning them off (assuming `turn_off()` corresponds to closing them).
# - **Temperature Check**: We check the indoor and outdoor temperatures using the respective sensors. If the indoor temperature is above a high threshold and the outdoor temperature is lower, we prompt the user to open the windows.
# - **User Interaction**: The script asks the user whether they would like to open the windows for cooling, providing an interactive element.
# 
# This script integrates with the provided modules to achieve the specified smart home behavior. Adjustments may be necessary depending on the exact behavior of the `turn_on` and `turn_off` methods in your actuator classes.