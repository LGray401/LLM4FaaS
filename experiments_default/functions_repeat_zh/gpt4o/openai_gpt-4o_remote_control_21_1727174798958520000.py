# Based on your functional description and the provided source code files, I will create the `function.py` file to handle the described functionality. This script will initialize the home environment and execute the required actions.
# 
# Here's the `function.py` file:

# functions/function.py

from home.home_plan import home_plan, get_room
from home.actuator import Light, Curtain, MusicPlayer, CoffeeMachine, AC, CleaningRobot

def main():
    # Initialize home plan
    home = home_plan()
    
    # Get Living Room
    living_room = get_room(home, "LivingRoom")
    
    # Turn on and set light to medium brightness
    light = next((actuator for actuator in living_room.actuators if isinstance(actuator, Light)), None)
    if light:
        light.turn_on()
        light.set_brightness_level("medium")
    
    # Turn on music player and play a relaxing song
    music_player = next((actuator for actuator in living_room.actuators if isinstance(actuator, MusicPlayer)), None)
    if music_player:
        music_player.turn_on()
        music_player.play_music("Relaxing Playlist")
    
    # Turn on coffee machine and make a cup of coffee
    coffee_machine = next((actuator for actuator in living_room.actuators if isinstance(actuator, CoffeeMachine)), None)
    if coffee_machine:
        coffee_machine.turn_on()
        coffee_machine.make_coffee("coffee")
    
    # Turn on AC and set it to 22 degrees
    ac = next((actuator for actuator in living_room.actuators if isinstance(actuator, AC)), None)
    if ac:
        ac.turn_on()
        ac.set_target_temperature(22)
    
    # Turn off the curtain
    curtain = next((actuator for actuator in living_room.actuators if isinstance(actuator, Curtain)), None)
    if curtain:
        curtain.turn_off()
    
    # Turn on cleaning robot and start cleaning
    cleaning_robot = next((actuator for actuator in living_room.actuators if isinstance(actuator, CleaningRobot)), None)
    if cleaning_robot:
        cleaning_robot.turn_on()
        cleaning_robot.daily_routine()

if __name__ == "__main__":
    main()