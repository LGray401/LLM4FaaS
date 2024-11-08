# Based on the provided functional description and the source code files, here is the 'functions/function.py' file that implements the main function to handle the "MORNING PLAN", "LEAVE HOME PLAN", and "MOVIE PLAN":
# 
# ### functions/function.py

import time
from home.home_plan import home_plan, get_room_actuators, get_all_actuators
from home.config import TEMP_HIGH, TEMP_LOW

def morning_plan(home):
    print("Executing Morning Plan...")
    bedroom_actuators = get_room_actuators(home, "Bedroom")
    kitchen_actuators = get_room_actuators(home, "Kitchen")
    
    # Turn on the coffee machine in the kitchen
    for actuator in kitchen_actuators:
        if actuator.actuator_type == "CoffeeMachine":
            actuator.turn_on()
            actuator.make_coffee("Espresso")
    
    # Turn on the heater in the bedroom if the temperature is too low
    for actuator in bedroom_actuators:
        if actuator.actuator_type == "Heater":
            actuator.turn_on()
            actuator.set_target_temperature(TEMP_HIGH - 5)
            # Simulate temperature adjustment
            actuator.adjust_temperature(TEMP_LOW)

def leave_home_plan(home):
    print("Executing Leave Home Plan...")
    all_actuators = get_all_actuators(home, "Light")

    # Turn off all lights
    for actuator in all_actuators:
        actuator.turn_off()

    # Lock all doors
    all_doors = get_all_actuators(home, "Door")
    for door in all_doors:
        door.lock()

def movie_plan(home):
    print("Executing Movie Plan...")
    living_room_actuators = get_room_actuators(home, "LivingRoom")
    
    # Dim the lights in the living room
    for actuator in living_room_actuators:
        if actuator.actuator_type == "Light":
            actuator.turn_on()
            actuator.set_brightness_level("low")
    
    # Turn on the Smart TV and play a movie channel
    for actuator in living_room_actuators:
        if actuator.actuator_type == "SmartTV":
            actuator.turn_on()
            actuator.play_channel("Movie Channel")

def main():
    home = home_plan()
    morning_plan(home)
    time.sleep(2)
    leave_home_plan(home)
    time.sleep(2)
    movie_plan(home)

if __name__ == "__main__":
    main()