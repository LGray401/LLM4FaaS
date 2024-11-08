# Based on your functional description of dimming the bedroom lights, I will create a `function.py` file that will contain the main function to accomplish this task. The function will interact with the `Light` actuator to set the brightness to a lower level.
# 
# Here's the content of `function.py`:

# functions/function.py

from home.home_plan import home_plan
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.actuator import Light

def dim_bedroom_lights():
    # Get the home plan
    home = home_plan()
    
    # Get the Bedroom room
    bedroom = next((room for room in home if room.name == "Bedroom"), None)
    
    if bedroom is not None:
        # Get all Light actuators in the Bedroom
        lights = [actuator for actuator in bedroom.actuators if isinstance(actuator, Light)]
        
        # Dim each light found
        for light in lights:
            light.turn_on()  # Ensure the light is on before adjusting brightness
            light.set_brightness_level("low")  # Set brightness to low
    else:
        print("Bedroom not found in the home plan.")

def main():
    print("Dimming bedroom lights...")
    dim_bedroom_lights()

if __name__ == "__main__":
    main()