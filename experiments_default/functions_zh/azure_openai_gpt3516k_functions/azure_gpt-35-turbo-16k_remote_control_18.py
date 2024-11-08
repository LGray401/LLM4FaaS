# I have created the 'function.py' file for your smart home project based on the functional description and the provided source code. Here is the code:

from home.home_plan import home_plan, get_room_actuators
from home.actuator import Light

def open_light(room_name):
    home = home_plan()
    actuators = get_room_actuators(home, room_name)
    if actuators is None:
        return
    
    for actuator in actuators:
        if isinstance(actuator, Light):
            actuator.turn_on()
            break

if __name__ == "__main__":
    room_name = "LivingRoom"
    open_light(room_name)