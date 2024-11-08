# Based on the functional description and source code you've provided, I will create a `function.py` file that integrates the functionalities for the cleaning robot, music player, smart TV, and bedroom light control. Below is the content of `function.py`:

# function.py
from home.home_plan import home_plan, get_room, get_room_actuators, get_room_sensors
from home.actuator import CleaningRobot, MusicPlayer, SmartTV, Light
from home.logger_config import logger

def main():
    # Create the home plan
    home = home_plan()
    
    # Example usage of cleaning robot
    living_room = get_room(home, "LivingRoom")
    if living_room:
        cleaning_robot = next((actuator for actuator in living_room.actuators if isinstance(actuator, CleaningRobot)), None)
        if cleaning_robot:
            cleaning_robot.turn_on()
            cleaning_robot.daily_routine()

    # Example usage of music player
    bedroom = get_room(home, "Bedroom")
    if bedroom:
        music_player = next((actuator for actuator in bedroom.actuators if isinstance(actuator, MusicPlayer)), None)
        if music_player:
            music_player.turn_on()
            music_player.play_music("Chill Playlist")

    # Example usage of smart TV
    living_room = get_room(home, "LivingRoom")
    if living_room:
        smart_tv = next((actuator for actuator in living_room.actuators if isinstance(actuator, SmartTV)), None)
        if smart_tv:
            smart_tv.turn_on()
            smart_tv.play_channel("News Channel")

    # Example usage of bedroom light control
    bedroom = get_room(home, "Bedroom")
    if bedroom:
        light = next((actuator for actuator in bedroom.actuators if isinstance(actuator, Light)), None)
        if light:
            light.turn_on()
            light.set_brightness_level("high")  # Set brightness to high
            light.set_brightness_level("low")   # Change brightness to low
            light.turn_off()

if __name__ == "__main__":
    main()