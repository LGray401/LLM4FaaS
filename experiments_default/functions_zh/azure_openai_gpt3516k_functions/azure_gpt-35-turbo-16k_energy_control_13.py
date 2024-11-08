# Sure! I have created the 'function.py' file for your smart home project based on the given functional description and the provided source code. Here is the content of the 'function.py' file:

import time
from home.home_plan import home_plan, print_home_plan, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger


def auto_power_off_lights(home):
    print("Checking if lights can be automatically turned off...")
    logger.info("Checking if lights can be automatically turned off...")

    all_light_sensors = get_all_sensors(home, "LightIntensive")
    if len(all_light_sensors) == 0:
        print("No light sensors found. Cannot determine light intensity.")
        logger.warning("No light sensors found. Cannot determine light intensity.")
        return

    for light_sensor in all_light_sensors:
        light_reading = light_sensor.get_reading()
        if light_reading is not None and light_reading < LIGHT_INTENSITY_LOW:
            room_name = light_sensor.room_name
            room_lights = get_room_actuators(home, room_name)
            if room_lights is not None:
                for light in room_lights:
                    light.turn_off()

    print("Lights auto power off check complete.")
    logger.info("Lights auto power off check complete.")


def auto_power_off_sockets(home):
    print("Checking if sockets can be automatically turned off...")
    logger.info("Checking if sockets can be automatically turned off...")

    all_humidity_sensors = get_all_sensors(home, "Humidity")
    if len(all_humidity_sensors) == 0:
        print("No humidity sensors found. Cannot determine humidity level.")
        logger.warning("No humidity sensors found. Cannot determine humidity level.")
        return

    for humidity_sensor in all_humidity_sensors:
        humidity_reading = humidity_sensor.get_reading()
        if humidity_reading is not None and humidity_reading < HUMIDITY_LOW:
            room_name = humidity_sensor.room_name
            room_sockets = get_room_actuators(home, room_name)
            if room_sockets is not None:
                for socket in room_sockets:
                    socket.turn_off()

    print("Sockets auto power off check complete.")
    logger.info("Sockets auto power off check complete.")


def auto_adjust_temperature(home):
    print("Checking if temperature can be automatically adjusted...")
    logger.info("Checking if temperature can be automatically adjusted...")

    all_temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    if len(all_temperature_sensors) == 0:
        print("No temperature sensors found. Cannot determine indoor temperature.")
        logger.warning("No temperature sensors found. Cannot determine indoor temperature.")
        return

    for temperature_sensor in all_temperature_sensors:
        temperature_reading = temperature_sensor.get_reading()
        if temperature_reading is not None:
            room_name = temperature_sensor.room_name
            room_heaters = get_room_actuators(home, room_name)
            room_acs = get_room_actuators(home, room_name)
            if room_heaters is not None and room_acs is not None:
                for heater in room_heaters:
                    heater.adjust_temperature(temperature_reading)
                for ac in room_acs:
                    ac.adjust_temperature(temperature_reading)

    print("Temperature auto adjustment check complete.")
    logger.info("Temperature auto adjustment check complete.")


def auto_adjust_humidity(home):
    print("Checking if humidity can be automatically adjusted...")
    logger.info("Checking if humidity can be automatically adjusted...")

    all_humidity_sensors = get_all_sensors(home, "Humidity")
    if len(all_humidity_sensors) == 0:
        print("No humidity sensors found. Cannot determine humidity level.")
        logger.warning("No humidity sensors found. Cannot determine humidity level.")
        return

    for humidity_sensor in all_humidity_sensors:
        humidity_reading = humidity_sensor.get_reading()
        if humidity_reading is not None:
            room_name = humidity_sensor.room_name
            room_humidifiers = get_room_actuators(home, room_name)
            if room_humidifiers is not None:
                for humidifier in room_humidifiers:
                    if humidity_reading > HUMIDITY_HIGH:
                        humidifier.decrease_humidity()
                    elif humidity_reading < HUMIDITY_LOW:
                        humidifier.increase_humidity()

    print("Humidity auto adjustment check complete.")
    logger.info("Humidity auto adjustment check complete.")


def auto_adjust_lighting(home):
    print("Checking if lighting can be automatically adjusted...")
    logger.info("Checking if lighting can be automatically adjusted...")

    all_light_sensors = get_all_sensors(home, "LightIntensive")
    if len(all_light_sensors) == 0:
        print("No light sensors found. Cannot determine light intensity.")
        logger.warning("No light sensors found. Cannot determine light intensity.")
        return

    for light_sensor in all_light_sensors:
        light_reading = light_sensor.get_reading()
        if light_reading is not None:
            room_name = light_sensor.room_name
            room_lights = get_room_actuators(home, room_name)
            if room_lights is not None:
                for light in room_lights:
                    if light_reading > LIGHT_INTENSITY_HIGH:
                        light.set_brightness_level("high")
                    elif light_reading < LIGHT_INTENSITY_LOW:
                        light.set_brightness_level("low")

    print("Lighting auto adjustment check complete.")
    logger.info("Lighting auto adjustment check complete.")


