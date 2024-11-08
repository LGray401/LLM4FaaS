# Based on your project description and provided source code files, I'll create a `function.py` file to handle the main functionalities as outlined in your functional description. This file will be located in the 'functions' folder and will import necessary classes and functions from the 'home' folder.
# 
# Here's the `function.py` file:

# functions/function.py

from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor
from home.actuator import CleaningRobot, MusicPlayer, SmartTV, Light
from home.home_plan import home_plan, get_room

def main():
    home = home_plan()

    # Example usage of each functionality
    # 1. Cleaning Robot: start cleaning, spot cleaning, end cleaning
    living_room = get_room(home, "LivingRoom")
    for actuator in living_room.actuators:
        if isinstance(actuator, CleaningRobot):
            actuator.turn_on()
            actuator.daily_routine()
            # For spot cleaning, we can implement a similar method in the CleaningRobot class if needed
            actuator.turn_off()

    # 2. Music Player: select song, listen to audiobook
    for actuator in living_room.actuators:
        if isinstance(actuator, MusicPlayer):
            actuator.turn_on()
            actuator.play_music("Favorite Songs Playlist")
            actuator.play_music("Audiobook: '1984' by George Orwell")
            actuator.turn_off()

    # 3. TV: voice channel switching, on-demand movies, TV series
    for actuator in living_room.actuators:
        if isinstance(actuator, SmartTV):
            actuator.turn_on()
            actuator.play_channel("News Channel")
            actuator.play_channel("Movie: 'Inception'")
            actuator.play_channel("TV Series: 'Friends'")
            actuator.turn_off()

    # 4. Bedroom lighting: on, off, brightness adjustment
    bedroom = get_room(home, "Bedroom")
    for actuator in bedroom.actuators:
        if isinstance(actuator, Light):
            actuator.turn_on()
            actuator.set_brightness_level("high")
            actuator.set_brightness_level("medium")
            actuator.set_brightness_level("low")
            actuator.turn_off()

if __name__ == "__main__":
    main()