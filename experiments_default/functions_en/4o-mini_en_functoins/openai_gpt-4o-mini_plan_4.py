# Based on the functional description and the provided source code files, I will create a `function.py` file that implements the specified morning, leave home, and movie plans. This file will organize the functionality around the defined plans using the various sensors and actuators from your smart home project.
# 
# Here's the implementation for `function.py`:

# function.py
from home.home_plan import home_plan
from home.actuator import Curtain, Light
from home.logger_config import logger

def morning_plan(home):
    logger.info("Executing morning plan...")
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, Curtain):
                actuator.turn_on()  # Open curtains
                logger.info(f"{actuator.id} has been opened for the morning plan.")
                print(f"{actuator.id} has been opened for the morning plan.")

def leave_home_plan(home):
    logger.info("Executing leave home plan...")
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, Light):
                actuator.turn_off()  # Turn off lamps
                logger.info(f"{actuator.id} has been turned off for the leave home plan.")
                print(f"{actuator.id} has been turned off for the leave home plan.")

def movie_plan(home):
    logger.info("Executing movie plan...")
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, Light):
                actuator.set_brightness_level("low")  # Adjust light brightness for movie
                logger.info(f"Brightness set to low for {actuator.id} for the movie plan.")
                print(f"Brightness set to low for {actuator.id} for the movie plan.")

def main():
    home = home_plan()  # Create home plan with rooms and components
    morning_plan(home)  # Execute morning plan
    leave_home_plan(home)  # Execute leave home plan
    movie_plan(home)  # Execute movie plan

if __name__ == "__main__":
    main()