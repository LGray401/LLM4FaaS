# Based on the provided functional description and source code, I will create a `function.py` file that implements the following logic:
# 
# 1. When the AC is turned on, automatically close all windows and doors.
# 2. If the indoor temperature is higher than the target set by the AC and the outdoor temperature is lower than the indoor temperature, prompt the user to ask if they want to open the windows for cooling.
# 
# Here’s the implementation for `function.py`:
# 
# ```python
# function.py

from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.actuator import AC, Window, Door
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor
from home.logger_config import logger

def main():
    home = home_plan()

    # Assume we are working with the LivingRoom for this example
    living_room = next(room for room in home if room.name == "LivingRoom")

    # Get the AC and window/door actuators
    ac = next(actuator for actuator in living_room.actuators if isinstance(actuator, AC))
    windows = get_all_actuators(home, "Window")
    doors = get_all_actuators(home, "Door")

    # Turn on the AC
    ac.turn_on()

    # Close all windows and doors when the AC is turned on
    for window in windows:
        window.turn_off()
    for door in doors:
        door.lock()

    # Get indoor and outdoor temperature readings
    indoor_temp_sensor = next(sensor for sensor in living_room.sensors if isinstance(sensor, IndoorTemperatureSensor))
    outdoor_temp_sensor = next(sensor for sensor in living_room.sensors if isinstance(sensor, OutdoorTemperatureSensor))

    indoor_temp = indoor_temp_sensor.get_reading()
    outdoor_temp = outdoor_temp_sensor.get_reading()

    # Check if indoor temperature is higher than outdoor temperature
    if indoor_temp is not None and outdoor_temp is not None:
        if indoor_temp > outdoor_temp:
            # Prompt user to open the window
            open_window = input(f"The indoor temperature is {indoor_temp}°C and the outdoor temperature is {outdoor_temp}°C. Do you want to open the windows for cooling? (yes/no): ")
            if open_window.lower() == 'yes':
                for window in windows:
                    window.turn_on()
                    logger.info(f"Opened {window.id} for cooling.")
            else:
                logger.info("Windows remain closed.")
        else:
            logger.info("Indoor temperature is lower than or equal to outdoor temperature, no action needed.")

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation:
# - The `main` function initializes the home plan and retrieves the necessary sensors and actuators.
# - When the AC is turned on, it automatically closes all windows and locks the doors.
# - It takes readings from the indoor and outdoor temperature sensors.
# - If the indoor temperature is higher than the outdoor temperature, it prompts the user to decide whether to open the windows for cooling. Based on the user's response, it either opens the windows or keeps them closed.
# 
# This implementation assumes a command-line interaction for user input for the window opening decision. Make sure that you adapt the input method if you're implementing this in a different environment (like a web app or GUI).