# Here is the 'function.py' file based on the given functional description and the provided source code files:

from home.home_plan import home_plan, print_home_plan, get_room, get_room_sensors, get_room_actuators, \
    get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    # Create a home plan
    home = home_plan()

    # Print the home plan
    print_home_plan(home)

    # Get a specific room
    living_room = get_room(home, "LivingRoom")

    # Get the sensors in the living room
    living_room_sensors = get_room_sensors(home, "LivingRoom")

    # Get the actuators in the living room
    living_room_actuators = get_room_actuators(home, "LivingRoom")

    # Get all the temperature sensors in the home
    temperature_sensors = get_all_sensors(home, "IndoorTemperature")

    # Get all the light actuators in the home
    light_actuators = get_all_actuators(home, "Light")

    # Perform temperature control based on the readings
    for sensor in temperature_sensors:
        reading = sensor.get_reading()
        if reading is not None:
            if reading < TEMP_LOW:
                for actuator in light_actuators:
                    actuator.turn_off()
            elif reading > TEMP_HIGH:
                for actuator in light_actuators:
                    actuator.turn_on()

    # Perform humidity control based on the readings
    for room in home:
        for sensor in room.sensors:
            if isinstance(sensor, HumiditySensor):
                reading = sensor.get_reading()
                if reading is not None:
                    if reading < HUMIDITY_LOW:
                        for actuator in room.actuators:
                            if isinstance(actuator, Humidifier):
                                actuator.increase_humidity()
                    elif reading > HUMIDITY_HIGH:
                        for actuator in room.actuators:
                            if isinstance(actuator, Humidifier):
                                actuator.decrease_humidity()

    # Perform light intensity control based on the readings
    for room in home:
        for sensor in room.sensors:
            if isinstance(sensor, LightIntensiveSensor):
                reading = sensor.get_reading()
                if reading is not None:
                    if reading < LIGHT_INTENSITY_LOW:
                        for actuator in room.actuators:
                            if isinstance(actuator, Light):
                                actuator.set_brightness_level("high")
                    elif reading > LIGHT_INTENSITY_HIGH:
                        for actuator in room.actuators:
                            if isinstance(actuator, Light):
                                actuator.set_brightness_level("low")


if __name__ == "__main__":
    main()