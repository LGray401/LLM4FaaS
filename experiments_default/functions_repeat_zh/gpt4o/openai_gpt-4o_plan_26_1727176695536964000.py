# Based on the given functional description and source code, here is the `function.py` file which contains the main function to implement the required functionalities:

import time
from home.home_plan import home_plan, get_room, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def morning_plan(home):
    print("\nStarting MORNING PLAN...")
    # Get required actuators
    living_room = get_room(home, "LivingRoom")
    kitchen = get_room(home, "Kitchen")

    # Turn on lights in LivingRoom
    for actuator in living_room.actuators:
        if actuator.actuator_type == "Light":
            actuator.turn_on()
            break

    # Ensure light intensity is within the desired range
    light_sensor = next(sensor for sensor in living_room.sensors if sensor.sensor_type == "LightIntensive")
    light_sensor.turn_on()
    while True:
        light_intensity = light_sensor.get_reading()
        if light_intensity is not None and LIGHT_INTENSITY_LOW <= light_intensity <= LIGHT_INTENSITY_HIGH:
            break
        for actuator in living_room.actuators:
            if actuator.actuator_type == "Light":
                actuator.turn_on()
                break
        time.sleep(1)

    # Make coffee in Kitchen
    coffee_machine = next(actuator for actuator in kitchen.actuators if actuator.actuator_type == "CoffeeMachine")
    coffee_machine.turn_on()
    coffee_machine.make_coffee("Cappuccino")

    # Open curtains in LivingRoom
    curtain = next(actuator for actuator in living_room.actuators if actuator.actuator_type == "Curtain")
    curtain.turn_on()

    # Play relaxing music in LivingRoom
    music_player = next(actuator for actuator in living_room.actuators if actuator.actuator_type == "MusicPlayer")
    music_player.turn_on()
    music_player.play_music("Relaxing Music")

def leave_home_plan(home):
    print("\nStarting LEAVE HOME PLAN...")
    for room in home:
        for actuator in room.actuators:
            if actuator.actuator_type == "Door":
                actuator.lock()
            elif actuator.actuator_type == "Light":
                actuator.turn_off()
            elif actuator.actuator_type == "SmartSocket":
                actuator.turn_off()

def movie_plan(home):
    print("\nStarting MOVIE PLAN...")
    living_room = get_room(home, "LivingRoom")

    # Close curtains in LivingRoom
    curtain = next(actuator for actuator in living_room.actuators if actuator.actuator_type == "Curtain")
    curtain.turn_off()

    # Dim lights in LivingRoom
    for actuator in living_room.actuators:
        if actuator.actuator_type == "Light":
            actuator.turn_on()
            actuator.set_brightness_level("low")
            break

def main():
    home = home_plan()
    
    # Execute the plans
    morning_plan(home)
    time.sleep(2)  # Wait for a while before executing the next plan
    leave_home_plan(home)
    time.sleep(2)  # Wait for a while before executing the next plan
    movie_plan(home)

if __name__ == "__main__":
    main()