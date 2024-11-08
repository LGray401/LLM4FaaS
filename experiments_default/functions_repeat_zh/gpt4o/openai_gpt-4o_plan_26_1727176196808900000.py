# Sure, based on your functional description and the provided source code, I'll create the `function.py` file to handle the "Morning Plan", "Leave Home Plan", and "Movie Plan". This file will be located in the 'functions' folder and will contain the main function to execute the plans.
# 
# Here is the `function.py`:

import time
from home.home_plan import home_plan, get_all_actuators, get_room_actuators, get_room_sensors
from home.config import LIGHT_INTENSITY_HIGH, LIGHT_INTENSITY_LOW

def morning_plan(home):
    print("Executing Morning Plan...")
    living_room_actuators = get_room_actuators(home, "LivingRoom")
    kitchen_actuators = get_room_actuators(home, "Kitchen")

    # Turn on all lights
    for actuator in living_room_actuators:
        if actuator.actuator_type == "Light":
            actuator.turn_on()

    # Adjust light brightness based on indoor light intensity
    light_sensors = get_all_sensors(home, "LightIntensive")
    for sensor in light_sensors:
        sensor.turn_on()
        reading = sensor.get_reading()
        if reading:
            for actuator in living_room_actuators:
                if actuator.actuator_type == "Light":
                    if reading < LIGHT_INTENSITY_LOW:
                        actuator.set_brightness_level("high")
                    elif reading > LIGHT_INTENSITY_HIGH:
                        actuator.set_brightness_level("low")
                    else:
                        actuator.set_brightness_level("medium")

    # Make a cup of cappuccino
    for actuator in kitchen_actuators:
        if actuator.actuator_type == "CoffeeMachine":
            actuator.turn_on()
            actuator.make_coffee("Cappuccino")

    # Open curtains
    for actuator in living_room_actuators:
        if actuator.actuator_type == "Curtain":
            actuator.turn_on()

    # Play relaxing music
    for actuator in living_room_actuators:
        if actuator.actuator_type == "MusicPlayer":
            actuator.turn_on()
            actuator.play_music("Relaxing Music")

def leave_home_plan(home):
    print("Executing Leave Home Plan...")
    all_lights = get_all_actuators(home, "Light")
    all_sockets = get_all_actuators(home, "SmartSocket")
    all_doors = get_all_actuators(home, "Door")

    # Turn off all lights
    for light in all_lights:
        light.turn_off()

    # Turn off all sockets
    for socket in all_sockets:
        socket.turn_off()

    # Close all doors
    for door in all_doors:
        door.lock()

def movie_plan(home):
    print("Executing Movie Plan...")
    living_room_actuators = get_room_actuators(home, "LivingRoom")

    # Close curtains
    for actuator in living_room_actuators:
        if actuator.actuator_type == "Curtain":
            actuator.turn_off()

    # Dim lights
    for actuator in living_room_actuators:
        if actuator.actuator_type == "Light":
            actuator.turn_on()
            actuator.set_brightness_level("low")

def main():
    home = home_plan()

    # Execute plans
    morning_plan(home)
    time.sleep(2)  # Wait for 2 seconds before executing the next plan
    leave_home_plan(home)
    time.sleep(2)  # Wait for 2 seconds before executing the next plan
    movie_plan(home)

if __name__ == "__main__":
    main()