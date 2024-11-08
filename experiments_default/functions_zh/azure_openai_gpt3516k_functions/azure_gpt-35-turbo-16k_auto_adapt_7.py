# Sure, here is the 'function.py' file based on the given functional description and the provided source code:

from home.home_plan import home_plan, print_home_plan, get_room, get_room_sensors, get_room_actuators, \
    get_all_sensors, get_all_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Light


def check_temperature():
    home = home_plan()
    sensors = get_all_sensors(home, "IndoorTemperature")
    for sensor in sensors:
        reading = sensor.get_reading()
        if reading:
            if reading > zTEMP_HIGH:
                print(f"Room {sensor.room_name} is too hot!")
            elif reading < TEMP_LOW:
                print(f"Room {sensor.room_name} is too cold!")


def check_humidity():
    home = home_plan()
    sensors = get_all_sensors(home, "Humidity")
    for sensor in sensors:
        reading = sensor.get_reading()
        if reading:
            if reading > HUMIDITY_HIGH:
                print(f"Room {sensor.room_name} is too humid!")
            elif reading < HUMIDITY_LOW:
                print(f"Room {sensor.room_name} is too dry!")


def check_light_intensity():
    home = home_plan()
    sensors = get_all_sensors(home, "LightIntensive")
    for sensor in sensors:
        reading = sensor.get_reading()
        if reading:
            if reading < LIGHT_INTENSITY_LOW:
                print(f"Room {sensor.room_name} is too dark!")


def turn_on_lights():
    home = home_plan()
    actuators = get_all_actuators(home, "Light")
    for actuator in actuators:
        actuator.turn_on()


def main():
    check_temperature()
    check_humidity()
    check_light_intensity()
    turn_on_lights()


if __name__ == "__main__":
    main()