# Based on your functional description and the provided source code, I will create a `function.py` file that will implement the morning plan, leave home plan, and movie plan by controlling the light actuators as specified. Here's how the `function.py` file will look:

# functions/function.py

from home.home_plan import home_plan
from home.actuator import Light
from home.logger_config import logger


def execute_morning_plan(home):
    """Turn on the lights for the morning plan."""
    logger.info("Executing Morning Plan: Turning on lights.")
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, Light):
                actuator.turn_on()
                actuator.set_brightness_level("high")  # Set brightness to high for morning


def execute_leave_home_plan(home):
    """Turn off the lights for the leave home plan."""
    logger.info("Executing Leave Home Plan: Turning off lights.")
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, Light):
                actuator.turn_off()


def execute_movie_plan(home):
    """Dim the lights for the movie plan."""
    logger.info("Executing Movie Plan: Dimming lights.")
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, Light):
                actuator.turn_on()
                actuator.set_brightness_level("low")  # Dim the lights for movie


def main():
    """Main function to execute all plans."""
    home = home_plan()
    
    # Execute the plans
    print("Executing Morning Plan...")
    execute_morning_plan(home)
    
    print("\nExecuting Leave Home Plan...")
    execute_leave_home_plan(home)
    
    print("\nExecuting Movie Plan...")
    execute_movie_plan(home)


if __name__ == "__main__":
    main()