# Based on your functional description and the provided source code, here's a `function.py` file that implements the required functionalities for the MORNING PLAN, LEAVE HOME PLAN, and MOVIE PLAN:

from home.home_plan import home_plan, get_room, get_all_actuators
from home.actuator import CoffeeMachine, Light, Curtain

def morning_plan(home):
    # Find the kitchen to make coffee
    kitchen = get_room(home, "Kitchen")
    if kitchen:
        # Get all coffee machines in the kitchen
        coffee_machines = [actuator for actuator in kitchen.actuators if actuator.actuator_type == "CoffeeMachine"]
        if coffee_machines:
            # Assume we want to make a regular coffee (you can modify this to choose different types of coffee)
            coffee_machines[0].turn_on()  # Turn on the coffee machine
            coffee_machines[0].make_coffee("regular")  # Make coffee
            # Optionally, turn off the coffee machine after use
            # coffee_machines[0].turn_off()
        else:
            print("No coffee machine found in the kitchen.")
    else:
        print("Kitchen not found in the home plan.")

def leave_home_plan(home):
    # Iterate through all rooms to turn off the lights
    for room in home:
        lights = [actuator for actuator in room.actuators if actuator.actuator_type == "Light"]
        for light in lights:
            light.turn_off()

def movie_plan(home):
    # Find the living room to control the curtains
    living_room = get_room(home, "LivingRoom")
    if living_room:
        # Get all curtains in the living room
        curtains = [actuator for actuator in living_room.actuators if actuator.actuator_type == "Curtain"]
        if curtains:
            # Close the curtains
            for curtain in curtains:
                curtain.turn_on()  # Assuming turn_on() means close for curtains
        else:
            print("No curtains found in the living room.")
    else:
        print("Living room not found in the home plan.")

if __name__ == "__main__":
    # Load the home plan
    home = home_plan()
    
    # Execute the morning plan
    print("Executing Morning Plan...")
    morning_plan(home)
    
    # Execute the leave home plan
    print("Executing Leave Home Plan...")
    leave_home_plan(home)
    
    # Execute the movie plan
    print("Executing Movie Plan...")
    movie_plan(home)