# Let's create the `function.py` file based on the provided information. Given the functional description, the main function should implement the following plans:
# 
# 1. **Morning Plan:** Control the curtain.
# 2. **Leave Home Plan:** Control the lights.
# 3. **Movie Plan:** Adjust the light brightness.
# 
# Here is the `function.py` file:

from home.home_plan import home_plan, get_all_actuators
from home.actuator import Curtain, Light

def morning_plan(home):
    # Control curtains in the morning
    curtains = get_all_actuators(home, "Curtain")
    for curtain in curtains:
        curtain.turn_on()
    print("Morning plan executed: Curtains are now open.")

def leave_home_plan(home):
    # Control lights when leaving home
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_off()
    print("Leave home plan executed: Lights are now off.")

def movie_plan(home):
    # Adjust light brightness for movie plan
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_on()
        light.set_brightness_level("low")
    print("Movie plan executed: Lights are now dimmed for the movie.")

def main():
    # Create a home plan
    home = home_plan()

    # Execute the different plans
    morning_plan(home)
    leave_home_plan(home)
    movie_plan(home)

if __name__ == "__main__":
    main()