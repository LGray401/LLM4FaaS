# Based on your project structure and functional description, we'll create a `function.py` file that will open windows and turn off air conditioning. We'll utilize the classes and methods from `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py` to achieve this functionality.
# 
# Here's the `function.py` file:
# 
# ## function.py

from home.home_plan import home_plan, get_all_actuators
from home.actuator import Window, AC
from home.logger_config import logger

def main():
    # Initialize the home plan
    home = home_plan()

    # Get all windows in the home
    windows = get_all_actuators(home, "Window")

    # Get all ACs in the home
    acs = get_all_actuators(home, "AC")

    # Open all windows
    for window in windows:
        if window.get_status() == "off":  # Check if the window is closed
            window.turn_on()  # Open the window
            logger.info(f"Window {window.id} is now open.")

    # Turn off all ACs
    for ac in acs:
        if ac.get_status() == "on":  # Check if the AC is on
            ac.turn_off()  # Turn off the AC
            logger.info(f"AC {ac.id} is now off.")

if __name__ == "__main__":
    main()