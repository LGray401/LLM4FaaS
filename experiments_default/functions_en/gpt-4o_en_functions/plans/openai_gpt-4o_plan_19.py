# Alright, based on your functional description and the existing code base, I will create a `function.py` file that contains the main functions to execute the "MORNING PLAN" and "LEAVE HOME PLAN". I will also leave a placeholder for the "MOVIE PLAN".
# 
# Here is the `function.py` file:

# functions/function.py

from home.home_plan import home_plan, get_room_actuators
from home.logger_config import logger

def morning_plan(home):
    logger.info("Executing Morning Plan")
    
    # Step 1: Open the curtains
    living_room = get_room_actuators(home, "LivingRoom")
    for actuator in living_room:
        if actuator.actuator_type == "Curtain":
            actuator.turn_on()
            print(f"Opening the curtains in {actuator.room_name}")
            logger.info(f"Opening the curtains in {actuator.room_name}")
    
    # Step 2: Make a cup of coffee
    kitchen = get_room_actuators(home, "Kitchen")
    for actuator in kitchen:
        if actuator.actuator_type == "CoffeeMachine":
            actuator.turn_on()
            actuator.make_coffee("Espresso")
            print(f"Making a cup of coffee in {actuator.room_name}")
            logger.info(f"Making a cup of coffee in {actuator.room_name}")

def leave_home_plan(home):
    logger.info("Executing Leave Home Plan")
    
    # Step 1: Lock the doors
    for room in home:
        for actuator in room.actuators:
            if actuator.actuator_type == "Door":
                actuator.lock()
                print(f"Locking the door in {actuator.room_name}")
                logger.info(f"Locking the door in {actuator.room_name}")

    # Step 2: Shut off the power
    for room in home:
        for actuator in room.actuators:
            if actuator.actuator_type == "SmartSocket":
                actuator.turn_off()
                print(f"Turning off SmartSocket in {actuator.room_name}")
                logger.info(f"Turning off SmartSocket in {actuator.room_name}")

def movie_plan(home):
    logger.info("Executing Movie Plan")
    # Placeholder for movie plan implementation
    pass

def main():
    home = home_plan()
    
    # Example calls to the plans
    morning_plan(home)
    leave_home_plan(home)
    movie_plan(home)

if __name__ == "__main__":
    main()