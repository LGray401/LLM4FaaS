# Here is the 'function.py' file for your smart home project:

from home.home_plan import home_plan, get_room_sensors, get_room_actuators, print_home_plan
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    # Create home plan
    home = home_plan()

    # Print home plan
    # print_home_plan(home)

    # Get bedroom sensors
    bedroom_sensors = get_room_sensors(home, "Bedroom")

    # Get bedroom actuators
    bedroom_actuators = get_room_actuators(home, "Bedroom")

    # Check and control temperature and window status in the bedroom
    check_temperature(bedroom_sensors, bedroom_actuators)
    check_humidity(bedroom_sensors, bedroom_actuators)
    check_outdoor_temperature(bedroom_sensors, bedroom_actuators)

def check_temperature(sensors, actuators):
    indoor_temp_sensor = None
    for sensor in sensors:
        if sensor.sensor_type == "IndoorTemperature":
            indoor_temp_sensor = sensor
            break

    if indoor_temp_sensor is None:
        print("No indoor temperature sensor found in the room.")
        return

    indoor_temp_sensor.turn_on()
    current_temperature = indoor_temp_sensor.get_reading()

    if current_temperature is None:
        print("Cannot get current temperature reading.")
        return

    if current_temperature > TEMP_HIGH:
        for actuator in actuators:
            if actuator.actuator_type == "Window":
                actuator.open()

    elif current_temperature < TEMP_LOW:
        for actuator in actuators:
            if actuator.actuator_type == "Window":
                actuator.close()

def check_humidity(sensors, actuators):
    humidity_sensor = None
    for sensor in sensors:
        if sensor.sensor_type == "Humidity":
            humidity_sensor = sensor
            break

    if humidity_sensor is None:
        print("No humidity sensor found in the room.")
        return

    humidity_sensor.turn_on()
    current_humidity = humidity_sensor.get_reading()

    if current_humidity is None:
        print("Cannot get current humidity reading.")
        return

    if current_humidity > HUMIDITY_HIGH:
        for actuator in actuators:
            if actuator.actuator_type == "Humidifier":
                actuator.decrease_humidity()

    elif current_humidity < HUMIDITY_LOW:
        for actuator in actuators:
            if actuator.actuator_type == "Humidifier":
                actuator.increase_humidity()

def check_outdoor_temperature(sensors, actuators):
    outdoor_temp_sensor = None
    for sensor in sensors:
        if sensor.sensor_type == "OutdoorTemperature":
            outdoor_temp_sensor = sensor
            break

    if outdoor_temp_sensor is None:
        print("No outdoor temperature sensor found in the room.")
        return

    outdoor_temp_sensor.turn_on()
    current_outdoor_temperature = outdoor_temp_sensor.get_reading()

    if current_outdoor_temperature is None:
        print("Cannot get current outdoor temperature reading.")
        return

    indoor_temp_sensor = None
    for sensor in sensors:
        if sensor.sensor_type == "IndoorTemperature":
            indoor_temp_sensor = sensor
            break

    if indoor_temp_sensor is None:
        print("No indoor temperature sensor found in the room.")
        return

    indoor_temp_sensor.turn_on()
    current_indoor_temperature = indoor_temp_sensor.get_reading()

    if current_indoor_temperature is None:
        print("Cannot get current indoor temperature reading.")
        return

    if current_indoor_temperature > TEMP_HIGH and current_outdoor_temperature < TEMP_LOW:
        for actuator in actuators:
            if actuator.actuator_type == "Window":
                actuator.open()

if __name__ == "__main__":
    main()