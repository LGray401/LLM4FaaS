# Based on the provided functional description and the source code files, I will create the `function.py` file to manage the sequence of actions for your smart home project. Here's the implementation:

# function.py

from home.home_plan import home_plan, get_room
from home.logger_config import logger

def main():
    # Initialize the home plan
    home = home_plan()
    
    # Living room actions
    living_room = get_room(home, "LivingRoom")
    if living_room:
        # Turn on the light and set to medium brightness
        light = next((act for act in living_room.actuators if act.actuator_type == "Light"), None)
        if light:
            light.turn_on()
            light.set_brightness_level("medium")

        # Play a relaxing song
        music_player = next((act for act in living_room.actuators if act.actuator_type == "MusicPlayer"), None)
        if music_player:
            music_player.turn_on()
            music_player.play_music("Relaxing Playlist")

        # Turn on the coffee machine to make coffee
        coffee_machine = next((act for act in living_room.actuators if act.actuator_type == "CoffeeMachine"), None)
        if coffee_machine:
            coffee_machine.turn_on()
            coffee_machine.make_coffee("Standard Coffee")

        # Turn on the AC and set the temperature to 22°C
        ac = next((act for act in living_room.actuators if act.actuator_type == "AC"), None)
        if ac:
            ac.turn_on()
            ac.set_target_temperature(22)

        # Close the curtains
        curtain = next((act for act in living_room.actuators if act.actuator_type == "Curtain"), None)
        if curtain:
            curtain.turn_on()

        # Start the cleaning robot
        cleaning_robot = next((act for act in living_room.actuators if act.actuator_type == "CleaningRobot"), None)
        if cleaning_robot:
            cleaning_robot.turn_on()
            cleaning_robot.daily_routine()

if __name__ == "__main__":
    main()