def auto_adjust_air_quality(home, room_name):
    print(f"Checking if air quality in {room_name} can be automatically adjusted...")
    logger.info(f"Checking if air quality in {room_name} can be automatically adjusted...")

    all_smoke_sensors = get_all_sensors(home, "Smoke")
    if len(all_smoke_sensors) == 0:
        print("No smoke sensors found. Cannot determine air quality.")
        logger.warning("No smoke sensors found. Cannot determine air quality.")
        return

    room_smoke_sensors = []
    for smoke_sensor in all_smoke_sensors:
        if smoke_sensor.room_name == room_name:
            room_smoke_sensors.append(smoke_sensor)

    if len(room_smoke_sensors) == 0:
        print(f"No smoke sensors found in {room_name}. Cannot determine air quality.")
        logger.warning(f"No smoke sensors found in {room_name}. Cannot determine air quality.")
        return

    for smoke_sensor in room_smoke_sensors:
        smoke_reading = smoke_sensor.get_reading()
        if smoke_reading is not None:
            room_actuators = get_room_actuators(home, room_name)
            if room_actuators is not None:
                for actuator in room_actuators:
                    if smoke_reading > 50:
                        actuator.turn_off()

    print(f"Air quality auto adjustment check in {room_name} complete.")
    logger.info(f"Air quality auto adjustment check in {room_name} complete.")


def auto_adjust_temperature_and_humidity(home):
    print("Checking if temperature and humidity can be automatically adjusted together...")
    logger.info("Checking if temperature and humidity can be automatically adjusted together...")

    all_temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    all_humidity_sensors = get_all_sensors(home, "Humidity")

    common_room_names = []

    if len(all_temperature_sensors) == 0:
        print("No temperature sensors found. Cannot determine indoor temperature.")
        logger.warning("No temperature sensors found. Cannot determine indoor temperature.")
    if len(all_humidity_sensors) == 0:
        print("No humidity sensors found. Cannot determine humidity level.")
        logger.warning("No humidity sensors found. Cannot determine humidity level.")

    for temperature_sensor in all_temperature_sensors:
        for humidity_sensor in all_humidity_sensors:
            if temperature_sensor.room_name == humidity_sensor.room_name:
                common_room_names.append(temperature_sensor.room_name)

    for room_name in common_room_names:
        room_temperature_sensors = []
        room_humidity_sensors = []
        for temperature_sensor in all_temperature_sensors:
            if temperature_sensor.room_name == room_name:
                room_temperature_sensors.append(temperature_sensor)
        for humidity_sensor in all_humidity_sensors:
            if humidity_sensor.room_name == room_name:
                room_humidity_sensors.append(humidity_sensor)

        room_heaters = get_room_actuators(home, room_name)
        room_acs = get_room_actuators(home, room_name)

        if room_heaters is not None and room_acs is not None:
            for temperature_sensor, humidity_sensor in zip(room_temperature_sensors, room_humidity_sensors):
                temperature_reading = temperature_sensor.get_reading()
                humidity_reading = humidity_sensor.get_reading()

                if temperature_reading is not None and humidity_reading is not None:
                    for heater in room_heaters:
                        if temperature_reading < TEMP_LOW:
                            heater.turn_on()
                        elif temperature_reading > TEMP_HIGH:
                            heater.turn_off()

                    for ac in room_acs:
                        if humidity_reading > HUMIDITY_HIGH:
                            ac.turn_on()
                        elif humidity_reading < HUMIDITY_LOW:
                            ac.turn_off()

    print("Temperature and Humidity auto adjustment check complete.")
    logger.info("Temperature and Humidity auto adjustment check complete.")


def main():
    logger.info("Starting Smart Home")

    # Create home plan
    home = home_plan()

    # Print home plan
    # print_home_plan(home)

    print("Starting Auto Power Off Lights")
    logger.info("Starting Auto Power Off Lights")
    auto_power_off_lights(home)

    print("Starting Auto Power Off Sockets")
    logger.info("Starting Auto Power Off Sockets")
    auto_power_off_sockets(home)

    print("Starting Auto Adjust Temperature")
    logger.info("Starting Auto Adjust Temperature")
    auto_adjust_temperature(home)

    print("Starting Auto Adjust Humidity")
    logger.info("Starting Auto Adjust Humidity")
    auto_adjust_humidity(home)

    print("Starting Auto Adjust Lighting")
    logger.info("Starting Auto Adjust Lighting")
    auto_adjust_lighting(home)

    print("Starting Auto Adjust Air Quality")
    logger.info("Starting Auto Adjust Air Quality")
    auto_adjust_air_quality(home, "Kitchen")

    print("Starting Auto Adjust Temperature and Humidity")
    logger.info("Starting Auto Adjust Temperature and Humidity")
    auto_adjust_temperature_and_humidity(home)

    logger.info("Smart Home Execution Completed")


if __name__ == "__main__":
    main()