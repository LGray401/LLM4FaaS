# To achieve the function of "关闭客厅的灯" (which means "turn off the lights in the living room"), we need to create a `function.py` file in the `functions` folder. This file will contain the `main` function, which will use the classes and methods from your existing project files to turn off the lights in the living room. 
# 
# Here's a `function.py` script that does that:
# 
# ```python
from home.home_plan import home_plan, get_room_actuators

def main():
    # Create a home plan which includes all the rooms and components
    home = home_plan()

    # Retrieve actuators specifically for the LivingRoom
    living_room_actuators = get_room_actuators(home, "LivingRoom")

    if living_room_actuators is not None:
        # Iterate through the actuators in the living room
        for actuator in living_room_actuators:
            # Check if the actuator is a Light
            if actuator.actuator_type == "Light":
                # Turn off the light
                actuator.turn_off()
    else:
        print("No actuators found in the Living Room.")

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation:
# 
# 1. **Import Necessary Functions**: We import `home_plan` and `get_room_actuators` from `home_plan.py` to create the home structure and retrieve actuators for a specific room, respectively.
# 
# 2. **Create Home Plan**: We call `home_plan()` to instantiate the rooms and components of the home.
# 
# 3. **Get Living Room Actuators**: We use `get_room_actuators` to get a list of actuators in the "LivingRoom".
# 
# 4. **Turn Off the Lights**: We iterate through the actuators in the living room, check if each actuator is a "Light", and if so, turn it off using the `turn_off` method.
# 
# 5. **Execution**: The `main` function is executed if this script is run directly.
# 
# You can place this `function.py` file inside the `functions` folder, and it should be able to control the lights in your smart home project as described.