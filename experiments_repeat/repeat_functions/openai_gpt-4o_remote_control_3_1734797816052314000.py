# To create the `function.py` file according to your requirements, we need to implement a function that turns off the lights in the living room. Here's how you can achieve this by utilizing the existing classes and methods from your provided code:
# 
# 1. **Import Necessary Components**: We need to import the `home_plan` function to get the home setup and the `get_room_actuators` function to get the actuators in the living room.
# 2. **Create the Main Function**: Implement the `main()` function to execute the task of turning off the lights in the living room.
# 
# Here's the `function.py` file:
# 
# ```python
# function.py
from home.home_plan import home_plan, get_room_actuators
from home.actuator import Light

def main():
    # Retrieve the home setup
    home = home_plan()
    
    # Get actuators in the Living Room
    living_room_actuators = get_room_actuators(home, "LivingRoom")
    
    # Find light actuators and turn them off
    for actuator in living_room_actuators:
        if isinstance(actuator, Light):
            actuator.turn_off()

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation of the Code:
# 
# - **Import Statements**: We import `home_plan` to initialize the home setup and `get_room_actuators` to fetch the actuators present in specific rooms.
#   
# - **Main Function**: 
#   - We first call `home_plan()` to initialize the setup of the home, which gives us a list of `Room` objects.
#   - We then use `get_room_actuators(home, "LivingRoom")` to get all actuators in the living room.
#   - We iterate over these actuators, check if they are instances of the `Light` class, and call the `turn_off()` method on them to turn them off.
# 
# ### How to Use:
# 
# - Save this file in the `functions` folder as `function.py`.
# - Run this script to execute the main function that will turn off all the lights in the living room, as per your functional description.
# 
# This should fulfill your requirement to "关闭客厅的灯" (turn off the living room lights).