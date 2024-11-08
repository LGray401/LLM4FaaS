# Here is the requested 'function.py' file based on your functional description:

from home.sensor import LightIntensiveSensor
from home.actuator import Light, SmartTV

def morning_plan(home):
    living_room = get_room(home, "LivingRoom")
    bedroom = get_room(home, "Bedroom")
    kitchen = get_room(home, "Kitchen")
    bathroom = get_room(home, "Bathroom")

    # Turn on lights in living room, bedroom, and kitchen
    living_room_lights = get_room_actuators(home, "LivingRoom")
    for light in living_room_lights:
        if isinstance(light, Light):
            light.turn_on()

    bedroom_lights = get_room_actuators(home, "Bedroom")
    for light in bedroom_lights:
        if isinstance(light, Light):
            light.turn_on()

    kitchen_lights = get_room_actuators(home, "Kitchen")
    for light in kitchen_lights:
        if isinstance(light, Light):
            light.turn_on()

    # Turn on the TV in the living room
    living_room_tv = get_room_actuators(home, "LivingRoom")
    for tv in living_room_tv:
        if isinstance(tv, SmartTV):
            tv.turn_on()

def leave_home_plan(home):
    living_room = get_room(home, "LivingRoom")
    bedroom = get_room(home, "Bedroom")
    kitchen = get_room(home, "Kitchen")
    bathroom = get_room(home, "Bathroom")

    # Turn off lights in living room, bedroom, and kitchen
    living_room_lights = get_room_actuators(home, "LivingRoom")
    for light in living_room_lights:
        if isinstance(light, Light):
            light.turn_off()

    bedroom_lights = get_room_actuators(home, "Bedroom")
    for light in bedroom_lights:
        if isinstance(light, Light):
            light.turn_off()

    kitchen_lights = get_room_actuators(home, "Kitchen")
    for light in kitchen_lights:
        if isinstance(light, Light):
            light.turn_off()

def movie_plan(home):
    living_room = get_room(home, "LivingRoom")

    # Turn on the TV in the living room
    living_room_tv = get_room_actuators(home, "LivingRoom")
    for tv in living_room_tv:
        if isinstance(tv, SmartTV):
            tv.turn_on()

    # Turn off lights in living room
    living_room_lights = get_room_actuators(home, "LivingRoom")
    for light in living_room_lights:
        if isinstance(light, Light):
            light.turn_off()

# Example usage
home = home_plan()
morning_plan(home)
leave_home_plan(home)
movie_plan(home)