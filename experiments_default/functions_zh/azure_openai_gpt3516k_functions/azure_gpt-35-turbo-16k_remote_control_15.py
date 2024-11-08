# Sure, I can help you with that. Here is the 'function.py' file based on the given functional description:

from home.home_plan import home_plan, print_home_plan, get_room_sensors, get_all_sensors, get_all_actuators
from home.logger_config import logger
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    # Get the home plan
    home = home_plan()

    # Print the home plan
    print_home_plan(home)

    # Get all temperature sensors
    temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    for sensor in temperature_sensors:
        temperature = sensor.get_reading()
        if temperature is not None:
            if temperature < TEMP_LOW:
                logger.warning(f"Temperature is too low in {sensor.room_name}!")
            elif temperature > TEMP_HIGH:
                logger.warning(f"Temperature is too high in {sensor.room_name}!")

    # Get all humidity sensors
    humidity_sensors = get_all_sensors(home, "Humidity")
    for sensor in humidity_sensors:
        humidity = sensor.get_reading()
        if humidity is not None:
            if humidity < HUMIDITY_LOW:
                logger.warning(f"Humidity is too low in {sensor.room_name}!")
            elif humidity > HUMIDITY_HIGH:
                logger.warning(f"Humidity is too high in {sensor.room_name}!")

    # Get all light intensity sensors
    light_intensity_sensors = get_all_sensors(home, "LightIntensive")
    for sensor in light_intensity_sensors:
        light_intensity = sensor.get_reading()
        if light_intensity is not None:
            if light_intensity < LIGHT_INTENSITY_LOW:
                logger.warning(f"Light intensity is too low in {sensor.room_name}!")
            elif light_intensity > LIGHT_INTENSITY_HIGH:
                logger.warning(f"Light intensity is too high in {sensor.room_name}!")

    # Get all actuators and perform actions
    actuators = get_all_actuators(home, None)
    for actuator in actuators:
        actuator.turn_on()
        actuator.get_status()

if __name__ == '__main__':
    main()