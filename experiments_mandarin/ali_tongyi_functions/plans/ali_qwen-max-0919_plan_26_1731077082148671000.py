# Based on the provided functional description and source code, I will create a `function.py` file that includes the main function to implement the morning plan, leave home plan, and movie plan. This file will be placed in the `functions` folder.
# 
# Here is the `function.py` file:

# functions/function.py

from datetime import datetime, time
import random
from home.home_plan import home_plan, get_room_actuators, get_room_sensors
from home.actuator import Light, Curtain, MusicPlayer, CoffeeMachine, Door, SmartSocket
from home.sensor import LightIntensiveSensor
from home.config import LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def execute_morning_plan():
    print("Executing Morning Plan...")
    home = home_plan()
    
    # Get actuators and sensors for the LivingRoom
    living_room_actuators = get_room_actuators(home, "LivingRoom")
    living_room_sensors = get_room_sensors(home, "LivingRoom")

    # Turn on the lights
    for actuator in living_room_actuators:
        if isinstance(actuator, Light):
            actuator.turn_on()
            actuator.set_brightness_level("medium")

    # Make a cappuccino
    for actuator in living_room_actuators:
        if isinstance(actuator, CoffeeMachine):
            actuator.turn_on()
            actuator.make_coffee("cappuccino")

    # Open the curtains
    for actuator in living_room_actuators:
        if isinstance(actuator, Curtain):
            actuator.turn_on()

    # Play relaxing light music
    for actuator in living_room_actuators:
        if isinstance(actuator, MusicPlayer):
            actuator.turn_on()
            actuator.play_music("Relaxing Light Music")

    # Adjust the light based on the indoor light intensity
    for sensor in living_room_sensors:
        if isinstance(sensor, LightIntensiveSensor):
            sensor.turn_on()
            light_reading = sensor.get_reading()
            if light_reading < LIGHT_INTENSITY_LOW:
                for actuator in living_room_actuators:
                    if isinstance(actuator, Light):
                        actuator.set_brightness_level("high")
            elif light_reading > LIGHT_INTENSITY_HIGH:
                for actuator in living_room_actuators:
                    if isinstance(actuator, Light):
                        actuator.set_brightness_level("low")
            else:
                for actuator in living_room_actuators:
                    if isinstance(actuator, Light):
                        actuator.set_brightness_level("medium")
            sensor.turn_off()

def execute_leave_home_plan():
    print("Executing Leave Home Plan...")
    home = home_plan()
    
    # Turn off all lights and smart sockets, and close all doors
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, Light):
                actuator.turn_off()
            elif isinstance(actuator, SmartSocket):
                actuator.turn_off()
            elif isinstance(actuator, Door):
                actuator.lock()

def execute_movie_plan():
    print("Executing Movie Plan...")
    home = home_plan()
    
    # Get actuators for the LivingRoom
    living_room_actuators = get_room_actuators(home, "LivingRoom")

    # Close the curtains
    for actuator in living_room_actuators:
        if isinstance(actuator, Curtain):
            actuator.turn_on()

    # Dim the lights
    for actuator in living_room_actuators:
        if isinstance(actuator, Light):
            actuator.turn_on()
            actuator.set_brightness_level("low")

def main():
    current_time = datetime.now().time()
    
    if current_time == time(7, 0):  # Check if it's 7:00 AM
        execute_morning_plan()
    elif current_time == time(8, 0):  # Example: Check if it's 8:00 AM (assuming this is when you leave home)
        execute_leave_home_plan()
    elif current_time == time(20, 0):  # Example: Check if it's 8:00 PM (assuming this is when you watch a movie)
        execute_movie_plan()

if __name__ == "__main__":
    main()