# To create the `function.py` file in the `functions` folder, we need to implement a function that closes the light in the living room. Based on the given code files, the `home_plan.py` module provides a way to access rooms and their associated actuators. We can use this to access the "LivingRoom" and its lights. Here’s how you can implement this:
# 
# ### `function.py` in the `functions` folder
# 
# ```python
from home.home_plan import home_plan, get_room_actuators
from home.actuator import Light

def main():
    # Create the home plan and get the actuators in the living room
    home = home_plan()
    living_room_actuators = get_room_actuators(home, "LivingRoom")
    
    if not living_room_actuators:
        print("No actuators found in the LivingRoom.")
        return

    # Find the lights in the living room and turn them off
    for actuator in living_room_actuators:
        if isinstance(actuator, Light):
            actuator.turn_off()
            print(f"Turned off light: {actuator.id}")

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation
# 
# 1. **Import Statements**: We import the necessary functions and classes from the `home_plan` and `actuator` modules.
# 
# 2. **Create Home Plan**: We call `home_plan()` to initialize the home setup, which returns a list of `Room` objects.
# 
# 3. **Get Living Room Actuators**: We use `get_room_actuators(home, "LivingRoom")` to retrieve the list of actuators in the living room.
# 
# 4. **Turn Off Lights**: We iterate over the actuators in the living room, checking if each actuator is an instance of the `Light` class. If it is, we call the `turn_off()` method to turn off the light and print a confirmation message.
# 
# 5. **Main Function Execution**: The `main()` function is executed if the script is run directly, turning off the lights in the living room.
# 
# Ensure that the `function.py` file is placed in the `functions` directory and that your project structure is set up correctly to match the imports. Additionally, make sure that the logging configuration (`logger_config`) is correctly set up, as it is referenced in the sensor and actuator modules.