# To create a `function.py` file that dims the bedroom light, we need to write a script that interacts with the smart home system. The script will:
# 
# 1. Use the home plan to locate the bedroom.
# 2. Retrieve the light actuators in the bedroom.
# 3. Set their brightness to a lower level.
# 
# Here is the `function.py` file content which should be placed in the `functions` folder:
# 
# ```python
from home.home_plan import home_plan, get_room_actuators
from home.actuator import Light

def main():
    # Initialize home plan
    home = home_plan()

    # Get the actuators in the Bedroom
    bedroom_actuators = get_room_actuators(home, "Bedroom")

    if bedroom_actuators is not None:
        for actuator in bedroom_actuators:
            if isinstance(actuator, Light):
                # Turn on the light if it is off
                if actuator.get_status() != "on":
                    actuator.turn_on()
                
                # Dim the light to 'low' brightness
                actuator.set_brightness_level("low")
    else:
        print("No actuators found in the Bedroom.")

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation:
# - **home_plan**: This function is used to create and return the entire home setup.
# - **get_room_actuators**: This function fetches all actuators in a specified room, in this case, "Bedroom".
# - **Light**: This is the actuator class responsible for controlling lights. We check if each actuator is an instance of `Light`.
# - **set_brightness_level**: The method is used to set the brightness level of the light. In this case, we set it to "low" to dim the light.
# 
# This script first ensures that the light is turned on, and then it sets the brightness to "low" to achieve the dimming effect. Make sure the required modules and classes are correctly imported and available in the specified directories.