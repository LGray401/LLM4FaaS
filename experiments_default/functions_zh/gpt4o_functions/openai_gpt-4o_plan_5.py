# Based on the provided functional description and source code files, I will create a `function.py` file in the `functions` folder that contains the main function to implement the smart home plans (Morning Plan, Leave Home Plan, and Movie Plan).
# 
# Here is the `function.py` file:

# file: functions/function.py

from home.home_plan import home_plan, get_room, get_all_actuators

def main():
    home = home_plan()  # Create the home plan

    print("=== Morning Plan ===")
    morning_plan(home)

    print("\n=== Leave Home Plan ===")
    leave_home_plan(home)

    print("\n=== Movie Plan ===")
    movie_plan(home)

def morning_plan(home):
    coffee_machines = get_all_actuators(home, "CoffeeMachine")
    for machine in coffee_machines:
        machine.turn_on()
        machine.make_coffee("Espresso")  # Example coffee type

def leave_home_plan(home):
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_off()

def movie_plan(home):
    curtains = get_all_actuators(home, "Curtain")
    for curtain in curtains:
        curtain.turn_on()

if __name__ == "__main__":
    main()