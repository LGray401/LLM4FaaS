# Based on the functional description and the provided source code, I will create a `function.py` file that incorporates the logic for controlling the AC and windows according to the specified conditions.
# 
# The `function.py` file will contain a main function that checks the temperature readings and controls the AC and windows accordingly. Here's how the file will look:

# functions/function.py

from home.home_plan import home_plan
from home.config import TEMP_LOW, TEMP_HIGH
import time

def control_climate(home):
    while True:
        for room in home:
            # Get the relevant sensors and actuators
            indoor_temp_sensor = next((s for s in room.sensors if isinstance(s, IndoorTemperatureSensor)), None)
            outdoor_temp_sensor = next((s for s in room.sensors if isinstance(s, OutdoorTemperatureSensor)), None)
            ac = next((a for a in room.actuators if isinstance(a, AC)), None)
            window = next((a for a in room.actuators if isinstance(a, Window)), None)

            # Check if sensors and actuators are present
            if indoor_temp_sensor and outdoor_temp_sensor and ac and window:
                indoor_temp = indoor_temp_sensor.get_reading()
                outdoor_temp = outdoor_temp_sensor.get_reading()

                if indoor_temp is not None and outdoor_temp is not None:
                    # Condition 1: When AC is turned on, close the window
                    if ac.get_status() == "on":
                        window.turn_off()
                    
                    # Condition 2: If indoor temperature exceeds 26°C and outdoor is below 26°C, open the window
                    if indoor_temp > 26 and outdoor_temp < 26:
                        window.turn_on()
                    else:
                        window.turn_off()

        time.sleep(5)  # Wait before checking again

def main():
    home = home_plan()
    control_climate(home)

if __name__ == "__main__":
    main()