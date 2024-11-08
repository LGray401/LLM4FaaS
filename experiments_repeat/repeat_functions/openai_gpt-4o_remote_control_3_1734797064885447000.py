# To implement the functionality described ("关闭客厅的灯" which translates to "turn off the living room lights"), we need to interact with the `Light` actuator class in the `actuator.py` file. Specifically, we will need to find the `Light` instances in the "LivingRoom" and call their `turn_off()` methods.
# 
# Let's write the `function.py` file that will accomplish this by utilizing the existing code structure.
# 
# ```python
# function.py

from home.home_plan import home_plan, get_room_actuators
from home.actuator import Light

def main():
    # Load the home plan
    home = home_plan()

    # Get all actuators in the LivingRoom
    living_room_actuators = get_room_actuators(home, "LivingRoom")

    # Iterate through each actuator in the LivingRoom
    for actuator in living_room_actuators:
        # Check if the actuator is a Light
        if isinstance(actuator, Light):
            # Turn off the light
            actuator.turn_off()

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation:
# 
# - **Import Statements**: We import necessary functions and classes from the `home_plan` and `actuator` modules.
# - **home_plan()**: This function is called to get the configuration of the home, including all rooms and their actuators.
# - **get_room_actuators()**: Retrieves the actuators in the specified room ("LivingRoom").
# - **Iterate and Check**: We iterate over the actuators in the living room and check if they are instances of the `Light` class.
# - **Turn Off Lights**: If the actuator is a `Light`, we call its `turn_off()` method to switch it off.
# - **main() Function**: This is the main function that executes the described functionality when the script is run.
# 
# This script makes use of existing code infrastructure and classes to perform its task efficiently. Ensure that the `functions` folder exists and place the `function.py` file inside it to meet your directory structure requirements.