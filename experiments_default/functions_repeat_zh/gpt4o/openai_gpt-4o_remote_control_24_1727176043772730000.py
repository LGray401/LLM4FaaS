# Sure, based on your functional description "请把卧室的灯关了" (which translates to "Please turn off the bedroom lights"), I will create a 'function.py' file under the 'functions' folder with the main function that turns off the light in the bedroom.
# 
# Here is the 'function.py' file:

from home.home_plan import home_plan, get_room_actuators
from home.actuator import Light

def main():
    # Create home plan
    home = home_plan()
    
    # Get all actuators in the bedroom
    bedroom_actuators = get_room_actuators(home, "Bedroom")
    
    # Iterate through the actuators to find the lights and turn them off
    for actuator in bedroom_actuators:
        if isinstance(actuator, Light):
            actuator.turn_off()

if __name__ == "__main__":
    main()