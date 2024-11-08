from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor
from home.actuator import AC, Window
from home.config import TEMP_HIGH

def main():
    home = home_plan()

    living_room = get_room(home, "LivingRoom")

    if living_room:
        # Get the indoor temperature sensor in the living room
        indoor_temp_sensor = get_room_sensors(home, "LivingRoom")[0]

        # Get the AC in the living room
        ac = get_room_actuators(home, "LivingRoom")[1]

        # Get all windows in the living room
        windows = get_room_actuators(home, "LivingRoom")[3:5]  # Index 3 and 4 are the windows

        # Check if the indoor temperature is above the threshold
        if indoor_temp_sensor.get_reading() > TEMP_HIGH:
            print("Indoor temperature is above the threshold. Turning on AC and opening windows.")
            ac.turn_on()
            ac.set_target_temperature(TEMP_HIGH - 1)  # Set target temperature to 1 degree lower than threshold

            # Open all windows
            for window in windows:
                window.turn_on()

        else:
            print("Indoor temperature is below the threshold. Turning off AC and closing windows.")
            ac.turn_off()

            # Close all windows
            for window in windows:
                window.turn_off()

if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Import necessary modules:**
#    - `home.home_plan`: This module contains functions to manage the home plan, including finding rooms, sensors, and actuators.
#    - `home.sensor`: This module contains the `IndoorTemperatureSensor` and `HumiditySensor` classes.
#    - `home.actuator`: This module contains the `AC` and `Window` classes.
#    - `home.config`: This module contains the `TEMP_HIGH` configuration value.

# 2. **Define the `main()` function:**
#    - Creates a `home` object using `home_plan()`.
#    - Finds the "LivingRoom" using `get_room()`.
#    - Gets the indoor temperature sensor and AC from the living room using `get_room_sensors()` and `get_room_actuators()`.
#    - Gets all windows in the living room using indexing.
#    - Checks if the indoor temperature is above the `TEMP_HIGH` threshold.
#    - If above the threshold:
#      - Prints a message.
#      - Turns on the AC using `ac.turn_on()`.
#      - Sets the AC target temperature 1 degree lower than the threshold using `ac.set_target_temperature()`.
#      - Opens all windows using a loop.
#    - If below the threshold:
#      - Prints a message.
#      - Turns off the AC using `ac.turn_off()`.
#      - Closes all windows using a loop.

# 3. **Run the `main()` function:**
#    - The `if __name__ == "__main__":` block ensures that the `main()` function is called only when the script is executed directly.

# **Key Improvements:**

# - **Modular design:** The code is organized into functions, making it more readable and maintainable.
# - **Clear logic:** The logic for turning on/off the AC and windows based on the indoor temperature is well-defined.
# - **Use of configuration values:** The `TEMP_HIGH` threshold is defined in the `config.py` file, making it easy to adjust.
# - **Error handling:** The code checks if the "LivingRoom" exists before accessing its sensors and actuators.

# This code demonstrates how to use the provided modules to control devices based on sensor readings. You can expand on this example to implement more complex logic and control other actuators in your smart home system. 
