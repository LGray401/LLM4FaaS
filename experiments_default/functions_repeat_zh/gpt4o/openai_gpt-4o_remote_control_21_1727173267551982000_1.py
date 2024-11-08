# Based on the functional description and the provided source code, I have created the `function.py` file for your smart home project. This file will include the main function that will follow the steps described in your functional description.
# 
# Here's the `function.py`:

import time
from home.home_plan import home_plan, get_room_actuators


def main():
    # Initialize the home with rooms, sensors, and actuators
    home = home_plan()

    # Get the required actuators from the living room
    living_room_actuators = get_room_actuators(home, "LivingRoom")
    
    # Dictionary to hold the actuators for easy access
    actuators_dict = {actuator.actuator_type: actuator for actuator in living_room_actuators}

    # Turn on the light and set it to medium brightness
    light = actuators_dict.get("Light")
    if light:
        light.turn_on()
        light.set_brightness_level("medium")

    # Turn on the music player and play a stress-relief song
    music_player = actuators_dict.get("MusicPlayer")
    if music_player:
        music_player.turn_on()
        music_player.play_music("stress_relief_playlist")

    # Turn on the coffee machine and make a cup of coffee
    coffee_machine = actuators_dict.get("CoffeeMachine")
    if coffee_machine:
        coffee_machine.turn_on()
        coffee_machine.make_coffee("regular coffee")

    # Turn on the AC and set the temperature to 22°C
    ac = actuators_dict.get("AC")
    if ac:
        ac.turn_on()
        ac.set_target_temperature(22)

    # Turn off the curtain
    curtain = actuators_dict.get("Curtain")
    if curtain:
        curtain.turn_off()

    # Turn on the cleaning robot and start the daily routine
    cleaning_robot = actuators_dict.get("CleaningRobot")
    if cleaning_robot:
        cleaning_robot.turn_on()
        cleaning_robot.daily_routine()

    # Log the completion of tasks
    print("All tasks have been completed successfully.")

if __name__ == "__main__":
    main()