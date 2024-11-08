# Based on the functional description you provided and the existing source code for your smart home project, I'll create the `function.py` file. This file will implement the required functionalities to manage the AC and window based on the temperature readings.
# 
# Below is the code for `function.py`:

# functions/function.py

from home.home_plan import home_plan
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor
from home.actuator import AC, Window
import time

def manage_room_conditions(home):
    for room in home:
        # Get the indoor temperature sensor and outdoor temperature sensor
        indoor_temp_sensor = next((sensor for sensor in room.sensors if isinstance(sensor, IndoorTemperatureSensor)), None)
        outdoor_temp_sensor = next((sensor for sensor in room.sensors if isinstance(sensor, OutdoorTemperatureSensor)), None)
        
        # Get the window actuator
        window = next((actor for actor in room.actuators if isinstance(actor, Window)), None)

        # Get the AC actuator
        ac = next((actor for actor in room.actuators if isinstance(actor, AC)), None)

        # Ensure we have the necessary components
        if indoor_temp_sensor and outdoor_temp_sensor and window and ac:
            # Get the current temperature readings
            indoor_temp = indoor_temp_sensor.get_reading()
            outdoor_temp = outdoor_temp_sensor.get_reading()
            
            # If AC is turned on, close the window
            if ac.get_status() == "on":
                window.turn_off()
                print(f"Window in {room.name} is closed because the AC is ON.")
            
            # If indoor temperature is greater than 26°C and outdoor temperature is less than 26°C, open the window
            if indoor_temp is not None and outdoor_temp is not None:
                if indoor_temp > 26 and outdoor_temp < 26:
                    window.turn_on()
                    print(f"Window in {room.name} is opened because indoor temp ({indoor_temp}°C) > 26°C and outdoor temp ({outdoor_temp}°C) < 26°C.")

def main():
    home = home_plan()  # Create the home layout
    while True:
        manage_room_conditions(home)  # Manage conditions in each room
        time.sleep(5)  # Wait for a while before checking again

if __name__ == "__main__":
    main()