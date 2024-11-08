# Based on the content of the markdown file, you are working on a smart home project and you need a new Python file named `function.py` that should be located in the 'functions' folder. This file should contain the main function that implements the following plans:
#
# 1. MORNING PLAN: The coffee machine should make a 7.40 degree coffee.
# 2. LEAVE HOME PLAN: The door should close at 8 o'clock.
# 3. MOVIE PLAN: The TV should start at 7pm.
#
# The `function.py` file should interact with the existing Python files (`sensor.py`, `actuator.py`, `home_plan.py`, and `config.py`) in your project.
#
# Here is a basic structure of the `function.py` file:
#
# ```python
from datetime import datetime
from home.actuator import CoffeeMachine, Door, SmartTV
from home.home_plan import get_room, home_plan

def main():
    # Initialize home plan
    home = home_plan()

    # MORNING PLAN
    # Get the CoffeeMachine in the Kitchen
    kitchen = get_room(home, "Kitchen")
    coffee_machine = next((actuator for actuator in kitchen.actuators if isinstance(actuator, CoffeeMachine)), None)
    if coffee_machine:
        coffee_machine.make_coffee(7.40)

    # LEAVE HOME PLAN
    # Get the Door in the LivingRoom
    living_room = get_room(home, "LivingRoom")
    door = next((actuator for actuator in living_room.actuators if isinstance(actuator, Door)), None)
    if door and datetime.now().hour == 8:
        door.lock()

    # MOVIE PLAN
    # Get the SmartTV in the LivingRoom
    tv = next((actuator for actuator in living_room.actuators if isinstance(actuator, SmartTV)), None)
    if tv and datetime.now().hour == 19:
        tv.play_channel("Movie Channel")

if __name__ == "__main__":
    main()
# ```
#
# This script will execute the morning plan, leave home plan, and movie plan based on the current time. Please note that you need to adjust the `make_coffee` method in the `CoffeeMachine` class to accept a temperature parameter, as currently it only accepts a coffee type. Also, the `play_channel` method in the `SmartTV` class needs to be adjusted to accept a channel name.