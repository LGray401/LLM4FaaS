# Based on your provided functional description and source code, I will create the `function.py` file that contains the main function to execute the morning, leave home, and movie plans. This script will be placed in the `functions` folder.
# 
# Here's the `function.py` file:

# functions/function.py

from home.home_plan import home_plan, get_room_actuators
from home.actuator import CoffeeMachine, Light, Curtain
from home.config import DAILY_ROUTINE_DURATION
import time

def execute_morning_plan(home):
    print("Executing Morning Plan...")
    
    # Get actuators for the kitchen
    kitchen_actuators = get_room_actuators(home, "Kitchen")
    
    # Find the coffee machine in the kitchen
    coffee_machine = next((actuator for actuator in kitchen_actuators if isinstance(actuator, CoffeeMachine)), None)
    
    if coffee_machine:
        coffee_machine.turn_on()
        coffee_machine.make_coffee("espresso")
        time.sleep(DAILY_ROUTINE_DURATION)  # Simulate the time it takes to make coffee
        coffee_machine.turn_off()
    else:
        print("No coffee machine found in the kitchen.")

def execute_leave_home_plan(home):
    print("Executing Leave Home Plan...")
    
    # Turn off all lights in the house
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, Light):
                actuator.turn_off()

def execute_movie_plan(home):
    print("Executing Movie Plan...")
    
    # Get actuators for the living room
    living_room_actuators = get_room_actuators(home, "LivingRoom")
    
    # Find the curtains in the living room
    curtains = [actuator for actuator in living_room_actuators if isinstance(actuator, Curtain)]
    
    if curtains:
        for curtain in curtains:
            curtain.turn_on()  # Assume turning on the curtain means closing it
    else:
        print("No curtains found in the living room.")

def main():
    # Create the home plan
    home = home_plan()
    
    # Execute the morning plan
    execute_morning_plan(home)
    
    # Wait for a while before executing the next plan
    time.sleep(DAILY_ROUTINE_DURATION)
    
    # Execute the leave home plan
    execute_leave_home_plan(home)
    
    # Wait for a while before executing the next plan
    time.sleep(DAILY_ROUTINE_DURATION)
    
    # Execute the movie plan
    execute_movie_plan(home)

if __name__ == "__main__":
    main()