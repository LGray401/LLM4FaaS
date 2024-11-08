# Sure! Based on your requirements and the provided source code, I'll create a `function.py` file that orchestrates the operations described in your functional description. Here's the `function.py` file:

# function.py
import os
import sys

# Add the home folder to the system path to import modules
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..', 'home'))

from home.home_plan import home_plan, get_room_actuators, get_room
from home.logger_config import logger

def main():
    # Initialize the home plan
    home = home_plan()
    
    # Define room
    room_name = "LivingRoom"

    # Get the room actuators
    room = get_room(home, room_name)
    if not room:
        logger.error(f"Room '{room_name}' not found!")
        return
    
    actuators = get_room_actuators(home, room_name)

    # Function to find specific actuator by type
    def find_actuator(actuator_type):
        for actuator in actuators:
            if actuator.actuator_type == actuator_type:
                return actuator
        return None

    # Light: Turn on and set to medium brightness
    light = find_actuator("Light")
    if light:
        light.turn_on()
        light.set_brightness_level("medium")

    # MusicPlayer: Turn on and play relaxing music
    music_player = find_actuator("MusicPlayer")
    if music_player:
        music_player.turn_on()
        music_player.play_music("relaxing_playlist")

    # CoffeeMachine: Turn on and make coffee
    coffee_machine = find_actuator("CoffeeMachine")
    if coffee_machine:
        coffee_machine.turn_on()
        coffee_machine.make_coffee("espresso")

    # AC: Turn on and set to 22°C
    ac = find_actuator("AC")
    if ac:
        ac.turn_on()
        ac.set_target_temperature(22)

    # Curtain: Close the curtain
    curtain = find_actuator("Curtain")
    if curtain:
        curtain.turn_off()

    # CleaningRobot: Turn on and start daily routine
    cleaning_robot = find_actuator("CleaningRobot")
    if cleaning_robot:
        cleaning_robot.turn_on()
        cleaning_robot.daily_routine()

if __name__ == "__main__":
    main()