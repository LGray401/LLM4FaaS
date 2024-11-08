# Based on the provided functional description and source code, I will create a `function.py` file that contains the main function to execute the morning plan, leave home plan, and movie plan. This file will be located in the `functions` folder.
# 
# ### Functional Description Recap:
# - **MORNING PLAN:** Turn on the coffee machine.
# - **LEAVE HOME PLAN:** Turn off all lights.
# - **MOVIE PLAN:** Close the curtains.
# 
# ### `function.py` Implementation:

# functions/function.py

from home.home_plan import home_plan, get_all_actuators, get_room_actuators
from home.actuator import CoffeeMachine, Light, Curtain

def execute_morning_plan():
    """
    Executes the morning plan: Turn on the coffee machine.
    """
    home = home_plan()
    coffee_machines = get_all_actuators(home, "CoffeeMachine")
    
    for coffee_machine in coffee_machines:
        if coffee_machine.status == "off":
            coffee_machine.turn_on()
        coffee_machine.make_coffee("espresso")

def execute_leave_home_plan():
    """
    Executes the leave home plan: Turn off all lights.
    """
    home = home_plan()
    lights = get_all_actuators(home, "Light")
    
    for light in lights:
        if light.status == "on":
            light.turn_off()

def execute_movie_plan():
    """
    Executes the movie plan: Close the curtains.
    """
    home = home_plan()
    curtains = get_all_actuators(home, "Curtain")
    
    for curtain in curtains:
        if curtain.status == "off":
            curtain.turn_on()
        # Assuming turning on the curtain actuator closes the curtains
        # If the logic is different, you may need to add a specific method to close the curtains

def main():
    print("Executing Smart Home Plans...")
    
    # Execute Morning Plan
    print("\n--- Executing Morning Plan ---")
    execute_morning_plan()
    
    # Execute Leave Home Plan
    print("\n--- Executing Leave Home Plan ---")
    execute_leave_home_plan()
    
    # Execute Movie Plan
    print("\n--- Executing Movie Plan ---")
    execute_movie_plan()

if __name__ == "__main__":
    main()