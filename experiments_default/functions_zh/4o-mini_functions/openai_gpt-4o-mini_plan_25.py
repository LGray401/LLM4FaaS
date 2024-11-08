# Based on the functional description you provided, I'll create the `function.py` file for your smart home project. This file will implement the specified plans: MORNING PLAN, LEAVE HOME PLAN, and MOVIE PLAN. Each plan will utilize the classes from your existing `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py` files.
# 
# Here's the content for `function.py`:

# function.py

from home.home_plan import home_plan
from home.actuator import Curtain, Light, MusicPlayer, CoffeeMachine, SmartTV, Door
from home.sensor import LightIntensiveSensor
from home.logger_config import logger
import time

# Threshold for light intensity to trigger the morning plan
LIGHT_INTENSITY_THRESHOLD = 800  # Example threshold (lux)

def morning_plan(home):
    # Get the Living Room which is assumed to be where the events are to occur
    living_room = next((room for room in home if room.name == "LivingRoom"), None)
    
    if living_room:
        # Check the light intensity sensor
        light_sensor = next((sensor for sensor in living_room.sensors if isinstance(sensor, LightIntensiveSensor)), None)
        
        if light_sensor:
            light_sensor.turn_on()  # Ensure the sensor is on
            light_reading = light_sensor.get_reading()
            
            if light_reading and light_reading >= LIGHT_INTENSITY_THRESHOLD:
                logger.info("Light intensity threshold met. Executing morning plan.")
                
                # Execute morning actions
                curtain = next((actuator for actuator in living_room.actuators if isinstance(actuator, Curtain)), None)
                light = next((actuator for actuator in living_room.actuators if isinstance(actuator, Light)), None)
                music_player = next((actuator for actuator in living_room.actuators if isinstance(actuator, MusicPlayer)), None)
                coffee_machine = next((actuator for actuator in living_room.actuators if isinstance(actuator, CoffeeMachine)), None)
                
                if curtain:
                    curtain.turn_on()  # Open curtains
                if light:
                    light.turn_off()  # Turn off bedroom light
                if music_player:
                    music_player.turn_on()  # Turn on music player
                    music_player.play_music("Morning Playlist")  # Play music
                if coffee_machine:
                    coffee_machine.turn_on()  # Turn on coffee machine
                    coffee_machine.make_coffee("Espresso")  # Make coffee
                
                logger.info("Morning plan executed.")
            else:
                logger.info("Light intensity threshold not met. Morning plan not executed.")
        else:
            logger.warning("Light intensity sensor not found in Living Room.")
    else:
        logger.warning("Living Room not found in home.")

def leave_home_plan(home):
    # Get the main door actuator
    main_door = next((room for room in home if room.name == "LivingRoom"), None)
    
    if main_door:
        door = next((actuator for actuator in main_door.actuators if isinstance(actuator, Door)), None)
        curtain = next((actuator for actuator in main_door.actuators if isinstance(actuator, Curtain)), None)
        light = next((actuator for actuator in main_door.actuators if isinstance(actuator, Light)), None)
        smart_socket = next((actuator for actuator in main_door.actuators if isinstance(actuator, SmartSocket)), None)
        
        if door:
            door.lock()  # Lock the door
            logger.info("Door locked.")
        
        if curtain:
            curtain.turn_off()  # Close curtains
        if light:
            light.turn_off()  # Turn off lights
        if smart_socket:
            smart_socket.turn_off()  # Turn off sockets
        
        logger.info("Leave home plan executed.")
    else:
        logger.warning("Living Room not found in home.")

def movie_plan(home):
    # Get the Living Room where the TV is assumed to be
    living_room = next((room for room in home if room.name == "LivingRoom"), None)

    if living_room:
        tv = next((actuator for actuator in living_room.actuators if isinstance(actuator, SmartTV)), None)
        curtain = next((actuator for actuator in living_room.actuators if isinstance(actuator, Curtain)), None)
        light = next((actuator for actuator in living_room.actuators if isinstance(actuator, Light)), None)
        
        if tv:
            tv.turn_on()  # Turn on the TV
            tv.play_channel("Movie Channel")  # Play a specific channel
            logger.info("TV turned on and playing Movie Channel.")
        
        if curtain:
            curtain.turn_off()  # Close curtains
        if light:
            light.set_brightness_level("low")  # Dim the lights
        
        logger.info("Movie plan executed.")
    else:
        logger.warning("Living Room not found in home.")

def main():
    home = home_plan()
    
    # Example invocation of the plans
    morning_plan(home)
    time.sleep(1)  # Simulating some delay
    leave_home_plan(home)
    time.sleep(1)  # Simulating some delay
    movie_plan(home)

if __name__ == "__main__":
    main()