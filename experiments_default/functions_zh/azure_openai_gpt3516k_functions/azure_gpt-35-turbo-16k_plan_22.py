# Sure! Here is the 'function.py' file that you requested:

from home.home_plan import home_plan, get_room_actuators, get_room_sensors, get_all_sensors, get_all_actuators
from home.actuator import Light


def main():
    # Get the home plan
    home = home_plan()

    # Example usage
    # Get all sensors of a specific type in a specific room
    living_room_sensors = get_room_sensors(home, "LivingRoom")
    if living_room_sensors is not None:
        for sensor in living_room_sensors:
            print(sensor.id)

    # Get all actuators of a specific type in a specific room
    bedroom_actuators = get_room_actuators(home, "Bedroom")
    if bedroom_actuators is not None:
        for actuator in bedroom_actuators:
            print(actuator.id)

    # Get all sensors of a specific type in the entire home
    indoor_temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    for sensor in indoor_temperature_sensors:
        print(sensor.id)

    # Get all actuators of a specific type in the entire home
    light_actuators = get_all_actuators(home, "Light")
    for actuator in light_actuators:
        print(actuator.id)

    # Example control
    # Turn on the lights in the living room
    for actuator in light_actuators:
        if actuator.room_name == "LivingRoom":
            actuator.turn_on()

    # Example control
    # Set the brightness level of the lights in the bedroom to "low"
    for actuator in light_actuators:
        if actuator.room_name == "Bedroom":
            if isinstance(actuator, Light):
                actuator.set_brightness_level("low")


if __name__ == "__main__":
    main()