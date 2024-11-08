# Based on the given functional description and source code files, I will create a `function.py` file that contains the main function to execute different home plans: MORNING PLAN, LEAVE HOME PLAN, and MOVIE PLAN. This file will interact with the sensors and actuators defined in the `home` folder.
# 
# Here is the `function.py` file:

# function.py
from home.sensor import LightIntensiveSensor
from home.actuator import CoffeeMachine, Curtain, Light, Door, SmartSocket, SmartTV
from home.home_plan import home_plan, get_room, get_all_actuators
from home.config import LIGHT_INTENSITY_LOW

def morning_plan(home):
    print("Executing Morning Plan...")
    # Get relevant actuators
    living_room = get_room(home, "LivingRoom")
    bedroom = get_room(home, "Bedroom")
    kitchen = get_room(home, "Kitchen")

    # Open curtains in the bedroom
    for actuator in bedroom.actuators:
        if isinstance(actuator, Curtain):
            actuator.turn_on()
            print(f"Curtains in {bedroom.name} are now OPEN.")

    # Turn on coffee machine in the kitchen
    for actuator in kitchen.actuators:
        if isinstance(actuator, CoffeeMachine):
            actuator.turn_on()
            actuator.make_coffee("normal")
            print(f"Coffee Machine in {kitchen.name} is now ON and making coffee.")

    # Check light intensity in the living room and turn on lights if it's dark
    for sensor in living_room.sensors:
        if isinstance(sensor, LightIntensiveSensor):
            sensor.turn_on()
            light_intensity = sensor.get_reading()
            if light_intensity is not None and light_intensity < LIGHT_INTENSITY_LOW:
                for actuator in living_room.actuators:
                    if isinstance(actuator, Light):
                        actuator.turn_on()
                        actuator.set_brightness_level("medium")
                        print(f"Lights in {living_room.name} are now ON with MEDIUM brightness.")

def leave_home_plan(home):
    print("Executing Leave Home Plan...")
    # Lock all doors
    for actuator in get_all_actuators(home, "Door"):
        actuator.lock()
    
    # Turn off all lights
    for actuator in get_all_actuators(home, "Light"):
        actuator.turn_off()
    
    # Turn off all smart sockets
    for actuator in get_all_actuators(home, "SmartSocket"):
        actuator.turn_off()

def movie_plan(home):
    print("Executing Movie Plan...")
    # Get relevant actuators
    living_room = get_room(home, "LivingRoom")

    # Close curtains in the living room
    for actuator in living_room.actuators:
        if isinstance(actuator, Curtain):
            actuator.turn_off()
            print(f"Curtains in {living_room.name} are now CLOSED.")

    # Set lights to dark mode
    for actuator in living_room.actuators:
        if isinstance(actuator, Light):
            actuator.turn_on()
            actuator.set_brightness_level("low")
            print(f"Lights in {living_room.name} are now ON with LOW brightness.")

    # Turn on the TV and play movie
    for actuator in living_room.actuators:
        if isinstance(actuator, SmartTV):
            actuator.turn_on()
            actuator.play_channel("movie_channel")
            print(f"Smart TV in {living_room.name} is now ON and playing movie.")

def main():
    home = home_plan()
    print_home_plan(home)

    # Execute different plans
    morning_plan(home)
    leave_home_plan(home)
    movie_plan(home)

if __name__ == "__main__":
    main()