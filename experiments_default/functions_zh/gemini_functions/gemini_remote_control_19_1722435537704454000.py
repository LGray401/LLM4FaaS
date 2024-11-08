from home.home_plan import home_plan, get_room, get_room_actuators
from home.actuator import AC
from home.logger_config import logger

def main():
    home = home_plan()
    living_room = get_room(home, "LivingRoom")
    if living_room:
        living_room_actuators = get_room_actuators(home, "LivingRoom")
        for actuator in living_room_actuators:
            if actuator.actuator_type == "AC":
                ac = actuator
                ac.turn_on()
                ac.set_target_temperature(26)
                logger.info("Turned on the AC in the Living Room and set the target temperature to 26 degrees.")
                print("Turned on the AC in the Living Room and set the target temperature to 26 degrees.")

if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Imports:**
#    - `home.home_plan`: Imports the `home_plan` function to create the home layout.
#    - `home.actuator`: Imports the `AC` class to interact with the air conditioner.
#    - `home.logger_config`: Imports the `logger` object for logging messages.

# 2. **`main` Function:**
#    - **Create Home Plan:** Calls `home_plan()` to get the home layout.
#    - **Get Living Room:** Uses `get_room` to find the "LivingRoom" object.
#    - **Find AC:** Iterates through the actuators in the Living Room and finds the AC (assuming only one AC in the room).
#    - **Turn On and Set Temperature:**
#       - Calls `turn_on()` on the AC object.
#       - Calls `set_target_temperature(26)` to set the desired temperature.
#    - **Log Success:** Logs a message indicating that the AC is turned on and the temperature is set.

# 3. **Running the Code:**
#    - The `if __name__ == "__main__":` block ensures that the code within it runs only when the file is executed directly (not imported as a module).
#    - The `main()` function is called, which performs the operations described above.

# **To use this function.py file:**

# 1. Make sure you have the `home` folder with the `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py` files.
# 2. Create a `functions` folder and place this `function.py` file in it.
# 3. Run the `function.py` file.

# This will turn on the AC in the Living Room and set its target temperature to 26 degrees Celsius. The `logger` object will log the action.
