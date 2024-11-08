# Based on your functional description and the provided source code, I will create a `function.py` file that will dim the lights in the bedroom. This will involve interacting with the `Light` actuator in the `Bedroom` room from the `home_plan.py`.
# 
# Here's the implementation for `function.py`:

# functions/function.py

from home.home_plan import home_plan, get_room, get_room_actuators

def dim_bedroom_lights(dim_level='low'):
    # Create the home plan
    home = home_plan()
    
    # Get the Bedroom room
    bedroom = get_room(home, "Bedroom")
    
    if bedroom is None:
        print("Bedroom not found.")
        return

    # Get all light actuators in the bedroom
    lights = get_room_actuators(home, "Bedroom")
    
    if not lights:
        print("No lights found in the Bedroom.")
        return
    
    # Dim the lights to the specified level
    for light in lights:
        light.turn_on()  # Ensure the light is on before setting brightness
        light.set_brightness_level(dim_level)

def main():
    # Dim the bedroom lights to low level
    dim_bedroom_lights('low')

if __name__ == "__main__":
    main()