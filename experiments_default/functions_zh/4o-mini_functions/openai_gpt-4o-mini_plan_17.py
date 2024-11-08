# Based on your functional description and the provided source code, I will create a `function.py` file that implements the morning, leave home, and movie plans. This file will use the classes defined in your other files to control the smart home devices according to the specified plans.
# 
# Here is the `function.py` file:

# functions/function.py
from home.home_plan import home_plan, print_home_plan, get_room, get_room_actuators
from home.actuator import CoffeeMachine, Light, Curtain

def morning_plan(home):
    print("Executing Morning Plan...")
    kitchen = get_room(home, "Kitchen")
    coffee_machine = get_room_actuators(home, "CoffeeMachine")

    if coffee_machine:
        coffee_machine[0].turn_on()  # Assuming there's only one coffee machine
        coffee_machine[0].make_coffee("Espresso")  # Change coffee type as needed

def leave_home_plan(home):
    print("Executing Leave Home Plan...")
    living_room = get_room(home, "LivingRoom")
    lights = get_room_actuators(home, "Light")

    if lights:
        for light in lights:
            light.turn_off()  # Turn off all lights in the living room

def movie_plan(home):
    print("Executing Movie Plan...")
    bedroom = get_room(home, "Bedroom")
    curtains = get_room_actuators(home, "Curtain")

    if curtains:
        curtains[0].turn_on()  # Assuming there's only one curtain
        print("Curtains closed for the movie.")

def main():
    home = home_plan()
    print_home_plan(home)

    # Execute the plans
    morning_plan(home)
    leave_home_plan(home)
    movie_plan(home)

if __name__ == "__main__":
    main()