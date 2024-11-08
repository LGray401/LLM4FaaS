# Sure, here is the 'function.py' file based on the given functional description and the provided source code:

from home.home_plan import home_plan, print_home_plan, get_room_sensors, get_room_actuators
from home.sensor import LightIntensiveSensor
from home.actuator import Light

def main():
    # Create the home plan
    home = home_plan()

    # Print the home plan
    print_home_plan(home)

    # Get the sensors and actuators in the living room
    living_room_sensors = get_room_sensors(home, "LivingRoom")
    living_room_actuators = get_room_actuators(home, "LivingRoom")

    # Turn on the lights in the living room
    for sensor in living_room_sensors:
        if isinstance(sensor, LightIntensiveSensor):
            sensor.turn_on()

    for actuator in living_room_actuators:
        if isinstance(actuator, Light):
            actuator.turn_on()

if __name__ == "__main__":
    main()