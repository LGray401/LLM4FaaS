# Based on your functional description and the provided source code, I will create a `function.py` file that contains the main function to execute the morning, leave home, and movie plans. The `function.py` will be placed in the `functions` folder.
# 
# Here is the `function.py` file:

# functions/function.py

from home.home_plan import home_plan, get_room_actuators
from home.actuator import Curtain, Light
import time

def execute_morning_plan(home):
    """
    Executes the morning plan which includes opening the curtains.
    """
    print("Executing Morning Plan...")
    for room in home:
        # Get all curtains in the room
        curtains = [actuator for actuator in room.actuators if isinstance(actuator, Curtain)]
        for curtain in curtains:
            curtain.turn_on()
            print(f"Opening {curtain.id} in {room.name}")
            time.sleep(1)  # Simulate the time it takes to open the curtain
            curtain.turn_off()  # Turn off after opening
    print("Morning Plan Executed.")

def execute_leave_home_plan(home):
    """
    Executes the leave home plan which includes turning off all lights.
    """
    print("Executing Leave Home Plan...")
    for room in home:
        # Get all lights in the room
        lights = [actuator for actuator in room.actuators if isinstance(actuator, Light)]
        for light in lights:
            if light.status == "on":
                light.turn_off()
                print(f"Turning off {light.id} in {room.name}")
                time.sleep(1)  # Simulate the time it takes to turn off the light
    print("Leave Home Plan Executed.")

def execute_movie_plan(home):
    """
    Executes the movie plan which includes setting the light brightness to low.
    """
    print("Executing Movie Plan...")
    for room in home:
        # Get all lights in the room
        lights = [actuator for actuator in room.actuators if isinstance(actuator, Light)]
        for light in lights:
            if light.status == "on":
                light.set_brightness_level("low")
                print(f"Setting {light.id} in {room.name} to LOW brightness")
                time.sleep(1)  # Simulate the time it takes to set the brightness
    print("Movie Plan Executed.")

def main():
    # Create the home plan
    home = home_plan()

    # Execute the morning plan
    execute_morning_plan(home)

    # Wait for a while (simulating some time passing)
    time.sleep(5)

    # Execute the leave home plan
    execute_leave_home_plan(home)

    # Wait for a while (simulating some time passing)
    time.sleep(5)

    # Execute the movie plan
    execute_movie_plan(home)

if __name__ == "__main__":
    main()