# Based on your functional description and the provided source code, here is a `function.py` file that integrates all the functionalities you mentioned:

from home.home_plan import home_plan, get_room, get_all_actuators, get_room_actuators
from home.actuator import CleaningRobot, MusicPlayer, SmartTV, Light
import time

def start_cleaning(room_name, home):
    room = get_room(home, room_name)
    if room:
        actuators = get_room_actuators(home, room_name)
        for actuator in actuators:
            if isinstance(actuator, CleaningRobot) and actuator.status == "off":
                actuator.turn_on()
                actuator.daily_routine()
                break

def spot_cleaning(room_name, home, duration=1):
    room = get_room(home, room_name)
    if room:
        actuators = get_room_actuators(home, room_name)
        for actuator in actuators:
            if isinstance(actuator, CleaningRobot) and actuator.status == "off":
                actuator.turn_on()
                print(f"Starting spot cleaning for {duration} seconds in {room_name}...")
                time.sleep(duration)
                actuator.turn_off()
                print(f"Spot cleaning finished in {room_name}.")
                break

def stop_cleaning(room_name, home):
    room = get_room(home, room_name)
    if room:
        actuators = get_room_actuators(home, room_name)
        for actuator in actuators:
            if isinstance(actuator, CleaningRobot) and actuator.status == "on":
                actuator.turn_off()
                print(f"Cleaning stopped in {room_name}.")
                break

def play_music(room_name, home, playlist):
    room = get_room(home, room_name)
    if room:
        actuators = get_room_actuators(home, room_name)
        for actuator in actuators:
            if isinstance(actuator, MusicPlayer) and actuator.status == "off":
                actuator.turn_on()
                actuator.play_music(playlist)
                break
        else:
            print(f"Music Player is not available or already on in {room_name}.")

def listen_to_book(room_name, home, book_name):
    # Assuming book_name is just a placeholder for now, and play_music can handle different types of audio
    play_music(room_name, home, book_name)  # Using play_music function for simplicity

def watch_tv(room_name, home, channel_name):
    room = get_room(home, room_name)
    if room:
        actuators = get_room_actuators(home, room_name)
        for actuator in actuators:
            if isinstance(actuator, SmartTV) and actuator.status == "off":
                actuator.turn_on()
                actuator.play_channel(channel_name)
                break
        else:
            print(f"SmartTV is not available or already on in {room_name}.")

def adjust_light(room_name, home, level_name):
    room = get_room(home, room_name)
    if room:
        actuators = get_room_actuators(home, room_name)
        for actuator in actuators:
            if isinstance(actuator, Light):
                if actuator.status == "off":
                    actuator.turn_on()
                actuator.set_brightness_level(level_name)
                break
        else:
            print(f"Light is not available in {room_name}.")

def turn_light_on(room_name, home):
    room = get_room(home, room_name)
    if room:
        actuators = get_room_actuators(home, room_name)
        for actuator in actuators:
            if isinstance(actuator, Light) and actuator.status == "off":
                actuator.turn_on()
                print(f"Light turned on in {room_name}.")
                break

def turn_light_off(room_name, home):
    room = get_room(home, room_name)
    if room:
        actuators = get_room_actuators(home, room_name)
        for actuator in actuators:
            if isinstance(actuator, Light) and actuator.status == "on":
                actuator.turn_off()
                print(f"Light turned off in {room_name}.")
                break

# Main function to demonstrate functionalities
def main():
    home = home_plan()
    
    # Example usage:
    start_cleaning("LivingRoom", home)
    time.sleep(2)  # Simulate some delay
    stop_cleaning("LivingRoom", home)

    play_music("Bedroom", home, "Relaxing Playlist")

    watch_tv("LivingRoom", home, "News Channel")

    adjust_light("Bedroom", home, "medium")

    turn_light_on("Kitchen", home)
    time.sleep(2)  # Simulate some delay
    turn_light_off("Kitchen", home)

if __name__ == "__main__":
    main()