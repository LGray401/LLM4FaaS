# Sure! Here is the `function.py` file that you requested:

from home.home_plan import home_plan, get_room_actuators

def open_windows(room_name):
    home = home_plan()
    actuators = get_room_actuators(home, room_name)
    if actuators is not None:
        for actuator in actuators:
            if actuator.actuator_type == "Window":
                actuator.turn_on()
    else:
        print(f"No actuators found in {room_name}")

if __name__ == "__main__":
    open_windows("LivingRoom")