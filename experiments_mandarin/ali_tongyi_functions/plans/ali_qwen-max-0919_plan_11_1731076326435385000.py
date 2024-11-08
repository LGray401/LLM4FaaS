# Based on the functional description and the provided source code, I will create a `function.py` file that contains the main function to execute the morning, leave home, and movie plans. This script will be located in the `functions` folder.
# 
# ### `function.py`

# functions/function.py

from home.home_plan import home_plan, get_room_actuators
from home.actuator import Light, Curtain, SmartTV
import time

def execute_morning_plan(home):
    """
    Execute the morning plan: Turn on the lights.
    """
    print("Executing Morning Plan...")
    
    # Get all lights in the living room
    actuators = get_room_actuators(home, "LivingRoom")
    for actuator in actuators:
        if isinstance(actuator, Light):
            actuator.turn_on()
            time.sleep(1)  # Simulate a delay for the light to turn on

def execute_leave_home_plan(home):
    """
    Execute the leave home plan: Open the curtains.
    """
    print("Executing Leave Home Plan...")
    
    # Get all curtains in the living room
    actuators = get_room_actuators(home, "LivingRoom")
    for actuator in actuators:
        if isinstance(actuator, Curtain):
            actuator.turn_on()
            time.sleep(1)  # Simulate a delay for the curtain to open

def execute_movie_plan(home):
    """
    Execute the movie plan: Turn on the TV.
    """
    print("Executing Movie Plan...")
    
    # Get the smart TV in the living room
    actuators = get_room_actuators(home, "LivingRoom")
    for actuator in actuators:
        if isinstance(actuator, SmartTV):
            actuator.turn_on()
            actuator.play_channel("Movie Channel")
            time.sleep(1)  # Simulate a delay for the TV to turn on and start playing

def main():
    # Initialize the home plan
    home = home_plan()
    
    # Execute the plans
    execute_morning_plan(home)
    time.sleep(5)  # Simulate some time passing
    execute_leave_home_plan(home)
    time.sleep(5)  # Simulate some time passing
    execute_movie_plan(home)

if __name__ == "__main__":
    main()