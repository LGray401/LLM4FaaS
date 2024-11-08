# Based on the provided functional description and source code, I will create a `function.py` file that includes a main function to handle the morning plan, leave home plan, and movie plan. The main function will be responsible for orchestrating the actions of the sensors and actuators in the smart home.
# 
# Here is the `function.py` file:

# functions/function.py

from home.home_plan import home_plan, get_room_actuators
from home.actuator import Light, AC, Heater, MusicPlayer, SmartTV, CoffeeMachine
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
import time

def execute_morning_plan(home):
    print("\nExecuting Morning Plan...")
    
    # Turn on lights in all rooms
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, Light):
                actuator.turn_on()
                actuator.set_brightness_level("medium")
    
    # Start coffee machine in the kitchen
    kitchen = get_room_actuators(home, "Kitchen")
    for actuator in kitchen:
        if isinstance(actuator, CoffeeMachine):
            actuator.turn_on()
            actuator.make_coffee("Espresso")
    
    # Play music in the living room
    living_room = get_room_actuators(home, "LivingRoom")
    for actuator in living_room:
        if isinstance(actuator, MusicPlayer):
            actuator.turn_on()
            actuator.play_music("Morning Playlist")

def execute_leave_home_plan(home):
    print("\nExecuting Leave Home Plan...")
    
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
    
    # Turn off all other actuators
    for room in home:
        for actuator in room.actuators:
            if not isinstance(actuator, (Door, Light)):
                actuator.turn_off()

def execute_movie_plan(home):
    print("\nExecuting Movie Plan...")
    
    # Turn on lights in the living room and set to low brightness
    living_room = get_room_actuators(home, "LivingRoom")
    for actuator in living_room:
        if isinstance(actuator, Light):
            actuator.turn_on()
            actuator.set_brightness_level("low")
    
    # Turn on the smart TV in the living room
    for actuator in living_room:
        if isinstance(actuator, SmartTV):
            actuator.turn_on()
            actuator.play_channel("Movie Channel")
    
    # Play background music in the living room
    for actuator in living_room:
        if isinstance(actuator, MusicPlayer):
            actuator.turn_on()
            actuator.play_music("Background Music")

def main():
    home = home_plan()
    
    # Execute the morning plan
    execute_morning_plan(home)
    time.sleep(5)  # Simulate some time passing
    
    # Execute the leave home plan
    execute_leave_home_plan(home)
    time.sleep(5)  # Simulate some time passing
    
    # Execute the movie plan
    execute_movie_plan(home)

if __name__ == "__main__":
    main()