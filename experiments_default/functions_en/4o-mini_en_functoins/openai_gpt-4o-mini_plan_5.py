# Based on your functional description and the provided source code, I will create the `function.py` file that implements the specified plans for your smart home project. This file will contain a `main` function that coordinates the execution of the morning, leave home, and movie plans.
# 
# Here's the `function.py` file that you can place in the `functions` folder:

# functions/function.py
from home.home_plan import home_plan
from home.actuator import CoffeeMachine, Light, Curtain
from home.logger_config import logger

def execute_morning_plan(home):
    logger.info("Executing morning plan...")
    coffee_machine = None
    
    # Find the CoffeeMachine actuator in the home
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, CoffeeMachine):
                coffee_machine = actuator
                break
        if coffee_machine:
            break

    if coffee_machine:
        coffee_machine.turn_on()
        coffee_machine.make_coffee("espresso")  # Example coffee type
    else:
        logger.warning("No Coffee Machine found in home.")

def execute_leave_home_plan(home):
    logger.info("Executing leave home plan...")
    light = None

    # Find the Light actuator in the home
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, Light):
                light = actuator
                break
        if light:
            break

    if light:
        light.turn_off()
    else:
        logger.warning("No Light found in home.")

def execute_movie_plan(home):
    logger.info("Executing movie plan...")
    curtain = None

    # Find the Curtain actuator in the home
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, Curtain):
                curtain = actuator
                break
        if curtain:
            break

    if curtain:
        curtain.turn_on()  # Assuming turning on the curtain means closing it
    else:
        logger.warning("No Curtain found in home.")

def main():
    home = home_plan()  # Get the home plan

    # Execute the plans in sequence
    execute_morning_plan(home)
    execute_leave_home_plan(home)
    execute_movie_plan(home)

if __name__ == "__main__":
    main()