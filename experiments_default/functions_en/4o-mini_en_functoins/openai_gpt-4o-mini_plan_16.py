# Based on the functional description and the provided source code, I'll create a `function.py` file that will implement the morning plan, leave home plan, and movie plan by controlling the lamp.
# 
# Here's how the `function.py` file will look:

# functions/function.py

from home.home_plan import home_plan
from home.actuator import Light
from home.logger_config import logger

def control_lights(action):
    home = home_plan()
    
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, Light):
                if action == "turn_on":
                    actuator.turn_on()
                elif action == "turn_off":
                    actuator.turn_off()

def morning_plan():
    print("Executing Morning Plan...")
    control_lights("turn_on")

def leave_home_plan():
    print("Executing Leave Home Plan...")
    control_lights("turn_off")

def movie_plan():
    print("Executing Movie Plan...")
    control_lights("turn_on")

def main():
    # Here you can call different plans based on your requirements
    # For example, you could set a schedule, trigger the plans based on events, etc.
    
    morning_plan()  # Uncomment to run the morning plan
    # leave_home_plan()  # Uncomment to run leave home plan
    # movie_plan()  # Uncomment to run movie plan

if __name__ == "__main__":
    main()