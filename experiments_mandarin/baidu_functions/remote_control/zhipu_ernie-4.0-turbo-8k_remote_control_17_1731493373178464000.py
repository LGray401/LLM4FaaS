# Based on your functional description and the provided source code, I will create a `function.py` file that contains the main function to turn off the living room light. Here's the implementation:
# 
# ### function.py

from home.home_plan import home_plan, get_room, get_room_actuators
from home.actuator import Light

def turn_off_living_room_light():
    # Get the home plan
    home = home_plan()
    
    # Get the living room
    living_room = get_room(home, "LivingRoom")
    
    if living_room:
        # Get the actuators in the living room
        actuators = get_room_actuators(home, "LivingRoom")
        
        if actuators:
            # Iterate through the actuators to find the light and turn it off
            for actuator in actuators:
                if isinstance(actuator, Light):
                    if actuator.status == "on":
                        actuator.turn_off()
                        print(f"Light {actuator.id} in LivingRoom has been turned off.")
                    else:
                        print(f"Light {actuator.id} in LivingRoom is already off.")
        else:
            print("No actuators found in the LivingRoom.")
    else:
        print("LivingRoom not found in the home plan.")

if __name__ == "__main__":
    turn_off_living_room_light()