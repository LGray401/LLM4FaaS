# Based on your requirements, I'll create a `function.py` file that contains a `main` function to turn off the lights in the bedroom. The `main` function will use the classes and methods provided in the other modules to achieve this functionality.
# 
# Here's the `function.py` file located in the `functions` folder:

# functions/function.py

from home.home_plan import home_plan, get_room_actuators
from home.actuator import Light

def main():
    # Create the home setup
    home = home_plan()
    
    # Get the actuators in the bedroom
    bedroom_actuators = get_room_actuators(home, "Bedroom")
    
    if bedroom_actuators:
        # Iterate through the actuators and turn off the lights
        for actuator in bedroom_actuators:
            if isinstance(actuator, Light):
                actuator.turn_off()
        print("卧室的灯已关")
    else:
        print("卧室里没有找到任何执行器")

if __name__ == "__main__":
    main()