# Sure! Here is the 'function.py' file based on your functional description:

from home.home_plan import get_all_actuators


def open_window(home):
    actuators = get_all_actuators(home, "Window")

    # Open all the windows
    for actuator in actuators:
        actuator.turn_on()

