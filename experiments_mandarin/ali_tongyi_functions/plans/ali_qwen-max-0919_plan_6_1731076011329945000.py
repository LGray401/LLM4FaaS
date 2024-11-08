# Based on your functional description and the provided source code, I will create a `function.py` file that contains the main function to execute the morning plan, leave home plan, and movie plan. This file will be located in the `functions` folder.
# 
# Here is the `function.py` file:

# functions/function.py

from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_actuators
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, SmartSocket, Door, CleaningRobot, SmartTV
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, DAILY_ROUTINE_DURATION
from home.logger_config import logger
import time

def morning_plan(home):
    logger.info("Starting Morning Plan")
    
    # Get bedroom
    bedroom = get_room(home, "Bedroom")
    if not bedroom:
        logger.error("Bedroom not found")
        return
    
    # Turn on lights
    for light in get_room_actuators(home, "Bedroom"):
        if isinstance(light, Light):
            light.turn_on()
            light.set_brightness_level("high")
    
    # Open curtains
    for curtain in get_room_actuators(home, "Bedroom"):
        if isinstance(curtain, Curtain):
            curtain.turn_on()
    
    # Play music
    for music_player in get_room_actuators(home, "Bedroom"):
        if isinstance(music_player, MusicPlayer):
            music_player.turn_on()
            music_player.play_music("Morning Playlist")
    
    # Make coffee
    kitchen = get_room(home, "Kitchen")
    if kitchen:
        for coffee_machine in get_room_actuators(kitchen, "CoffeeMachine"):
            if isinstance(coffee_machine, CoffeeMachine):
                coffee_machine.turn_on()
                coffee_machine.make_coffee("Cappuccino")
    
    logger.info("Morning Plan Completed")

def leave_home_plan(home):
    logger.info("Starting Leave Home Plan")
    
    # Lock all doors
    for door in get_all_actuators(home, "Door"):
        door.turn_off()
        door.lock()
    
    # Turn off all lights
    for light in get_all_actuators(home, "Light"):
        light.turn_off()
    
    # Turn off all music players
    for music_player in get_all_actuators(home, "MusicPlayer"):
        music_player.turn_off()
    
    # Send notification
    for notification_sender in get_all_actuators(home, "NotificationSender"):
        notification_sender.turn_on()
        notification_sender.notification_sender("You have left home. All systems are secured.")
    
    logger.info("Leave Home Plan Completed")

def movie_plan(home):
    logger.info("Starting Movie Plan")
    
    # Get living room
    living_room = get_room(home, "LivingRoom")
    if not living_room:
        logger.error("LivingRoom not found")
        return
    
    # Dim lights
    for light in get_room_actuators(living_room, "Light"):
        if isinstance(light, Light):
            light.turn_on()
            light.set_brightness_level("low")
    
    # Close curtains
    for curtain in get_room_actuators(living_room, "Curtain"):
        if isinstance(curtain, Curtain):
            curtain.turn_off()
    
    # Start playing movie on Smart TV
    for smart_tv in get_room_actuators(living_room, "SmartTV"):
        if isinstance(smart_tv, SmartTV):
            smart_tv.turn_on()
            smart_tv.play_channel("Movie Channel")
    
    # Play background music
    for music_player in get_room_actuators(living_room, "MusicPlayer"):
        if isinstance(music_player, MusicPlayer):
            music_player.turn_on()
            music_player.play_music("Relaxing Background Music")
    
    logger.info("Movie Plan Completed")

def main():
    home = home_plan()
    
    # Example usage of the plans
    morning_plan(home)
    time.sleep(5)  # Simulate some time passing
    leave_home_plan(home)
    time.sleep(5)  # Simulate some time passing
    movie_plan(home)

if __name__ == "__main__":
    main()