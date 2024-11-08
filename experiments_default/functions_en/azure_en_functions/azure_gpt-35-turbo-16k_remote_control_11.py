# Sure! Here is the 'function.py' file based on the given functional description and the provided source code:

from home.home_plan import home_plan, get_room_actuators, get_room_sensors, get_all_sensors, get_all_actuators

def sleep_mode():
    home = home_plan()
    for room in home:
        actuators = get_room_actuators(home, room.name)
        for actuator in actuators:
            actuator.turn_off()

def wake_up_mode():
    home = home_plan()
    for room in home:
        actuators = get_room_actuators(home, room.name)
        for actuator in actuators:
            actuator.turn_on()

def lights_off_mode():
    home = home_plan()
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_off()

def window_closing_mode():
    home = home_plan()
    windows = get_all_actuators(home, "Window")
    for window in windows:
        window.turn_off()

if __name__ == "__main__":
    sleep_mode()
    wake_up_mode()
    lights_off_mode()
    window_closing_mode()