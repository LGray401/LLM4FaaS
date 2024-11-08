# Based on your functional description and the provided source code, I will create a `function.py` file that contains the main functions to execute the MORNING PLAN, LEAVE HOME PLAN, and MOVIE PLAN. These functions will utilize the classes and methods defined in the `sensor.py`, `actuator.py`, and `home_plan.py` files.
# 
# Here is the `function.py` file:

from home.home_plan import home_plan, get_room, get_all_actuators
from home.actuator import CoffeeMachine, SmartTV, Door
from home.logger_config import logger
import datetime

def execute_morning_plan(home):
    # Get the kitchen room
    kitchen = get_room(home, "Kitchen")
    if not kitchen:
        return

    # Get the coffee machine from the kitchen
    coffee_machines = [actuator for actuator in kitchen.actuators if isinstance(actuator, CoffeeMachine)]
    if not coffee_machines:
        logger.warning("No CoffeeMachine found in the Kitchen.")
        return

    coffee_machine = coffee_machines[0]

    # Turn on the coffee machine and make coffee
    if coffee_machine.status == "off":
        coffee_machine.turn_on()
    coffee_machine.make_coffee("40°C coffee")  # Assuming 40°C is the temperature for the coffee

    logger.info("Morning Plan executed: Coffee made.")

def execute_leave_home_plan(home):
    # Get the living room
    living_room = get_room(home, "LivingRoom")
    if not living_room:
        return

    # Get the door from the living room (assuming it's the main door)
    doors = [actuator for actuator in living_room.actuators if isinstance(actuator, Door)]
    if not doors:
        logger.warning("No Door found in the LivingRoom.")
        return

    door = doors[0]

    # Lock the door (if it's not already locked)
    door.lock()

    logger.info("Leave Home Plan executed: Door locked.")

def execute_movie_plan(home):
    # Get the living room
    living_room = get_room(home, "LivingRoom")
    if not living_room:
        return

    # Get the TV from the living room
    tvs = [actuator for actuator in living_room.actuators if isinstance(actuator, SmartTV)]
    if not tvs:
        logger.warning("No SmartTV found in the LivingRoom.")
        return

    tv = tvs[0]

    # Turn on the TV and play a channel (assuming "Movie Channel" for this example)
    if tv.status == "off":
        tv.turn_on()
    tv.play_channel("Movie Channel")

    logger.info("Movie Plan executed: TV turned on and playing Movie Channel.")

def main():
    # Load the home plan
    home = home_plan()

    # Get current time
    current_time = datetime.datetime.now().time()

    # Execute plans based on time
    if current_time.hour == 7 and current_time.minute == 0:  # 7:00 AM
        execute_morning_plan(home)
    elif current_time.hour == 8 and current_time.minute == 0:  # 8:00 AM
        execute_leave_home_plan(home)
    elif current_time.hour == 19 and current_time.minute == 0:  # 7:00 PM
        execute_movie_plan(home)
    else:
        logger.info("No plan to execute at this time.")

if __name__ == "__main__":
    main()