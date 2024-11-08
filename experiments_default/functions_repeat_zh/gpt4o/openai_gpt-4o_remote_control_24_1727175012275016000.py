# Based on the provided functional description and the source code, you need to turn off the lights in the bedroom. I will create a `function.py` file that reads the home configuration, identifies the bedroom, and turns off all the lights in that room.
# 
# Here is the `function.py` file:

# function.py

from home.home_plan import home_plan, get_room_actuators
from home.actuator import Light

def main():
    # Create home plan
    home = home_plan()
    
    # Get actuators in the bedroom
    bedroom_actuators = get_room_actuators(home, "Bedroom")
    
    if bedroom_actuators:
        for actuator in bedroom_actuators:
            if isinstance(actuator, Light):
                actuator.turn_off()

if __name__ == "__main__":
    main()