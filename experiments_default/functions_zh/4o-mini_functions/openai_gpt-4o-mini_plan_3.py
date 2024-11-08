# Based on your functional description and the provided source code, I will create a `function.py` file that implements the morning, leave home, and movie plans by utilizing the classes from your existing modules.
# 
# Here's the content for `function.py`:

# functions/function.py

from home.home_plan import home_plan, get_room, get_room_actuators
from home.actuator import CoffeeMachine, Light, Curtain

def morning_plan(home):
    """Prepare a cup of coffee in the morning."""
    kitchen = get_room(home, "Kitchen")
    coffee_machine = None
    for actuator in kitchen.actuators:
        if isinstance(actuator, CoffeeMachine):
            coffee_machine = actuator
            break

    if coffee_machine:
        coffee_machine.turn_on()
        coffee_machine.make_coffee("espresso")  # You can specify the type of coffee
    else:
        print("Coffee machine not found in the kitchen.")

def leave_home_plan(home):
    """Turn off all lights when leaving home."""
    for room in home:
        lights = get_room_actuators(home, room.name)
        for actuator in lights:
            if isinstance(actuator, Light):
                actuator.turn_off()

def movie_plan(home):
    """Prepare for watching a movie by closing the curtains."""
    living_room = get_room(home, "LivingRoom")
    curtain = None
    for actuator in living_room.actuators:
        if isinstance(actuator, Curtain):
            curtain = actuator
            break

    if curtain:
        curtain.turn_on()  # Assuming turning on means closing the curtain
        print("Curtains are now closed.")
    else:
        print("Curtain not found in the living room.")

def main():
    home = home_plan()  # Get the home plan

    # Execute plans
    print("Executing Morning Plan...")
    morning_plan(home)

    print("Executing Leave Home Plan...")
    leave_home_plan(home)

    print("Executing Movie Plan...")
    movie_plan(home)

if __name__ == "__main__":
    main()