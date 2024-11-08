# Sure, I will create a 'function.py' file for your smart home project based on the given functional description and the provided source code.
# 
# Here is the 'function.py' file:

from home.home_plan import home_plan, get_room_actuators, get_room_sensors, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH


def get_temperature(room_name):
    sensors = get_room_sensors(home, room_name)
    for sensor in sensors:
        if sensor.sensor_type == "IndoorTemperature":
            return sensor.get_reading()
    return None


def get_humidity(room_name):
    sensors = get_room_sensors(home, room_name)
    for sensor in sensors:
        if sensor.sensor_type == "Humidity":
            return sensor.get_reading()
    return None


def get_light_intensity(room_name):
    sensors = get_room_sensors(home, room_name)
    for sensor in sensors:
        if sensor.sensor_type == "LightIntensive":
            return sensor.get_reading()
    return None


def set_target_temperature(room_name, temperature):
    actuators = get_room_actuators(home, room_name)
    for actuator in actuators:
        if actuator.actuator_type == "Heater" or actuator.actuator_type == "AC":
            actuator.set_target_temperature(temperature)


def set_light_brightness(room_name, brightness_level):
    actuators = get_room_actuators(home, room_name)
    for actuator in actuators:
        if actuator.actuator_type == "Light":
            actuator.set_brightness_level(brightness_level)


def get_temperature_sensors():
    return get_all_sensors(home, "IndoorTemperature")


def get_humidity_sensors():
    return get_all_sensors(home, "Humidity")


def get_light_intensity_sensors():
    return get_all_sensors(home, "LightIntensive")


def get_light_actuators():
    return get_all_actuators(home, "Light")


def get_door_actuators():
    return get_all_actuators(home, "Door")


def get_window_actuators():
    return get_all_actuators(home, "Window")


def get_curtain_actuators():
    return get_all_actuators(home, "Curtain")


def main():
    # Create home plan
    home = home_plan()

    # Example usage
    temperature = get_temperature("LivingRoom")
    print(f"Temperature in the LivingRoom: {temperature}°C")

    humidity = get_humidity("LivingRoom")
    print(f"Humidity in the LivingRoom: {humidity}%")

    light_intensity = get_light_intensity("LivingRoom")
    print(f"Light intensity in the LivingRoom: {light_intensity} lux")

    set_target_temperature("Bedroom", 20)

    set_light_brightness("LivingRoom", "medium")


if __name__ == "__main__":
    main()