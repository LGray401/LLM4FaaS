# Based on your functional description and the provided source code, I will create a `function.py` file that implements the required functionality: turning off doors and windows when the air conditioner is turned on, and asking whether to open the windows for cooling when the indoor temperature is high and the outdoor temperature is lower.
# 
# Here’s how you could structure the `function.py` file in the `functions` folder:
# 
# ```python
# functions/function.py

from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators
from home.config import TEMP_LOW, TEMP_HIGH
from home.actuator import AC, Window, Door
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor

def control_ac_and_windows(home):
    # Get the rooms and their sensors and actuators
    living_room = get_room(home, "LivingRoom")
    if living_room is None:
        return

    # Get the indoor and outdoor temperature sensors
    indoor_temp_sensor = next((s for s in living_room.sensors if isinstance(s, IndoorTemperatureSensor)), None)
    outdoor_temp_sensor = next((s for s in living_room.sensors if isinstance(s, OutdoorTemperatureSensor)), None)

    # Get the AC and window actuators
    ac = next((a for a in living_room.actuators if isinstance(a, AC)), None)
    windows = [a for a in living_room.actuators if isinstance(a, Window)]

    if indoor_temp_sensor is not None and outdoor_temp_sensor is not None:
        indoor_temp = indoor_temp_sensor.get_reading()
        outdoor_temp = outdoor_temp_sensor.get_reading()

        # Control Air Conditioner and Windows
        if ac is not None:
            if ac.get_status() == "off":
                ac.turn_on()  # Turn on the AC
                for window in windows:
                    window.turn_off()  # Close the windows
                print("Air Conditioner is ON, windows are closed.")
            else:
                print("Air Conditioner is already ON.")
            
            # Check temperature condition for opening windows
            if indoor_temp > TEMP_HIGH and outdoor_temp < TEMP_LOW:
                user_input = input("Indoor temperature is high and outdoor temperature is low. Do you want to open the windows for cooling? (yes/no): ")
                if user_input.lower() == 'yes':
                    for window in windows:
                        window.turn_on()  # Open the windows
                    print("Windows are opened for cooling.")
                else:
                    print("Windows remain closed.")
        else:
            print("AC is not available in the living room.")

def main():
    # Initialize home plan
    home = home_plan()
    
    # Control AC and Windows
    control_ac_and_windows(home)

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation of the Code:
# 1. **Imports**: The necessary classes and functions from the other modules are imported.
# 2. **Function `control_ac_and_windows`**:
#    - This function retrieves the Living Room components.
#    - It checks the status of the AC and the readings of the indoor and outdoor temperature sensors.
#    - If the AC is off, it turns it on and closes the windows.
#    - If the indoor temperature is high and the outdoor temperature is low, it prompts the user to decide whether to open the windows.
# 3. **`main` Function**: Initializes the home plan and calls the control function.
# 4. **Execution Block**: Calls the `main()` function when the script is executed.
# 
# This code should fulfill the requirements you've outlined in your functional description. Make sure to adjust the user input handling as needed for your specific use case, particularly if you wish to integrate it into an existing user interface or system.