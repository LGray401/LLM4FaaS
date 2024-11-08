# Based on the provided functional description and the existing code files for your smart home project, here is the implementation of the `function.py` file. This file will contain a main function that executes the specified plans: "MORNING PLAN", "LEAVE HOME PLAN", and "MOVIE PLAN".

# functions/function.py

from home.home_plan import home_plan
from home.actuator import Curtain, Light, SmartTV

def morning_plan(home):
    # Open the curtains in all rooms
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, Curtain):
                actuator.turn_on()

def leave_home_plan(home):
    # Turn off lights and windows in all rooms
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, Light) or isinstance(actuator, Window):
                actuator.turn_off()

def movie_plan(home):
    # Turn on the TV in all rooms
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, SmartTV):
                actuator.turn_on()

def main():
    home = home_plan()
    
    # Execute the plans
    print("Executing MORNING PLAN...")
    morning_plan(home)

    print("\nExecuting LEAVE HOME PLAN...")
    leave_home_plan(home)

    print("\nExecuting MOVIE PLAN...")
    movie_plan(home)

if __name__ == "__main__":
    main()