# Based on the provided functional description and source codes, I will create a `function.py` file that includes the main function to handle the specified plans: "Morning Plan", "Leave Home Plan", and "Movie Plan". The main function will interact with the `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py` files to perform the required actions.
# 
# Here is the `function.py` file:

import sys
from home.home_plan import home_plan, get_all_actuators

def morning_plan(home):
    print("Executing Morning Plan...")
    coffee_machines = get_all_actuators(home, "CoffeeMachine")
    for coffee_machine in coffee_machines:
        coffee_machine.turn_on()
        coffee_machine.make_coffee("Espresso")
    print("Morning Plan executed.\n")

def leave_home_plan(home):
    print("Executing Leave Home Plan...")
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_off()
    print("Leave Home Plan executed.\n")

def movie_plan(home):
    print("Executing Movie Plan...")
    curtains = get_all_actuators(home, "Curtain")
    for curtain in curtains:
        curtain.turn_on()
    print("Movie Plan executed.\n")

def main(plan_name):
    home = home_plan()
    if plan_name == "MORNING PLAN":
        morning_plan(home)
    elif plan_name == "LEAVE HOME PLAN":
        leave_home_plan(home)
    elif plan_name == "MOVIE PLAN":
        movie_plan(home)
    else:
        print(f"Unknown plan: {plan_name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python function.py <PLAN_NAME>")
    else:
        main(sys.argv[1])