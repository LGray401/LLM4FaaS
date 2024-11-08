# Given your functional description and the provided source code, I will create a `function.py` file that includes the main function to handle the three plans: MORNING PLAN, LEAVE HOME PLAN, and MOVIE PLAN. This file will be placed in the `functions` folder as per your request.
# 
# ### `functions/function.py`

from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators
from home.actuator import Light, Window, Curtain, MusicPlayer, CoffeeMachine, AC, Heater, Door, CleaningRobot, SmartTV, NotificationSender
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
import time

def execute_morning_plan(home):
    print("Executing Morning Plan...")
    
    # Get the bedroom
    bedroom = get_room(home, "Bedroom")
    if not bedroom:
        return
    
    # Turn on the lights
    for light in get_room_actuators(bedroom, "Light"):
        light.turn_on()
        light.set_brightness_level("medium")
    
    # Open the curtains
    for curtain in get_room_actuators(bedroom, "Curtain"):
        curtain.turn_on()
    
    # Open the windows
    for window in get_room_actuators(bedroom, "Window"):
        window.turn_on()
    
    # Start playing music
    for music_player in get_room_actuators(bedroom, "MusicPlayer"):
        music_player.turn_on()
        music_player.play_music("Morning Playlist")
    
    # Make coffee
    kitchen = get_room(home, "Kitchen")
    if kitchen:
        for coffee_machine in get_room_actuators(kitchen, "CoffeeMachine"):
            coffee_machine.turn_on()
            coffee_machine.make_coffee("Latte")
    
    # Adjust the temperature
    for ac in get_room_actuators(bedroom, "AC"):
        ac.turn_on()
        ac.set_target_temperature(TEMP_HIGH)
    
    for heater in get_room_actuators(bedroom, "Heater"):
        heater.turn_on()
        heater.set_target_temperature(TEMP_HIGH)

def execute_leave_home_plan(home):
    print("Executing Leave Home Plan...")
    
    # Get all rooms
    for room in home:
        # Turn off all lights
        for light in get_room_actuators(room, "Light"):
            light.turn_off()
        
        # Close all curtains
        for curtain in get_room_actuators(room, "Curtain"):
            curtain.turn_off()
        
        # Close all windows
        for window in get_room_actuators(room, "Window"):
            window.turn_off()
        
        # Lock all doors
        for door in get_room_actuators(room, "Door"):
            door.lock()
        
        # Turn off all other actuators
        for actuator in room.actuators:
            if actuator.actuator_type not in ["Light", "Curtain", "Window", "Door"]:
                actuator.turn_off()
    
    # Notify the user
    for notification_sender in get_all_actuators(home, "NotificationSender"):
        notification_sender.turn_on()
        notification_sender.notification_sender("Goodbye! Have a nice day!")

def execute_movie_plan(home):
    print("Executing Movie Plan...")
    
    # Get the living room
    living_room = get_room(home, "LivingRoom")
    if not living_room:
        return
    
    # Dim the lights
    for light in get_room_actuators(living_room, "Light"):
        light.turn_on()
        light.set_brightness_level("low")
    
    # Close the curtains
    for curtain in get_room_actuators(living_room, "Curtain"):
        curtain.turn_on()
    
    # Play a movie on the smart TV
    for smart_tv in get_room_actuators(living_room, "SmartTV"):
        smart_tv.turn_on()
        smart_tv.play_channel("Movie Channel")
    
    # Play background music
    for music_player in get_room_actuators(living_room, "MusicPlayer"):
        music_player.turn_on()
        music_player.play_music("Relaxing Playlist")
    
    # Adjust the temperature
    for ac in get_room_actuators(living_room, "AC"):
        ac.turn_on()
        ac.set_target_temperature(TEMP_HIGH)
    
    for heater in get_room_actuators(living_room, "Heater"):
        heater.turn_on()
        heater.set_target_temperature(TEMP_HIGH)

def main():
    home = home_plan()
    while True:
        command = input("请输入指令 (MORNING PLAN, LEAVE HOME PLAN, MOVIE PLAN): ")
        if command == "小g 我要起床了":
            execute_morning_plan(home)
        elif command == "小g 我要走了 拜拜":
            execute_leave_home_plan(home)
        elif command == "小g 我想开心一下":
            execute_movie_plan(home)
        else:
            print("未知指令，请重新输入。")

if __name__ == "__main__":
    main()