# Based on your functional description "卧室灯调暗一些" (which translates to "dim the bedroom lights a bit"), we need to create a `function.py` file that will locate and interact with the lights in the bedroom. Here's how you can implement this functionality:
# 
# ```python
# functions/function.py

from home.home_plan import home_plan, get_room_actuators
from home.actuator import Light

def dim_bedroom_lights():
    # Get the full home plan
    home = home_plan()
    
    # Retrieve the actuators in the bedroom
    bedroom_actuators = get_room_actuators(home, "Bedroom")
    
    if not bedroom_actuators:
        print("No actuators found in the bedroom.")
        return
    
    # Find the lights in the bedroom and dim them
    for actuator in bedroom_actuators:
        if isinstance(actuator, Light):
            actuator.turn_on()  # Ensure the light is on before setting brightness
            current_status = actuator.get_status()
            
            # If the light is already on, set the brightness level to 'low'
            if current_status == "on":
                actuator.set_brightness_level("low")
            else:
                print(f"Light {actuator.id} is not on, cannot dim.")
            
if __name__ == "__main__":
    dim_bedroom_lights()
# ```
# 
# ### Explanation:
# 1. **Import Necessary Modules**: We import `home_plan` and `get_room_actuators` from `home_plan.py` to get the layout of the home and actuators in a specific room. We also import `Light` from `actuator.py`.
# 
# 2. **Define `dim_bedroom_lights` Function**:
#    - **Get Home Plan**: Retrieve the current home layout.
#    - **Get Bedroom Actuators**: Use `get_room_actuators` to fetch all actuators in the "Bedroom".
#    - **Check for Actuators**: Ensure that actuators were found in the bedroom.
#    - **Dim the Lights**: Iterate through the actuators, check if they are an instance of `Light`, and if so, turn them on and set their brightness to "low".
# 
# 3. **Main Execution**: We call `dim_bedroom_lights()` when this script is run directly.
# 
# Ensure that the `functions` directory is structured correctly relative to the `home` directory, so that the imports work properly. You can run this script, and it should dim the bedroom lights by setting their brightness level to "low".