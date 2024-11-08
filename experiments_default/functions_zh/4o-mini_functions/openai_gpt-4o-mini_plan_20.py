# Based on the provided functional description and existing code files, I'll create a `function.py` file that implements the specified plans for the smart home automation project. This file will include a main function that executes the "MORNING PLAN", "LEAVE HOME PLAN", and "MOVIE PLAN". Each plan will control the relevant actuators according to the descriptions you provided.
# 
# Here's the content for `function.py`:

# functions/function.py

from home.home_plan import home_plan
from home.actuator import Curtain, Light

def execute_morning_plan(home):
    print("Executing MORNING PLAN: Opening curtains.")
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, Curtain):
                actuator.turn_on()  # Open curtains

def execute_leave_home_plan(home):
    print("Executing LEAVE HOME PLAN: Turning off lights.")
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, Light):
                actuator.turn_off()  # Turn off lights

def execute_movie_plan(home):
    print("Executing MOVIE PLAN: Adjusting light brightness.")
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, Light):
                actuator.turn_on()  # Ensure the light is on before setting brightness
                actuator.set_brightness_level("low")  # Set brightness to low for movie

def main():
    # Create home layout
    home = home_plan()

    # Execute plans
    execute_morning_plan(home)
    execute_leave_home_plan(home)
    execute_movie_plan(home)

if __name__ == "__main__":
    main()