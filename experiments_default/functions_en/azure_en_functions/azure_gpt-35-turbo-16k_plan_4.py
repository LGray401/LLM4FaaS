# Here is the 'function.py' file based on your functional description and the provided source code:

from home.home_plan import *
from home.config import *

def main():
    home = home_plan()

    # MORNING PLAN
    living_room = get_room(home, "LivingRoom")
    curtain = get_room_actuators(home, "LivingRoom")[4]
    curtain.turn_on()

    # LEAVE HOME PLAN
    living_room = get_room(home, "LivingRoom")
    lamp = get_room_actuators(home, "LivingRoom")[1]
    lamp.turn_on()

    # MOVIE PLAN
    living_room = get_room(home, "LivingRoom")
    light = get_room_actuators(home, "LivingRoom")[1]
    light.set_brightness_level("low")

if __name__ == "__main__":
    main()