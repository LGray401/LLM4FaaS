# Based on your functional description and the provided source code, I will create the `function.py` file that contains the main function to implement the specified morning plan, leave home plan, and movie plan.
# 
# Here is the `function.py` file:

# function.py

from home.home_plan import home_plan
from home.actuator import CoffeeMachine, Door, SmartTV
from datetime import datetime

def morning_plan(home):
    print("Executing Morning Plan...")
    coffee_machine = None

    # Find CoffeeMachine in the Kitchen
    for room in home:
        if room.name == "Kitchen":
            for actuator in room.actuators:
                if isinstance(actuator, CoffeeMachine):
                    coffee_machine = actuator
                    break
            
    if coffee_machine:
        coffee_machine.turn_on()
        coffee_machine.make_coffee("coffee")
    else:
        print("Coffee machine not found!")

def leave_home_plan(home):
    print("Executing Leave Home Plan...")
    door = None

    # Find Door in the LivingRoom
    for room in home:
        if room.name == "LivingRoom":
            for actuator in room.actuators:
                if isinstance(actuator, Door):
                    door = actuator
                    break
            
    if door:
        door.lock()
    else:
        print("Door not found!")

def movie_plan(home):
    print("Executing Movie Plan...")
    tv = None

    # Find SmartTV in the LivingRoom
    for room in home:
        if room.name == "LivingRoom":
            for actuator in room.actuators:
                if isinstance(actuator, SmartTV):
                    tv = actuator
                    break
            
    if tv:
        tv.turn_on()
        tv.play_channel("Movie Channel")
    else:
        print("TV not found!")

def main():
    home = home_plan()

    # Set current time for testing
    current_time = datetime.now()
    print(f"Current time: {current_time.strftime('%H:%M')}")

    # Execute plans based on current time
    if current_time.hour == 7 and current_time.minute == 40:
        morning_plan(home)
    if current_time.hour == 8 and current_time.minute == 0:
        leave_home_plan(home)
    if current_time.hour == 19 and current_time.minute == 0:
        movie_plan(home)

if __name__ == "__main__":
    main()