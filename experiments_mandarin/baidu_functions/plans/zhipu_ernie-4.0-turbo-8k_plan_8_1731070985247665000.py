# Based on your functional description and the provided source code, I'll create a `function.py` file that contains the main functions to execute the MORNING PLAN, LEAVE HOME PLAN, and MOVIE PLAN. These functions will utilize the classes and methods defined in the `sensor.py`, `actuator.py`, and `home_plan.py` files.
# 
# Here's the `function.py` file:

from home.home_plan import home_plan, get_room, get_all_actuators, get_all_sensors
from home.actuator import Light, Heater, AC, SmartTV
from home.sensor import LightIntensiveSensor
from home.logger_config import logger

def morning_plan():
    home = home_plan()
    
    # Wake up and turn on the lights in the bedroom
    bedroom = get_room(home, "Bedroom")
    if bedroom:
        for actuator in bedroom.actuators:
            if isinstance(actuator, Light):
                actuator.turn_on()
                actuator.set_brightness_level("medium")
    
    # Turn on the heater if it's cold
    for sensor in get_all_sensors(home, "IndoorTemperature"):
        if sensor.room_name == "Bedroom" and sensor.get_reading() < 15:
            heater = next((actuator for actuator in bedroom.actuators if isinstance(actuator, Heater)), None)
            if heater:
                heater.turn_on()
                heater.set_target_temperature(22)
    
    # Open the curtains
    for actuator in bedroom.actuators:
        if isinstance(actuator, Curtain):
            actuator.turn_on()
    
    # Maybe play some music
    for actuator in bedroom.actuators:
        if isinstance(actuator, MusicPlayer):
            actuator.turn_on()
            actuator.play_music("Morning Playlist")
    
    logger.info("Morning Plan Executed")

def leave_home_plan():
    home = home_plan()
    
    # Turn off all lights
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, Light):
                actuator.turn_off()
    
    # Lock all doors
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, Door):
                actuator.lock()
    
    # Turn on security system (not implemented, assuming a NotificationSender or similar could be used)
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, NotificationSender):
                actuator.turn_on()
                actuator.notification_sender("Home security system activated")
    
    logger.info("Leave Home Plan Executed")

def movie_plan():
    home = home_plan()
    
    # Turn on the TV in the living room
    living_room = get_room(home, "LivingRoom")
    if living_room:
        for actuator in living_room.actuators:
            if isinstance(actuator, SmartTV):
                actuator.turn_on()
                actuator.play_channel("Movie Channel")
    
    # Turn off the lights
    for actuator in living_room.actuators:
        if isinstance(actuator, Light):
            actuator.turn_off()
    
    # Adjust the AC for a comfortable movie experience
    for sensor in get_all_sensors(home, "IndoorTemperature"):
        if sensor.room_name == "LivingRoom":
            current_temp = sensor.get_reading()
            for actuator in living_room.actuators:
                if isinstance(actuator, AC):
                    actuator.turn_on()
                    actuator.set_target_temperature(24)
                    actuator.adjust_temperature(current_temp)
    
    logger.info("Movie Plan Executed")

if __name__ == "__main__":
    # Test the functions
    morning_plan()
    leave_home_plan()
    movie_plan()