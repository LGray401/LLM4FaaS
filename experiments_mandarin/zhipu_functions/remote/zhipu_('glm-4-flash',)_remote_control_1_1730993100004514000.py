# Based on the provided functional description and source code, here is the `function.py` file you requested. This file contains the main function that you can use to interact with the smart home components.

# function.py
from home.sensor import Sensor
from home.actuator import Actuator
from home.home_plan import home_plan

def main():
    # Load the home plan
    home = home_plan()
    
    # Example usage:
    # 1. Turn on the cleaning robot in the Living Room
    living_room = get_room(home, "LivingRoom")
    if living_room:
        cleaning_robot = get_room_actuators(living_room, "CleaningRobot")
        if cleaning_robot:
            cleaning_robot[0].turn_on()
    
    # 2. Set the target temperature of the AC in the Living Room to 20°C
    ac = get_all_actuators(home, "AC")
    if ac:
        ac[0].set_target_temperature(20)
    
    # 3. Turn off the light in the Bedroom
    bedroom = get_room(home, "Bedroom")
    if bedroom:
        lights = get_room_actuators(bedroom, "Light")
        if lights:
            lights[0].turn_off()
    
    # 4. Play some music on the Music Player in the Living Room
    music_player = get_room_actuators(living_room, "MusicPlayer")
    if music_player:
        music_player[0].play_music("playlist_name")
    
    # 5. Lock the door in the Living Room
    door = get_room_actuators(living_room, "Door")
    if door:
        door[0].lock()

if __name__ == "__main__":
    main()