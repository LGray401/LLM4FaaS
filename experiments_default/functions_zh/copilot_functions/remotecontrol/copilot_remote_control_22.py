# Based on the functional description and the provided source code, it seems like you want to create a `function.py` file that controls various devices in a smart home. The function should be able to turn on the lights in the living room, bedroom, and bathroom, turn on the air conditioning in the living room and bedroom, turn on the heating in the bathroom, and turn on the TV in the living room.
#
# Here is a Python function that should meet your requirements:
#
# ```python
# function.py
from home.actuator import Light, AC, Heater, SmartTV
from home.home_plan import get_room, get_all_actuators

def control_devices(home):
    # Get all the lights in the home
    all_lights = get_all_actuators(home, "Light")
    # Get all the ACs in the home
    all_acs = get_all_actuators(home, "AC")
    # Get all the heaters in the home
    all_heaters = get_all_actuators(home, "Heater")
    # Get all the TVs in the home
    all_tvs = get_all_actuators(home, "SmartTV")

    # Define the rooms where we want to turn on the lights
    rooms_with_lights_on = ["LivingRoom", "Bedroom", "Bathroom"]
    # Define the rooms where we want to turn on the AC
    rooms_with_ac_on = ["LivingRoom", "Bedroom"]
    # Define the rooms where we want to turn on the heater
    rooms_with_heater_on = ["Bathroom"]
    # Define the rooms where we want to turn on the TV
    rooms_with_tv_on = ["LivingRoom"]

    # Turn on the lights in the specified rooms
    for light in all_lights:
        if light.room_name in rooms_with_lights_on:
            light.turn_on()

    # Turn on the AC in the specified rooms
    for ac in all_acs:
        if ac.room_name in rooms_with_ac_on:
            ac.turn_on()

    # Turn on the heater in the specified rooms
    for heater in all_heaters:
        if heater.room_name in rooms_with_heater_on:
            heater.turn_on()

    # Turn on the TV in the specified rooms
    for tv in all_tvs:
        if tv.room_name in rooms_with_tv_on:
            tv.turn_on()
# ```
#
# This function takes in a `home` object, which is a list of `Room` objects. Each `Room` object contains a list of `Sensor` and `Actuator` objects. The function iterates over all the `Actuator` objects in the home, and if the `Actuator` is in a specified room, it turns it on.
#
# You can call this function in your main program after you have created your `home` object. For example:
#
# ```python
from home.home_plan import home_plan
# from functions.function import control_devices

home = home_plan()
control_devices(home)
# ```
#
# This will turn on the specified devices in the specified rooms.