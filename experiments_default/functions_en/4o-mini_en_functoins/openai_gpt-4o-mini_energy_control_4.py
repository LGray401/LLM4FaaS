# Based on the provided functional description and source code files, I'll create a `function.py` file that implements the required functionality to open windows to cool down based on the current temperature readings. 
# 
# This implementation will include:
# 1. Initialization of the home with rooms and their components.
# 2. Reading the outdoor temperature.
# 3. If the outdoor temperature is lower than a specified threshold, the windows will be opened.
# 
# Here's how the `function.py` file looks:

# function.py
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW
from home.actuator import Window
from home.logger_config import logger

def open_windows_to_cool_down():
    # Get the home plan
    home = home_plan()
    
    # Get all outdoor temperature sensors
    outdoor_temp_sensors = get_all_sensors(home, "OutdoorTemperature")
    
    # Assuming we only need one outdoor temperature sensor
    if outdoor_temp_sensors:
        outdoor_sensor = outdoor_temp_sensors[0]
        outdoor_sensor.turn_on()  # Turn on the sensor to get readings
        outdoor_temperature = outdoor_sensor.get_reading()
        outdoor_sensor.turn_off()  # Turn off the sensor after reading
        
        if outdoor_temperature is not None:
            logger.info(f"Outdoor temperature is {outdoor_temperature}°C.")
            print(f"Outdoor temperature is {outdoor_temperature}°C.")
            
            # Check if the outdoor temperature is below the threshold
            if outdoor_temperature < TEMP_LOW:
                # Open all windows in the house
                all_windows = get_all_actuators(home, "Window")
                for window in all_windows:
                    window.turn_on()  # Simulate opening the window
                    print(f"{window.id} is opened to cool down the house.")
                    logger.info(f"{window.id} is opened to cool down the house.")
            else:
                print("Outdoor temperature is not low enough to open windows.")
                logger.info("Outdoor temperature is not low enough to open windows.")
        else:
            print("Failed to read outdoor temperature.")
            logger.error("Failed to read outdoor temperature.")
    else:
        print("No outdoor temperature sensors found.")
        logger.warning("No outdoor temperature sensors found.")

def main():
    open_windows_to_cool_down()

if __name__ == "__main__":
    main()