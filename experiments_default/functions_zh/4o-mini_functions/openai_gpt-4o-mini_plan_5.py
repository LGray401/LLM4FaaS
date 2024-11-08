# Based on your functional description and the provided source code, I will create a `function.py` file that implements the required morning, leave home, and movie plans. This file will contain a `main()` function that orchestrates the interactions between sensors and actuators according to the specified plans.
# 
# Here's the code for `function.py`:

# function.py
from home.home_plan import home_plan, get_room, get_room_actuators
from home.actuator import CoffeeMachine, Light, Curtain
from home.logger_config import logger


def morning_plan(home):
    """Execute the morning plan by turning on the coffee machine."""
    room = get_room(home, "Kitchen")
    if room:
        coffee_machine = next((actuator for actuator in room.actuators if isinstance(actuator, CoffeeMachine)), None)
        if coffee_machine:
            coffee_machine.turn_on()
            coffee_machine.make_coffee("Espresso")  # You can change the coffee type as needed.
        else:
            print("Coffee machine not found in the kitchen.")
            logger.warning("Coffee machine not found in the kitchen.")
    else:
        print("Kitchen not found in the home.")
        logger.warning("Kitchen not found in the home.")

        
def leave_home_plan(home):
    """Execute the leave home plan by turning off the lights."""
    room = get_room(home, "LivingRoom")
    if room:
        lights = get_room_actuators(home, "Light")
        for light in lights:
            light.turn_off()
    else:
        print("Living room not found in the home.")
        logger.warning("Living room not found in the home.")


def movie_plan(home):
    """Execute the movie plan by closing the curtains."""
    room = get_room(home, "LivingRoom")
    if room:
        curtain = next((actuator for actuator in room.actuators if isinstance(actuator, Curtain)), None)
        if curtain:
            curtain.turn_on()  # Assuming we need to turn on the curtain actuator.
            print(f"{curtain.id} is now closed for movie time.")
            logger.info(f"{curtain.id} is now closed for movie time.")
        else:
            print("Curtain not found in the living room.")
            logger.warning("Curtain not found in the living room.")
    else:
        print("Living room not found in the home.")
        logger.warning("Living room not found in the home.")


def main():
    home = home_plan()  # Create home plan
    print("Executing morning plan...")
    morning_plan(home)

    print("Executing leave home plan...")
    leave_home_plan(home)
    
    print("Executing movie plan...")
    movie_plan(home)


if __name__ == "__main__":
    main()