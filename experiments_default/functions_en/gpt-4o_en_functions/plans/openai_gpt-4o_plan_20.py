# Based on your functional description and the provided source code, I'll create a `function.py` file that meets your requirements. This file will be placed in the `functions` folder and will contain the main functions to execute the smart home plans: MORNING PLAN, LEAVE HOME PLAN, and MOVIE PLAN.
# 
# Here's the `function.py` file:

# functions/function.py

from home.home_plan import home_plan, get_all_actuators

def main():
    # Initialize the home with its rooms, sensors, and actuators
    home = home_plan()

    # MORNING PLAN: Open the curtains
    def morning_plan():
        curtains = get_all_actuators(home, "Curtain")
        for curtain in curtains:
            curtain.turn_on()
        print("MORNING PLAN: Curtains are now open.")

    # LEAVE HOME PLAN: Turn off the lights
    def leave_home_plan():
        lights = get_all_actuators(home, "Light")
        for light in lights:
            light.turn_off()
        print("LEAVE HOME PLAN: Lights are now off.")

    # MOVIE PLAN: Adjust light brightness
    def movie_plan():
        lights = get_all_actuators(home, "Light")
        for light in lights:
            light.turn_on()
            light.set_brightness_level("low")
        print("MOVIE PLAN: Light brightness adjusted to low.")

    # Execute the plans based on the functional description
    morning_plan()
    leave_home_plan()
    movie_plan()

if __name__ == "__main__":
    main()