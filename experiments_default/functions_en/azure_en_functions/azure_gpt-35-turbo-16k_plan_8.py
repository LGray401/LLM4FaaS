# Here is the 'function.py' file based on your functional description and the provided source code:

from home.home_plan import home_plan, get_room_sensors, get_room_actuators, print_home_plan
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Light, Window, Curtain, SmartTV

def main():
    # Create home plan
    home = home_plan()

    # Print home plan
    print_home_plan(home)

    # Get sensors and actuators for the desired room
    living_room_sensors = get_room_sensors(home, "LivingRoom")
    living_room_actuators = get_room_actuators(home, "LivingRoom")

    # Perform morning plan
    morning_plan(living_room_sensors, living_room_actuators)

    # Perform leave home plan
    leave_home_plan(living_room_actuators)

    # Perform movie plan
    movie_plan(living_room_actuators)

def morning_plan(sensors, actuators):
    print("\nMORNING PLAN: I woke up, please make our home work")

    # Turn on lights in the living room
    light = get_actuator(actuators, "Light")
    if light is not None:
        light.turn_on()

    # Open curtains in the living room
    curtain = get_actuator(actuators, "Curtain")
    if curtain is not None:
        curtain.open()

    # Turn on the TV in the living room
    tv = get_actuator(actuators, "SmartTV")
    if tv is not None:
        tv.turn_on()

def leave_home_plan(actuators):
    print("\nLEAVE HOME PLAN: I'm out, protect the house")

    # Close windows in the living room
    window = get_actuator(actuators, "Window")
    if window is not None:
        window.close()

    # Close curtains in the living room
    curtain = get_actuator(actuators, "Curtain")
    if curtain is not None:
        curtain.close()

    # Turn off lights in the living room
    light = get_actuator(actuators, "Light")
    if light is not None:
        light.turn_off()

    # Turn off the TV in the living room
    tv = get_actuator(actuators, "SmartTV")
    if tv is not None:
        tv.turn_off()

def movie_plan(actuators):
    print("\nMOVIE PLAN: Turn on the TV and turn off the lights")

    # Turn on the TV in the living room
    tv = get_actuator(actuators, "SmartTV")
    if tv is not None:
        tv.turn_on()

    # Turn off lights in the living room
    light = get_actuator(actuators, "Light")
    if light is not None:
        light.turn_off()

def get_actuator(actuators, actuator_type):
    for actuator in actuators:
        if actuator.actuator_type == actuator_type:
            return actuator
    return None

if __name__ == "__main__":
    main()