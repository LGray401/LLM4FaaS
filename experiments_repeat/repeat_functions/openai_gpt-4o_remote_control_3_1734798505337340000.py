# To fulfill the functional description "关闭客厅的灯" (which means "turn off the living room lights" in English), we can create a `function.py` file that locates the lights in the living room and turns them off. Below is the code for the `function.py` file:
# 
# ```python
# functions/function.py

from home.home_plan import home_plan, get_room_actuators

def main():
    # Load the home plan
    home = home_plan()

    # Get all actuators in the living room
    living_room_actuators = get_room_actuators(home, "LivingRoom")

    # Find the lights and turn them off
    for actuator in living_room_actuators:
        if actuator.actuator_type == "Light":
            actuator.turn_off()

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation:
# 
# 1. **Import Necessary Functions**: We import `home_plan` to create the home environment and `get_room_actuators` to fetch the actuators (devices that can be controlled) in a specific room.
# 
# 2. **Load Home Plan**: We call `home_plan()` to get the list of rooms and their components.
# 
# 3. **Get Living Room Actuators**: We use `get_room_actuators` to retrieve all actuators in the "LivingRoom".
# 
# 4. **Turn Off Lights**: We iterate over the actuators, check if the actuator type is "Light", and call `turn_off()` on each light actuator.
# 
# 5. **Run the Main Function**: The script executes the `main()` function when run as a standalone program.
# 
# Ensure that the `function.py` file is placed in the `functions` folder as specified, and it will perform the action of turning off the lights in the living room when executed.