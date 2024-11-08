# Based on your functional description and provided source code, I will create a `function.py` file that includes a main function to control the smart home system according to the modes: Sleep Mode, Wake-up Mode, Lights Off Mode, and Windows Closed Mode. The main function will use the classes from the `sensor.py` and `actuator.py` files to interact with the sensors and actuators.
# 
# Here's the `function.py`:

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'home'))
from sensor import Sensor
from actuator import Actuator
from home_plan import home_plan
from home.logger_config import logger

def sleep_mode():
    logger.info("Entering Sleep Mode")
    # Turn off all lights and heating/cooling systems
    lights = get_all_actuators(home_plan(), "Light")
    for light in lights:
        light.turn_off()

    heaters = get_all_actuators(home_plan(), "Heater")
    for heater in heaters:
        heater.turn_off()

    acs = get_all_actuators(home_plan(), "AC")
    for ac in acs:
        ac.turn_off()

    # Close all windows and curtains
    windows = get_all_actuators(home_plan(), "Window")
    for window in windows:
        window.turn_on()

    curtains = get_all_actuators(home_plan(), "Curtain")
    for curtain in curtains:
        curtain.turn_on()

def wake_up_mode():
    logger.info("Entering Wake-up Mode")
    # Turn on lights and heating/cooling systems
    lights = get_all_actuators(home_plan(), "Light")
    for light in lights:
        light.turn_on()

    heaters = get_all_actuators(home_plan(), "Heater")
    for heater in heaters:
        heater.turn_on()

    acs = get_all_actuators(home_plan(), "AC")
    for ac in acs:
        ac.turn_on()

    # Open all windows and curtains
    windows = get_all_actuators(home_plan(), "Window")
    for window in windows:
        window.turn_off()

    curtains = get_all_actuators(home_plan(), "Curtain")
    for curtain in curtains:
        curtain.turn_off()

def lights_off_mode():
    logger.info("Entering Lights Off Mode")
    # Turn off all lights
    lights = get_all_actuators(home_plan(), "Light")
    for light in lights:
        light.turn_off()

def windows_closed_mode():
    logger.info("Entering Windows Closed Mode")
    # Close all windows
    windows = get_all_actuators(home_plan(), "Window")
    for window in windows:
        window.turn_on()

def main(mode):
    if mode == "sleep":
        sleep_mode()
    elif mode == "wake_up":
        wake_up_mode()
    elif mode == "lights_off":
        lights_off_mode()
    elif mode == "windows_closed":
        windows_closed_mode()
    else:
        logger.error("Invalid mode specified")
        print("Invalid mode specified")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        logger.error("Usage: python function.py <mode>")
        print("Usage: python function.py <mode>")
    else:
        mode = sys.argv[1]
        main(mode)