# Sure, here is the `function.py` file based on the given functional description and the provided source code:

from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators
from home.actuator import Light

def main():
    # Define the home plan
    home = home_plan()

    # Print the home plan
    print_home_plan(home)

    # Get a specific room
    room = get_room(home, "LivingRoom")

    # Get the sensors in a specific room
    sensors = get_room_sensors(home, "LivingRoom")
    print(sensors)

    # Get the actuators in a specific room
    actuators = get_room_actuators(home, "LivingRoom")
    print(actuators)

    # Get all sensors of a specific type
    temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    print(temperature_sensors)

    # Get all actuators of a specific type
    light_actuators = get_all_actuators(home, "Light")
    print(light_actuators)

    # Example usage: Turn on the lights in the living room
    for actuator in light_actuators:
        actuator.turn_on()

if __name__ == "__main__":
    main()