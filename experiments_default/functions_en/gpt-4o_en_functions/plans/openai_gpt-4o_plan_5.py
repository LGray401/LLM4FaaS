# Based on your functional description and the provided source code, we can create a `function.py` file that will implement the main function to execute the routines you described: "MORNING PLAN" for the coffee machine, "LEAVE HOME PLAN" for the lamp, and "MOVIE PLAN" for the curtain. Here's the `function.py` file:
# 
# ### function.py

import sys
from home.home_plan import home_plan, get_all_actuators

def morning_plan(home):
    coffee_machines = get_all_actuators(home, "CoffeeMachine")
    if coffee_machines:
        for coffee_machine in coffee_machines:
            coffee_machine.turn_on()
            coffee_machine.make_coffee("Espresso")
    else:
        print("No coffee machine found in the home.")

def leave_home_plan(home):
    lamps = get_all_actuators(home, "Light")
    if lamps:
        for lamp in lamps:
            lamp.turn_off()
    else:
        print("No lamps found in the home.")

def movie_plan(home):
    curtains = get_all_actuators(home, "Curtain")
    if curtains:
        for curtain in curtains:
            curtain.turn_on()
    else:
        print("No curtains found in the home.")

def main():
    home = home_plan()
    
    if len(sys.argv) != 2:
        print("Usage: python function.py <plan>")
        print("<plan>: morning, leave_home, movie")
        return

    plan = sys.argv[1]
    if plan == "morning":
        morning_plan(home)
    elif plan == "leave_home":
        leave_home_plan(home)
    elif plan == "movie":
        movie_plan(home)
    else:
        print(f"Unknown plan: {plan}")
        print("Available plans: morning, leave_home, movie")

if __name__ == "__main__":
    main()