# Based on your functional description and the provided source code, I will create a `function.py` file that contains the main functions to execute the MORNING PLAN, LEAVE HOME PLAN, and MOVIE PLAN. These functions will interact with the sensors and actuators defined in your `sensor.py` and `actuator.py` files, respectively. The `home_plan.py` file will be used to retrieve the rooms and their components.
# 
# Here's the `function.py` file:

from home.home_plan import home_plan, get_room, get_room_actuators
from home.actuator import CoffeeMachine, Light, Curtain

def morning_plan(home):
    # Execute the morning plan: turn on the coffee machine in the kitchen
    kitchen = get_room(home, "Kitchen")
    if kitchen:
        for actuator in kitchen.actuators:
            if isinstance(actuator, CoffeeMachine):
                actuator.turn_on()
                actuator.make_coffee("Espresso")  # Assuming a default coffee type
                break

def leave_home_plan(home):
    # Execute the leave home plan: turn off all lights in all rooms
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, Light):
                actuator.turn_off()

def movie_plan(home):
    # Execute the movie plan: close the curtains in the living room
    living_room = get_room(home, "LivingRoom")
    if living_room:
        for actuator in living_room.actuators:
            if isinstance(actuator, Curtain):
                actuator.turn_on()  # Assuming turn_on() closes the curtains for the movie
                break

if __name__ == "__main__":
    # Initialize the home plan
    home = home_plan()
    
    # Test the plans
    print("Executing Morning Plan...")
    morning_plan(home)
    
    print("\nExecuting Leave Home Plan...")
    leave_home_plan(home)
    
    print("\nExecuting Movie Plan...")
    movie_plan(home)