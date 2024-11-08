# Sure! I'll help you create the `function.py` file based on the functional descriptions provided and the existing code. Here's the `function.py` file:

# functions/function.py
from home.home_plan import home_plan, get_all_actuators

def main():
    # Create the home plan
    home = home_plan()

    # MORNING PLAN: Coffee machine 7.40 degree coffee/:coffee
    coffee_machines = get_all_actuators(home, "CoffeeMachine")
    if coffee_machines:
        for coffee_machine in coffee_machines:
            coffee_machine.turn_on()
            coffee_machine.make_coffee("7.40 degree coffee/:coffee")
            coffee_machine.turn_off()

    # LEAVE HOME PLAN: Close the door at 8 o'clock
    doors = get_all_actuators(home, "Door")
    if doors:
        for door in doors:
            door.turn_on()
            door.lock()
            door.turn_off()

    # MOVIE PLAN: TV starts at 7pm
    smart_tvs = get_all_actuators(home, "SmartTV")
    if smart_tvs:
        for tv in smart_tvs:
            tv.turn_on()
            tv.play_channel("Movie Channel")
            tv.turn_off()

if __name__ == "__main__":
    main()