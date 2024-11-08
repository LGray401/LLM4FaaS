from home.home_plan import get_room, get_room_actuators
from home.actuator import Light
from home.logger_config import logger

def main():
    home = get_room(get_room_actuators(home, "LivingRoom"))
    
    for actuator in home:
        if actuator.actuator_type == "Light":
            light = Light(actuator.room_name)
            light.turn_off()
            logger.info(f"Turned off the light in the {actuator.room_name}")
            print(f"Turned off the light in the {actuator.room_name}")
            break

if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Import Necessary Modules:**
#    - `from home.home_plan import get_room, get_room_actuators`: Imports functions to retrieve the "LivingRoom" and its actuators from your home plan.
#    - `from home.actuator import Light`: Imports the `Light` class to interact with lights.
#    - `from home.logger_config import logger`: Imports your logger for logging events.

# 2. **`main` Function:**
#    - `home = get_room(get_room_actuators(home, "LivingRoom"))`: This line retrieves the "LivingRoom" and its actuators. 
#       - It first calls `get_room_actuators` to get all actuators in the "LivingRoom."
#       - Then, it calls `get_room` again to access the "LivingRoom" object itself (since `get_room_actuators` likely returns a list of actuators).
#    - `for actuator in home:`: This loop iterates through the actuators in the "LivingRoom."
#    - `if actuator.actuator_type == "Light":`:  Checks if the current actuator is a `Light`.
#    - `light = Light(actuator.room_name)`: Creates a `Light` object with the room name.
#    - `light.turn_off()`: Turns off the light.
#    - `logger.info(f"Turned off the light in the {actuator.room_name}")`: Logs the action.
#    - `print(f"Turned off the light in the {actuator.room_name}")`: Prints a message to the console.
#    - `break`: Exits the loop after finding the first light.

# 3. **`if __name__ == "__main__":` Block:**
#    - This block ensures that the `main` function is only executed when the script is run directly, not when imported as a module.

# **How to Use:**

# 1. **Place the `function.py` file in the `functions` folder:** Make sure the `functions` folder exists in your project directory.
# 2. **Run the `function.py` script:** Use the command `python functions/function.py` in your terminal.
# 3. **Review Logs:** Check your log file for details about the action.

# **Important:**

# - This code assumes you have already defined the `home` object in your `home_plan.py` file.
# - Adjust the `room_name` in the `get_room_actuators` function if you need to target a different room.
# - Consider using a more descriptive variable name than `home` (e.g., `smart_home`).
# - This is a simple example; you can extend it with additional logic to handle different actuator types and scenarios.
