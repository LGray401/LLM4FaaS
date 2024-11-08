# Based on your functional description of turning off the living room light, I will create a `function.py` file in the `functions` folder that includes a main function for this purpose. The function will locate the living room light actuator and turn it off.
# 
# Here's the content for `function.py`:

# function.py
from home.home_plan import home_plan
from home.actuator import Light

def turn_off_living_room_light():
    # Get the home plan
    home = home_plan()
    
    # Find the living room
    living_room = next((room for room in home if room.name == "LivingRoom"), None)
    
    if living_room:
        # Find the light actuator in the living room
        light_actuator = next((actuator for actuator in living_room.actuators if isinstance(actuator, Light)), None)
        
        if light_actuator:
            # Turn off the light
            light_actuator.turn_off()
        else:
            print("No light actuator found in the living room.")
    else:
        print("Living room not found in the home plan.")

def main():
    turn_off_living_room_light()

if __name__ == "__main__":
    main()