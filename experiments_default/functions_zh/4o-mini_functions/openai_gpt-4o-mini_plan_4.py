# Based on your functional description and the provided source code, I will create the `function.py` file for your smart home project. This file will include a main function that implements the specified plans (Morning Plan, Leave Home Plan, and Movie Plan) using the existing classes from your project.
# 
# Here's how `function.py` could look:

# functions/function.py
from home.home_plan import home_plan, get_all_actuators, get_room
from home.actuator import Curtain, Light

def execute_morning_plan(home):
    # Morning Plan: Open curtains
    living_room = get_room(home, "LivingRoom")
    if living_room:
        curtains = get_all_actuators(living_room, "Curtain")
        for curtain in curtains:
            curtain.turn_on()  # Assuming turnzing on opens the curtain
            print(f"Opened {curtain.id}")

def execute_leave_home_plan(home):
    # Leave Home Plan: Turn off lights
    living_room = get_room(home, "LivingRoom")
    if living_room:
        lights = get_all_actuators(living_room, "Light")
        for light in lights:
            light.turn_off()  # Turn off all lights
            print(f"Turned off {light.id}")

def execute_movie_plan(home):
    # Movie Plan: Adjust light brightness
    living_room = get_room(home, "LivingRoom")
    if living_room:
        lights = get_all_actuators(living_room, "Light")
        for light in lights:
            light.turn_on()  # Make sure light is on before setting brightness
            light.set_brightness_level("low")  # Adjust brightness to low for movie
            print(f"Set {light.id} brightness to low")

def main():
    home = home_plan()  # Create the home plan

    # Execute plans
    print("Executing Morning Plan...")
    execute_morning_plan(home)

    print("\nExecuting Leave Home Plan...")
    execute_leave_home_plan(home)

    print("\nExecuting Movie Plan...")
    execute_movie_plan(home)

if __name__ == "__main__":
    main()