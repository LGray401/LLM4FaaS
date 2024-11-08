# Based on the provided functional description and source code, I will create a `function.py` file that contains the main function to execute the morning, leave home, and movie plans. The `function.py` will be located in the `functions` folder, as specified. 
# 
# Here is the `function.py` file:

# functions/function.py

from home.home_plan import home_plan, get_room_actuators
from home.actuator import Curtain, Light, Window, SmartTV
from home.logger_config import logger

def execute_morning_plan(home):
    """
    Execute the morning plan:
    - Open the curtains
    """
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, Curtain):
                actuator.turn_on()
                logger.info(f"Morning Plan: {actuator.id} is now ON.")

def execute_leave_home_plan(home):
    """
    Execute the leave home plan:
    - Turn off all lights
    - Close all windows
    """
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, Light):
                actuator.turn_off()
                logger.info(f"Leave Home Plan: {actuator.id} is now OFF.")
            elif isinstance(actuator, Window):
                actuator.turn_off()
                logger.info(f"Leave Home Plan: {actuator.id} is now CLOSED.")

def execute_movie_plan(home):
    """
    Execute the movie plan:
    - Turn on the TV
    """
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, SmartTV):
                actuator.turn_on()
                actuator.play_channel("Movie Channel")
                logger.info(f"Movie Plan: {actuator.id} is now ON and playing Movie Channel.")

def main():
    # Create the home plan
    home = home_plan()

    # Execute the morning plan
    execute_morning_plan(home)

    # Execute the leave home plan
    execute_leave_home_plan(home)

    # Execute the movie plan
    execute_movie_plan(home)

if __name__ == "__main__":
    main()