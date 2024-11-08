from home.home_plan import home_plan, get_room, get_room_actuators
from home.actuator import AC

def main():
    home = home_plan()
    living_room = get_room(home, "LivingRoom")
    if living_room:
        living_room_actuators = get_room_actuators(home, "LivingRoom")
        for actuator in living_room_actuators:
            if isinstance(actuator, AC):
                actuator.set_target_temperature(26)
                actuator.turn_on()
                break
        else:
            print("No AC found in the living room.")

if __name__ == "__main__":
    main()

# This `function.py` file does the following:

# 1. **Imports necessary modules:**
#    - `home.home_plan`: To access functions for creating the home plan and retrieving rooms and actuators.
#    - `home.actuator`: To work with the `AC` actuator class.

# 2. **Defines the `main` function:**
#    - Calls `home_plan()` to create the home structure.
#    - Uses `get_room()` to find the "LivingRoom".
#    - If "LivingRoom" is found:
#      - Gets the actuators in the living room using `get_room_actuators()`.
#      - Iterates through the actuators:
#        - If an actuator is an `AC` instance:
#          - Sets the target temperature using `actuator.set_target_temperature(26)`.
#          - Turns on the AC using `actuator.turn_on()`.
#          - Exits the loop (using `break`) because we've found the desired AC.
#    - If "LivingRoom" is not found, prints a message.

# 3. **Executes `main` if the script is run directly:**
#    - The `if __name__ == "__main__":` block ensures that `main` is called only when the script is run directly, not when imported as a module.

# **How to use:**

# 1. Place this `function.py` file in the `functions` folder of your project.
# 2. Ensure the other files (`sensor.py`, `actuator.py`, `home_plan.py`, and `config.py`) are in the `home` folder.
# 3. Run `function.py` (e.g., `python functions/function.py`). 

# This will turn on the AC in the living room and set its temperature to 26 degrees.
