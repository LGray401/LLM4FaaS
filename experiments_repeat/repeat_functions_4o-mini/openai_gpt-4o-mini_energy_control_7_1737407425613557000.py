# Based on your functional description and the provided source code, I will create a `function.py` file located in the `functions` folder. This file will implement the functionality where the air conditioning (AC) automatically closes doors and windows when turned on, and checks if the windows should be opened for cooling when the indoor temperature is higher than the outdoor temperature.
# 
# Here's how the `function.py` file will be structured:
# 
# 1. **Import Necessary Classes**: We will import the necessary classes from the existing modules.
# 2. **Define Main Function**:
#    - Create instances of sensors and actuators.
#    - Implement the logic to turn on the AC.
#    - Control the doors and windows based on the AC status and temperature readings.
#    - Prompt the user if the indoor temperature is high and the outdoor temperature is lower, asking whether to open the windows.
# 
# Here's the implementation of `function.py`:
# 
# ```python
# functions/function.py

from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH
from home.logger_config import logger

def main():
    # Create home layout and components
    home = home_plan()

    # Get all relevant sensors and actuators
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    outdoor_temp_sensors = get_all_sensors(home, "OutdoorTemperature")
    windows = get_all_actuators(home, "Window")
    doors = get_all_actuators(home, "Door")
    acs = get_all_actuators(home, "AC")
    
    # Assume we are working with the first instances for simplicity
    if indoor_temp_sensors and outdoor_temp_sensors and acs:
        indoor_temp_sensor = indoor_temp_sensors[0]
        outdoor_temp_sensor = outdoor_temp_sensors[0]
        ac = acs[0]
        
        # Turn on the AC
        ac.turn_on()
        
        # Close all doors and windows when AC is on
        for door in doors:
            door.turn_off()
        for window in windows:
            window.turn_off()

        # Get readings
        indoor_temp = indoor_temp_sensor.get_reading()
        outdoor_temp = outdoor_temp_sensor.get_reading()
        
        if indoor_temp is not None and outdoor_temp is not None:
            # Check if indoor temperature is higher than the outdoor temperature
            if indoor_temp > outdoor_temp:
                # Ask user if they want to open the window
                user_input = input(f"Indoor temperature is {indoor_temp}°C and outdoor temperature is {outdoor_temp}°C. "
                                   "Do you want to open the window to cool down? (yes/no): ")
                if user_input.lower() == 'yes':
                    for window in windows:
                        window.turn_on()  # Open the window
                else:
                    print("Keeping the windows closed.")
                    logger.info("User chose to keep the windows closed.")
            else:
                print("Outdoor temperature is lower or equal to indoor temperature. No need to open the windows.")
                logger.info("No need to open the windows, outdoor is cooler or equal.")

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation:
# - **Imports**: We import the necessary functions and classes from your existing modules.
# - **Main Function**: 
#   - Initializes the home plan.
#   - Retrieves indoor and outdoor temperature sensors, AC actuators, and window/door actuators.
#   - Turns on the AC and closes all doors and windows.
#   - Checks the temperature readings and prompts the user to decide if they want to open the windows when it's warmer indoors than outdoors.
# 
# ### Usage:
# You can run this script by executing `python function.py` from your terminal or command prompt while in the `functions` directory. Make sure the other components of your smart home system are set up correctly for it to work as intended.