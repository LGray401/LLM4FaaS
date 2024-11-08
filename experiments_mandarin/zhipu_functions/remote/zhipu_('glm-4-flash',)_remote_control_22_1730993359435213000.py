# Based on the functional description and the source code you provided, here is a `function.py` file that should be placed in the `functions` folder and contain the `main` function for your smart home project:

# function.py

from home.sensor import Sensor
from home.actuator import Actuator
from home_plan import home_plan

def main():
    # Get the home plan
    home = home_plan()

    # Turn on the lights in the living room, bedroom, and bathroom
    living_room_lights = get_room_actuators(home, "LivingRoom")
    bedroom_lights = get_room_actuators(home, "Bedroom")
    bathroom_lights = get_room_actuators(home, "Bathroom")

    for light in living_room_lights + bedroom_lights + bathroom_lights:
        if isinstance(light, Actuator) and light.actuator_type == "Light":
            light.turn_on()

    # Turn on the AC in the living room and bedroom
    living_room_ac = get_room_actuators(home, "LivingRoom")
    bedroom_ac = get_room_actuators(home, "Bedroom")

    for ac in living_room_ac + bedroom_ac:
        if isinstance(ac, Actuator) and ac.actuator_type == "AC":
            ac.turn_on()

    # Turn on the heater in the bathroom
    bathroom_heater = get_room_actuators(home, "Bathroom")
    for heater in bathroom_heater:
        if isinstance(heater, Actuator) and heater.actuator_type == "Heater":
            heater.turn_on()

    # Turn on the TV in the living room
    living_room_tv = get_room_actuators(home, "LivingRoom")
    for tv in living_room_tv:
        if isinstance(tv, Actuator) and tv.actuator_type == "SmartTV":
            tv.turn_on()

def get_room_actuators(home, room_name):
    for room in home:
        if room.name == room_name:
            return room.actuators
    return []

if __name__ == "__main__":
    main()