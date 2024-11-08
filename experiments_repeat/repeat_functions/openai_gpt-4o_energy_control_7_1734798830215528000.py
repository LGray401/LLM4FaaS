# To fulfill your requirements, we need to create a `function.py` file in the `functions` folder. This file will contain the main function that integrates the functionality outlined in your description:
# 
# 1. Automatically close doors and windows when the air conditioner (AC) is turned on.
# 2. If the indoor temperature is high and the outdoor temperature is low, prompt the user about opening windows to reduce the temperature.
# 
# Here’s how the `function.py` file can be structured:
# 
# ```python
from home.home_plan import home_plan, get_room_actuators, get_room_sensors
from home.actuator import AC, Window, Door
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor

def main():
    # Create the home plan
    home = home_plan()

    # Iterate over each room in the home
    for room in home:
        # Get AC actuators in the room
        ac_units = [a for a in room.actuators if isinstance(a, AC)]
        # Get windows and doors in the room
        windows_and_doors = [a for a in room.actuators if isinstance(a, (Window, Door))]
        
        # Get temperature sensors in the room
        indoor_temp_sensors = [s for s in room.sensors if isinstance(s, IndoorTemperatureSensor)]
        outdoor_temp_sensors = [s for s in room.sensors if isinstance(s, OutdoorTemperatureSensor)]

        # Check if any AC is turned on
        for ac in ac_units:
            if ac.get_status() == "on":
                # Close all windows and doors when AC is on
                for wd in windows_and_doors:
                    wd.turn_off()

        # Check temperature conditions to suggest opening windows
        for indoor_sensor in indoor_temp_sensors:
            indoor_temp = indoor_sensor.get_reading()
            if indoor_temp is None:
                continue
            for outdoor_sensor in outdoor_temp_sensors:
                outdoor_temp = outdoor_sensor.get_reading()
                if outdoor_temp is None:
                    continue
                
                # If indoor temperature is high and outdoor temperature is low, prompt user
                if indoor_temp > 25 and outdoor_temp < 15:
                    print(f"Consider opening windows in {room.name} to reduce temperature.")

if __name__ == "__main__":
    main()
# ```
# 
# ### How This Code Works:
# - **Home Plan Initialization**: We start by initializing the home layout using `home_plan()`, which provides us with all rooms and their associated sensors and actuators.
# - **Iterate Through Each Room**: For each room, we retrieve actuators (AC, windows, and doors) and sensors (indoor and outdoor temperature sensors).
# - **AC Status Check**: If any AC unit is turned on, we turn off (close) all windows and doors for that room to ensure efficient cooling.
# - **Temperature Check**: If the indoor temperature is higher than 25°C and the outdoor temperature is lower than 15°C, we print a suggestion to open the windows for natural cooling.
# 
# ### Note:
# - The code assumes that the `turn_off()` method correctly closes the windows and doors, and that the `get_reading()` method provides the current temperature readings.
# - The `main()` function is designed to be the entry point of the script, allowing it to be executed directly.
# 
# Place this script in the `functions` folder as `function.py`. Ensure all necessary modules and classes are correctly imported from your existing project structure.