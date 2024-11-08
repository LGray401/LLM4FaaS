# Based on your provided functional description and the existing source code, here is the `function.py` file that implements the main function for the smart home project. This file will be placed in the `functions` folder and will utilize the classes and functions from the `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py` files.

# functions/function.py

from home.home_plan import home_plan, get_all_actuators
from home.actuator import Light, Curtain, SmartTV

def main():
    # Create the home plan
    home = home_plan()

    # MORNING PLAN
    print("Executing Morning Plan...")
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_on()

    # LEAVE HOME PLAN
    print("Executing Leave Home Plan...")
    curtains = get_all_actuators(home, "Curtain")
    for curtain in curtains:
        curtain.turn_on()

    # MOVIE PLAN
    print("Executing Movie Plan...")
    tvs = get_all_actuators(home, "SmartTV")
    for tv in tvs:
        tv.turn_on()

if __name__ == "__main__":
    main()