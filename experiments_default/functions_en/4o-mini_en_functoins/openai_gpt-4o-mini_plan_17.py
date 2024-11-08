# Based on your functional description and the existing source code, I've created a `function.py` file that implements the main functionality for your smart home project. It will execute the specified routines for the morning, leaving home, and movie plans.
# 
# Here's the content for `function.py`:

# function.py
from home.home_plan import home_plan, get_room_actuators
from home.actuator import CoffeeMachine, Light, Curtain

def execute_morning_plan(home):
    print("Executing Morning Plan...")
    kitchen = get_room_actuators(home, "Kitchen")
    if kitchen:
        coffee_machine = next((act for act in kitchen if isinstance(act, CoffeeMachine)), None)
        if coffee_machine:
            coffee_machine.turn_on()
            coffee_machine.make_coffee("Espresso")
        else:
            print("No CoffeeMachine found in Kitchen.")
    else:
        print("No kitchen found in home.")

def execute_leave_home_plan(home):
    print("Executing Leave Home Plan...")
    living_room = get_room_actuators(home, "LivingRoom")
    if living_room:
        lamp = next((act for act in living_room if isinstance(act, Light)), None)
        if lamp:
            lamp.turn_off()
        else:
            print("No Light found in Living Room.")
    else:
        print("No living room found in home.")

def execute_movie_plan(home):
    print("Executing Movie Plan...")
    bedroom = get_room_actuators(home, "Bedroom")
    if bedroom:
        curtains = next((act for act in bedroom if isinstance(act, Curtain)), None)
        if curtains:
            curtains.turn_on()
        else:
            print("No Curtains found in Bedroom.")
    else:
        print("No bedroom found in home.")

def main():
    home = home_plan()
    
    # Execute plans
    execute_morning_plan(home)
    execute_leave_home_plan(home)
    execute_movie_plan(home)

if __name__ == "__main__":
    main()