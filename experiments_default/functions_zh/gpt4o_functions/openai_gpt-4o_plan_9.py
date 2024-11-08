# Based on your functional description and the provided source code, I can create a `function.py` file that implements the main function to handle your specified smart home plans.
# 
# Here is the `function.py` file content:

from home.home_plan import home_plan, get_all_actuators
from home.config import TEMP_CHANGE_DURATION_WINDOW

def main():
    home = home_plan()

    # MORNING PLAN: Coffee machine at 7:40 AM
    coffee_machines = get_all_actuators(home, "CoffeeMachine")
    for coffee_machine in coffee_machines:
        coffee_machine.turn_on()
        coffee_machine.make_coffee("咖啡")

    # LEAVE HOME PLAN: Close the entry door at 8:00 AM
    doors = get_all_actuators(home, "Door")
    for door in doors:
        door.turn_off()

    # MOVIE PLAN: Start playing TV at 7:00 PM
    smart_tvs = get_all_actuators(home, "SmartTV")
    for smart_tv in smart_tvs:
        smart_tv.turn_on()
        smart_tv.play_channel("电视")

if __name__ == "__main__":
    main()