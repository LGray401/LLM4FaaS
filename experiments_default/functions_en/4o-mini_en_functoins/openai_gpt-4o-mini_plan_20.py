# Based on the provided functional description and source code, here is the implementation of the `function.py` file. This file will include a `main` function that executes the specified plans for the smart home.
# 
# ### `functions/function.py`

from home.home_plan import home_plan
from home.actuator import Curtain, Light

def morning_plan(home):
    # Open the curtains
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, Curtain):
                actuator.turn_on()
                print(f"Curtain in {room.name} opened.")

def leave_home_plan(home):
    # Turn off the lights
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, Light):
                actuator.turn_off()
                print(f"Light in {room.name} turned off.")

def movie_plan(home):
    # Adjust light brightness
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, Light):
                actuator.set_brightness_level("medium")
                print(f"Light in {room.name} brightness adjusted to medium.")

def main():
    home = home_plan()
    
    # Execute the plans
    print("Executing Morning Plan...")
    morning_plan(home)

    print("\nExecuting Leave Home Plan...")
    leave_home_plan(home)

    print("\nExecuting Movie Plan...")
    movie_plan(home)

if __name__ == "__main__":
    main()