# Based on the provided functional description and source code, here is a `function.py` file that would be a part of your smart home project. This file will contain a main function that demonstrates how to interact with the sensor and actuator classes defined in your other files.

# function.py
import os

# Set the current working directory to the 'functions' folder
os.chdir('functions')

# Import necessary modules and classes
from sensor import Sensor, IndoorTemperatureSensor, OutdoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, \
    SmokeSensor
from actuator import Actuator, Heater, AC, CoffeeMachine, SmartTV, Light, Window, Curtain, MusicPlayer, Door, \
    CleaningRobot, NotificationSender, SmartSocket, Humidifier
from home_plan import home_plan

def main():
    # Create the home plan
    home = home_plan()
    
    # Example usage of the system
    # MORNING PLAN
    print("MORNING PLAN")
    # Turn on the light in the living room
    living_room_light = get_room_actuators(home, "LivingRoom")[0]  # Assuming there is only one light in the living room
    living_room_light.turn_on()
    
    # LEAVE HOME PLAN
    print("\nLEAVE HOME PLAN")
    # Turn off the light and lock the door in the living room
    living_room_light.turn_off()
    living_room_door = get_room_actuators(home, "LivingRoom")[1]  # Assuming there is only one door in the living room
    living_room_door.lock()
    
    # MOVIE PLAN
    print("\nMOVIE PLAN")
    # Turn on the TV and set the volume in the living room
    living_room_tv = get_room_actuators(home, "LivingRoom")[2]  # Assuming there is only one TV in the living room
    living_room_tv.play_channel("HBO")
    
    # Turn on the AC to cool the room
    living_room_ac = get_room_actuators(home, "LivingRoom")[3]  # Assuming there is only one AC in the living room
    living_room_ac.set_target_temperature(20)
    
    # Play some music
    living_room_music_player = get_room_actuators(home, "LivingRoom")[4]  # Assuming there is only one music player in the living room
    living_room_music_player.play_music("Rock Playlist")

def get_room_actuators(home, room_name):
    room = get_room(home, room_name)
    if room:
        return room.actuators
    else:
        print(f"No room named '{room_name}' found.")
        return []

def get_room(home, room_name):
    for room in home:
        if room.name == room_name:
            return room
    print(f"No room named '{room_name}' found.")
    return None

if __name__ == "__main__":
    main()