# Based on the functional description and the provided code files, I will create a `function.py` file that includes the main function to execute the specified plans: MORNING PLAN, LEAVE HOME PLAN, and MOVIE PLAN.
# 
# Here's the `function.py` file:

# function.py

from home.home_plan import home_plan, get_room, get_all_actuators, get_all_sensors
from home.config import LIGHT_INTENSITY_LOW

def morning_plan(home):
    print("Executing Morning Plan...")
    
    living_room = get_room(home, "LivingRoom")
    bedroom = get_room(home, "Bedroom")
    kitchen = get_room(home, "Kitchen")
    
    # Open curtains
    bedroom_curtains = [actuator for actuator in bedroom.actuators if actuator.actuator_type == "Curtain"]
    for curtain in bedroom_curtains:
        curtain.turn_on()
    
    # Start coffee machine
    kitchen_coffee_machines = [actuator for actuator in kitchen.actuators if actuator.actuator_type == "CoffeeMachine"]
    for coffee_machine in kitchen_coffee_machines:
        coffee_machine.turn_on()
        coffee_machine.make_coffee("espresso")
    
    # Check light intensity and turn on lights if needed
    light_sensors = get_all_sensors(home, "LightIntensive")
    for sensor in light_sensors:
        sensor.turn_on()
        reading = sensor.get_reading()
        if reading is not None and reading < LIGHT_INTENSITY_LOW:
            lights = get_all_actuators(home, "Light")
            for light in lights:
                light.turn_on()
                light.set_brightness_level("medium")


def leave_home_plan(home):
    print("Executing Leave Home Plan...")
    
    # Lock doors
    doors = get_all_actuators(home, "Door")
    for door in doors:
        door.lock()
    
    # Turn off lights
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_off()
    
    # Turn off all smart sockets
    smart_sockets = get_all_actuators(home, "SmartSocket")
    for socket in smart_sockets:
        socket.turn_off()


def movie_plan(home):
    print("Executing Movie Plan...")
    
    living_room = get_room(home, "LivingRoom")
    
    # Close curtains
    living_room_curtains = [actuator for actuator in living_room.actuators if actuator.actuator_type == "Curtain"]
    for curtain in living_room_curtains:
        curtain.turn_on()
    
    # Dim lights
    living_room_lights = [actuator for actuator in living_room.actuators if actuator.actuator_type == "Light"]
    for light in living_room_lights:
        light.turn_on()
        light.set_brightness_level("low")
    
    # Turn on TV and play movie
    tvs = [actuator for actuator in living_room.actuators if actuator.actuator_type == "SmartTV"]
    for tv in tvs:
        tv.turn_on()
        tv.play_channel("Movie Channel")


def main():
    # Create home setup
    home = home_plan()
    
    # Execute plans
    morning_plan(home)
    leave_home_plan(home)
    movie_plan(home)


if __name__ == "__main__":
    main()