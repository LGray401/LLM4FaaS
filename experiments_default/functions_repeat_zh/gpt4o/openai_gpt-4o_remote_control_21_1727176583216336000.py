# Sure, I'll create the `function.py` file based on your requirement. This file will be placed in the `functions` folder and will contain the main function to execute the described tasks.
# 
# Here's the `function.py`:

import sys
import os

# Set up the import path for the home folder
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'home'))

from home_plan import home_plan, get_room

def main():
    # Initialize home plan
    home = home_plan()
    
    # Get the living room
    living_room = get_room(home, "LivingRoom")
    if not living_room:
        print("LivingRoom not found!")
        return

    # Get actuators
    light = next((act for act in living_room.actuators if act.actuator_type == "Light"), None)
    music_player = next((act for act in living_room.actuators if act.actuator_type == "MusicPlayer"), None)
    coffee_machine = next((act for act in living_room.actuators if act.actuator_type == "CoffeeMachine"), None)
    ac = next((act for act in living_room.actuators if act.actuator_type == "AC"), None)
    curtain = next((act for act in living_room.actuators if act.actuator_type == "Curtain"), None)
    cleaning_robot = next((act for act in living_room.actuators if act.actuator_type == "CleaningRobot"), None)

    # Perform actions
    if light:
        light.turn_on()
        light.set_brightness_level("medium")

    if music_player:
        music_player.turn_on()
        music_player.play_music("Relaxing Music Playlist")

    if coffee_machine:
        coffee_machine.turn_on()
        coffee_machine.make_coffee("Espresso")

    if ac:
        ac.turn_on()
        ac.set_target_temperature(22)

    if curtain:
        curtain.turn_off()  # Assuming turn_off means closing the curtain

    if cleaning_robot:
        cleaning_robot.turn_on()
        cleaning_robot.daily_routine()

if __name__ == "__main__":
    main()