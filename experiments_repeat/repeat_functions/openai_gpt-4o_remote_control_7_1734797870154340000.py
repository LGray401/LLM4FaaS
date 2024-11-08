# To implement the required functionality of dimming the bedroom lights, we need to write a `function.py` file that will interact with the `home_plan.py` to access the bedroom's actuators and adjust the light brightness.
# 
# Here's the `function.py` file:
# 
# ```python
from home.home_plan import home_plan, get_room_actuators
from home.actuator import Light

def main():
    # Create the home plan
    home = home_plan()

    # Get actuators in the Bedroom
    bedroom_actuators = get_room_actuators(home, "Bedroom")

    # Find the lights in the Bedroom and dim them
    for actuator in bedroom_actuators:
        if isinstance(actuator, Light):
            actuator.turn_on()  # Ensure the light is on before dimming
            actuator.set_brightness_level("low")  # Dim the light

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation:
# 1. **Import Required Components**: Import necessary functions and classes from `home_plan.py` and `actuator.py`.
# 2. **Create Home Plan**: Use `home_plan()` to create the home configuration.
# 3. **Access Bedroom Actuators**: Retrieve the list of actuators for the bedroom using `get_room_actuators()`.
# 4. **Dim the Lights**: Loop through the actuators, identify `Light` instances, and set their brightness to "low". Ensure the lights are turned on before setting the brightness.
# 
# ### Instructions:
# - Save this script in the `functions` folder as `function.py`.
# - Ensure all dependencies and imports are correctly configured according to your project structure.
# - This script assumes the room name is exactly "Bedroom" as defined in the `home_plan.py`. Adjust if your setup uses different naming conventions.