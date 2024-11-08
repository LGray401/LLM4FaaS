# Based on the functional description and the provided source code, here's the `function.py` file that you can use for your smart home project. This file will contain the main functions to execute the MORNING PLAN, LEAVE HOME PLAN, and MOVIE PLAN.

# function.py
from home.home_plan import home_plan, get_room, get_room_actuators
from home.actuator import CoffeeMachine, Light, Curtain

def morning_plan(home):
    # Execute the morning plan: turn on the coffee machine
    kitchen = get_room(home, "Kitchen")
    if kitchen:
        for actuator in kitchen.actuators:
            if isinstance(actuator, CoffeeMachine):
                actuator.turn_on()
                actuator.make_coffee("Espresso")  # or any other type of coffee
                break

def leave_home_plan(home):
    # Execute the leave home plan: turn off all lights
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, Light):
                actuator.turn_off()

def movie_plan(home):
    # Execute the movie plan: close the curtains
    living_room = get_room(home, "LivingRoom")
    if living_room:
        for actuator in living_room.actuators:
            if isinstance(actuator, Curtain):
                actuator.turn_on()  # Assuming turn_on() closes the curtains for movie mode
                # You might need to implement additional logic if turn_on() does not represent closing
                break

def main():
    # Initialize the home plan
    home = home_plan()
    
    # Execute the morning plan
    morning_plan(home)
    
    # Execute the leave home plan
    leave_home_plan(home)
    
    # Execute the movie plan
    movie_plan(home)

if __name__ == "__main__":
    main()