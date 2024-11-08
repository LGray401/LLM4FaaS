# Based on the functional description and the provided source code, we need to implement a `function.py` file that contains a `main` function. This function will perform the following:
# 
# 1. When the air conditioning (AC) is turned on, close all doors and windows.
# 2. If the indoor temperature is high and the outdoor temperature is lower, prompt the user to consider opening a window to cool down the room.
# 
# Below is the implementation for `function.py`. This script will use the classes and functions defined in the other modules.
# 
# ```python
# function.py
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor
from home.actuator import AC, Window, Door
from home.home_plan import home_plan, get_room_actuators
from home.config import TEMP_HIGH
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    # Set up the home environment
    home = home_plan()

    # Iterate over each room
    for room in home:
        # Get the AC in the room
        ac_units = [actuator for actuator in room.actuators if isinstance(actuator, AC)]
        windows = [actuator for actuator in room.actuators if isinstance(actuator, Window)]
        doors = [actuator for actuator in room.actuators if isinstance(actuator, Door)]
        indoor_temp_sensors = [sensor for sensor in room.sensors if isinstance(sensor, IndoorTemperatureSensor)]
        outdoor_temp_sensors = [sensor for sensor in room.sensors if isinstance(sensor, OutdoorTemperatureSensor)]

        for ac in ac_units:
            if ac.get_status() == "on":
                # Close all windows and doors when AC is on
                for window in windows:
                    if window.get_status() == "on":
                        logger.info(f"Closing window in room {room.name}")
                        window.turn_off()

                for door in doors:
                    if door.get_status() == "on":
                        logger.info(f"Closing door in room {room.name}")
                        door.turn_off()

        # Check temperatures to possibly open windows
        for indoor_sensor in indoor_temp_sensors:
            indoor_temp = indoor_sensor.get_reading()
            if indoor_temp is None or not outdoor_temp_sensors:
                continue

            for outdoor_sensor in outdoor_temp_sensors:
                outdoor_temp = outdoor_sensor.get_reading()
                if outdoor_temp is None:
                    continue

                if indoor_temp > TEMP_HIGH and outdoor_temp < indoor_temp:
                    logger.info(f"Indoor temp is {indoor_temp}°C and outdoor temp is {outdoor_temp}°C.")
                    response = input(f"In {room.name}, indoor temp is high and outdoor temp is lower. Do you want to open a window to cool down? (yes/no): ")
                    if response.lower() == "yes":
                        for window in windows:
                            if window.get_status() == "off":
                                logger.info(f"Opening window in room {room.name}")
                                window.turn_on()

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation:
# 
# - **Initialization**: The script initializes the home plan and iterates over each room to get the necessary sensors and actuators (AC, windows, doors).
# - **AC Control**: If any AC unit is on in a room, it ensures all windows and doors in that room are closed.
# - **Temperature Check**: It checks the indoor and outdoor temperatures. If the indoor temperature is above a high threshold and the outdoor temperature is lower, it prompts the user to open a window.
# - **Window Control**: If the user agrees, it opens a window to allow natural cooling.
# 
# This implementation should be saved in `function.py` inside the `functions` folder. Make sure to have the appropriate logging configuration in your project to capture the log outputs.