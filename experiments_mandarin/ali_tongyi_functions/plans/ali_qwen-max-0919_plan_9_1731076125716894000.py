# Given your functional description and the provided source code, I will create a `function.py` file that contains the main function to execute the morning plan, leave home plan, and movie plan. This script will be placed in the `functions` folder.
# 
# Here's the `function.py` file:

# functions/function.py

import time
from datetime import datetime, timedelta
from home.home_plan import home_plan, get_room_actuators
from home.actuator import CoffeeMachine, Door, SmartTV
from home.config import DAILY_ROUTINE_DURATION

def main():
    # Initialize the home plan
    home = home_plan()

    while True:
        current_time = datetime.now().time()
        print(f"Current Time: {current_time}")

        # MORNING PLAN
        if current_time.hour == 7 and current_time.minute >= 40:
            kitchen_actuators = get_room_actuators(home, "Kitchen")
            for actuator in kitchen_actuators:
                if isinstance(actuator, CoffeeMachine):
                    actuator.turn_on()
                    actuator.make_coffee("Coffee")
                    actuator.turn_off()
                    print("Morning coffee is ready! :coffee:")
                    break

        # LEAVE HOME PLAN
        if current_time.hour == 8 and current_time.minute == 0:
            livingroom_actuators = get_room_actuators(home, "LivingRoom")
            for actuator in livingroom_actuators:
                if isinstance(actuator, Door):
                    actuator.lock()
                    print("Ingress door locked.")
                    break

        # MOVIE PLAN
        if current_time.hour == 19 and current_time.minute == 0:
            livingroom_actuators = get_room_actuators(home, "LivingRoom")
            for actuator in livingroom_actuators:
                if isinstance(actuator, SmartTV):
                    actuator.turn_on()
                    actuator.play_channel("Movie Channel")
                    print("Starting to play a movie on TV.")
                    break

        # Sleep for a minute before checking the time again
        time.sleep(60)

if __name__ == "__main__":
    main()