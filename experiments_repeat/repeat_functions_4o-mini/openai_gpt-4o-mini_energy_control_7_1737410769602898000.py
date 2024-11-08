# Certainly! Below is the content for the `function.py` file based on your functional description of automatically closing windows and doors when the air conditioning (AC) is turned on, and asking whether to open the windows for cooling when the indoor temperature is higher than the outdoor temperature.
# 
# ### `function.py`
# ```python
import time
from home.home_plan import home_plan
from home.config import TEMP_LOW, TEMP_HIGH
from home.actuator import AC, Window, Door
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor

def main():
    # Initialize home with rooms and components
    home = home_plan()

    # Assume we are focusing on the Living Room for this example
    living_room = next((room for room in home if room.name == "LivingRoom"), None)
    if living_room is None:
        print("Living room not found!")
        return

    # Get the indoor and outdoor temperature sensors
    indoor_temp_sensor = next((sensor for sensor in living_room.sensors if isinstance(sensor, IndoorTemperatureSensor)), None)
    outdoor_temp_sensor = next((sensor for sensor in living_room.sensors if isinstance(sensor, OutdoorTemperatureSensor)), None)

    # Get the AC, Windows, and Doors actuators
    ac = next((actuator for actuator in living_room.actuators if isinstance(actuator, AC)), None)
    windows = [actuator for actuator in living_room.actuators if isinstance(actuator, Window)]
    doors = [actuator for actuator in living_room.actuators if isinstance(actuator, Door)]

    # Turn on AC
    ac.turn_on()
    
    # Close doors and windows when AC is turned on
    for window in windows:
        window.turn_off()
    for door in doors:
        door.turn_off()

    # Get current readings
    if indoor_temp_sensor and outdoor_temp_sensor:
        indoor_temp = indoor_temp_sensor.get_reading()
        outdoor_temp = outdoor_temp_sensor.get_reading()

        # Check if indoor temperature is higher than outdoor temperature
        if indoor_temp is not None and outdoor_temp is not None:
            print(f"Indoor Temperature: {indoor_temp}°C, Outdoor Temperature: {outdoor_temp}°C")

            if indoor_temp > outdoor_temp:
                # Prompt user to open windows for cooling
                user_response = input("Indoor temperature is higher than outdoor temperature. Do you want to open the windows for cooling? (yes/no): ")
                if user_response.lower() == 'yes':
                    for window in windows:
                        window.turn_on()
                else:
                    print("Windows remain closed.")
            else:
                print("No need to open the windows, indoor temperature is lower than or equal to outdoor temperature.")

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation:
# 1. **Initialization**: The `main()` function initializes the home layout and retrieves the relevant sensors and actuators from the Living Room.
# 2. **AC Control**: When the AC is turned on, all windows and doors are automatically turned off (closed).
# 3. **Temperature Check**: It fetches the readings from the indoor and outdoor temperature sensors.
# 4. **User Interaction**: If the indoor temperature is higher, the user is prompted to decide whether to open the windows for cooling. Depending on the user's input, the windows may be opened or kept closed.
# 
# ### Usage:
# - Place this code in the `function.py` file located in the `functions` folder of your project.
# - You can run it, and it will execute the described logic based on your smart home setup.
# 
# Feel free to modify any part of the code to better fit your project's needs!