# To create the `function.py` file as per your functional description "关闭客厅的灯" (which translates to "turn off the living room lights"), we need to implement a function that specifically targets the lights in the living room and turns them off.
# 
# Below is the implementation of the `function.py` file based on the provided source code and the functionality you described:
# 
# ```python
from home.home_plan import home_plan, get_room_actuators

def main():
    # Create the home plan which initializes all the rooms with their actuators and sensors
    home = home_plan()
    
    # Get all actuators in the Living Room
    living_room_actuators = get_room_actuators(home, "LivingRoom")
    
    if living_room_actuators:
        # Iterate through the actuators and turn off the lights
        for actuator in living_room_actuators:
            if actuator.actuator_type == "Light":
                actuator.turn_off()
                print(f"Turned off: {actuator.id}")
    else:
        print("No actuators found in the Living Room.")

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation:
# 
# 1. **Import Statements**: 
#    - We import the `home_plan` function to initialize the home with all rooms, sensors, and actuators.
#    - We import `get_room_actuators` to fetch the actuators for a specific room.
# 
# 2. **Main Function**:
#    - We call `home_plan()` to get our home setup.
#    - We use `get_room_actuators` to retrieve all actuators in the "LivingRoom".
#    - We iterate over the actuators and check if the actuator type is "Light". If it is, we call `turn_off()` on it to turn off the light.
# 
# 3. **Execution**:
#    - The `main()` function is called when the script is run directly, ensuring the lights in the living room are turned off.
# 
# This script will be placed in the 'functions' folder as `function.py`, and it will perform the task of turning off the lights in the living room when executed.