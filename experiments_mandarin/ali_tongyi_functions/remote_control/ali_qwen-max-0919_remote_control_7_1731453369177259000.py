# Based on your functional description, you want to create a `function.py` file that will dim the lights in the bedroom. The `function.py` should be placed in the `functions` folder and contain the main function to achieve this. Here is the implementation:
# 
# ### `function.py`

from home.home_plan import home_plan, get_room_actuators

def dim_bedroom_lights():
    # Create the home plan
    home = home_plan()

    # Get the actuators in the bedroom
    bedroom_actuators = get_room_actuators(home, "Bedroom")

    # Find and set the brightness level of the lights to 'low'
    for actuator in bedroom_actuators:
        if actuator.actuator_type == "Light":
            if actuator.status == "on":
                actuator.set_brightness_level("low")
            else:
                print(f"Light {actuator.id} is OFF. Please turn it on before setting the brightness level.")
                # You can also choose to turn on the light and then set the brightness level
                # actuator.turn_on()
                # actuator.set_brightness_level("low")

if __name__ == "__main__":
    dim_bedroom_lights()