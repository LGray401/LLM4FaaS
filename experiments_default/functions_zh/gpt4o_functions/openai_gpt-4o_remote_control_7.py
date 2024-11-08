# Below is the 'function.py' file located in the 'functions' folder. This file includes the main function to dim the bedroom light as per the provided functional description.
# 
# ### functions/function.py

from home.home_plan import home_plan, get_room_actuators
from home.actuator import Light

def dim_bedroom_light():
    home = home_plan()
    bedroom_actuators = get_room_actuators(home, "Bedroom")
    
    for actuator in bedroom_actuators:
        if isinstance(actuator, Light):
            actuator.turn_on()  # Ensure the light is on before setting brightness
            actuator.set_brightness_level("low")
            print(f"Dimmed the light in {actuator.room_name} to low brightness.")
            return

    print("No light actuator found in the Bedroom.")

if __name__ == "__main__":
    dim_bedroom_light()