# Based on your functional description and the provided source code, here is the `function.py` file that should be placed in the `functions` folder. This file contains the `main` function which will orchestrate the operations described in your functional description.

from home.home_plan import home_plan, get_room
from home.actuator import Light, CoffeeMachine, AC, Curtain, CleaningRobot, MusicPlayer

def main():
    # Initialize the home setup
    home = home_plan()
    
    # Find living room and kitchen
    living_room = get_room(home, "LivingRoom")
    kitchen = get_room(home, "Kitchen")

    # Check if the rooms were found
    if not living_room or not kitchen:
        print("Required rooms are not available in the home plan.")
        return

    # Light: Turn On and set to medium brightness
    for actuator in living_room.actuators:
        if isinstance(actuator, Light):
            actuator.turn_on()
            actuator.set_brightness_level("medium")

    # Music Player: Turn On and play relaxing music
    for actuator in living_room.actuators:
        if isinstance(actuator, MusicPlayer):
            actuator.turn_on()
            actuator.play_music("relaxing music")

    # Coffee Machine: Turn On and make coffee
    for actuator in kitchen.actuators:
        if isinstance(actuator, CoffeeMachine):
            actuator.turn_on()
            actuator.make_coffee("regular coffee")

    # AC: Turn On and set temperature to 22°
    for actuator in living_room.actuators:
        if isinstance(actuator, AC):
            actuator.turn_on()
            actuator.set_target_temperature(22)

    # Curtains: Close
    for actuator in living_room.actuators:
        if isinstance(actuator, Curtain):
            actuator.turn_off()  # Assuming turn_off means closing the curtain

    # Cleaning Robot: Turn On and start daily routine
    for actuator in living_room.actuators:
        if isinstance(actuator, CleaningRobot):
            actuator.turn_on()
            actuator.daily_routine()

if __name__ == "__main__":
    main()