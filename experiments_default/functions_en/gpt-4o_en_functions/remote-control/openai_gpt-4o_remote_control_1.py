# Based on your functional description and the provided source code, here is the `function.py` file that should be located in the `functions` folder. This file will contain the main function and will use the components defined in the `home` folder.
# 
# ### function.py

import time
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, OutdoorTemperatureSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, SmartSocket, Door, CleaningRobot, SmartTV
from home.home_plan import home_plan, get_room, get_all_actuators
from home.config import DAILY_ROUTINE_DURATION

def main():
    # Initialize home plan
    home = home_plan()

    # Example: Sweeping robot routine in the living room
    living_room = get_room(home, "LivingRoom")
    if living_room:
        cleaning_robot = next((actuator for actuator in living_room.actuators if isinstance(actuator, CleaningRobot)), None)
        if cleaning_robot:
            cleaning_robot.turn_on()
            cleaning_robot.daily_routine()

    # Example: Music player functionality in the bedroom
    bedroom = get_room(home, "Bedroom")
    if bedroom:
        music_player = next((actuator for actuator in bedroom.actuators if isinstance(actuator, MusicPlayer)), None)
        if music_player:
            music_player.turn_on()
            music_player.play_music("Jazz Playlist")
            music_player.play_music("Audiobook: The Great Gatsby")

    # Example: Smart TV functionality in the living room
    if living_room:
        smart_tv = next((actuator for actuator in living_room.actuators if isinstance(actuator, SmartTV)), None)
        if smart_tv:
            smart_tv.turn_on()
            smart_tv.play_channel("Voice Channel Selection: HBO")
            smart_tv.play_channel("On-Demand Movie: Inception")

    # Example: Bedroom lighting adjustment
    if bedroom:
        bedroom_lights = [actuator for actuator in bedroom.actuators if isinstance(actuator, Light)]
        for light in bedroom_lights:
            light.turn_on()
            light.set_brightness_level("medium")

    # End of operations
    print("All operations completed.")

if __name__ == "__main__":
    main()