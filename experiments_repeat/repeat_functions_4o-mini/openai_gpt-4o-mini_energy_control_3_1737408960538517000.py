# Based on your functional description of "开窗关空调," which translates to "open the window and turn off the air conditioner," I will create a `function.py` file. This file will include a main function that manages the interaction between the window actuator and the air conditioner actuator based on the sensor readings.
# 
# Here's the content for `function.py`:
# 
# ```python
# function.py
from home.home_plan import home_plan
from home.config import TEMP_HIGH
from home.actuator import AC, Window
from home.sensor import IndoorTemperatureSensor


def open_window_and_turn_off_ac(home):
    # Get the room and its components
    living_room = next((room for room in home if room.name == "LivingRoom"), None)

    if living_room is None:
        print("Living Room not found in the home plan.")
        return

    # Find the window and AC actuators
    window = next((actuator for actuator in living_room.actuators if isinstance(actuator, Window)), None)
    ac = next((actuator for actuator in living_room.actuators if isinstance(actuator, AC)), None)

    # Find the indoor temperature sensor
    temp_sensor = next((sensor for sensor in living_room.sensors if isinstance(sensor, IndoorTemperatureSensor)), None)

    if window:
        window.turn_on()  # Open the window
    else:
        print("No window actuator found in the Living Room.")

    if ac:
        current_temp = temp_sensor.get_reading()
        if current_temp is not None and current_temp > TEMP_HIGH:
            ac.turn_off()  # Turn off the air conditioner
        else:
            print("The air conditioner is already off or the temperature is within range.")
    else:
        print("No air conditioner actuator found in the Living Room.")


def main():
    home = home_plan()  # Create the home plan
    open_window_and_turn_off_ac(home)  # Execute the function


if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation of the Code:
# 1. **Import Statements**: It imports necessary classes and constants from other modules.
# 2. **Function `open_window_and_turn_off_ac`**:
#    - This function locates the Living Room, the window actuator, the air conditioner actuator, and the indoor temperature sensor.
#    - It opens the window by turning on the window actuator.
#    - It retrieves the current temperature reading from the indoor temperature sensor.
#    - If the temperature is above the defined `TEMP_HIGH` threshold, it turns off the air conditioner.
# 3. **Main Function**:
#    - It creates the home plan by calling `home_plan()` and then calls the `open_window_and_turn_off_ac` function to perform the required actions.
# 4. **Entry Point**: The standard if-statement to check if the script is being run directly.
# 
# You can save this code as `function.py` in your `functions` folder. This will allow you to interact with the smart home system to open the window and turn off the AC based on the current indoor temperature.