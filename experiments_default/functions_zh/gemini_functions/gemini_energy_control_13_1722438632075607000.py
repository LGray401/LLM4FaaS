from home.home_plan import home_plan, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, \
    TEMP_CHANGE_DURATION_WINDOW
from home.logger_config import logger


def turn_on_light_if_dark(home, room_name):
    light_sensors = get_room_sensors(home, room_name)
    lights = get_room_actuators(home, room_name, "Light")

    for light_sensor in light_sensors:
        if light_sensor.sensor_type == "LightIntensive":
            reading = light_sensor.get_reading()
            if reading is not None and reading < LIGHT_INTENSITY_LOW:
                print(f"It's dark in {room_name}, turn on the light.")
                logger.info(f"It's dark in {room_name}, turn on the light.")
                for light in lights:
                    if light.status == "off":
                        light.turn_on()
                        break


def turn_off_light_if_bright(home, room_name):
    light_sensors = get_room_sensors(home, room_name)
    lights = get_room_actuators(home, room_name, "Light")

    for light_sensor in light_sensors:
        if light_sensor.sensor_type == "LightIntensive":
            reading = light_sensor.get_reading()
            if reading is not None and reading > LIGHT_INTENSITY_HIGH:
                print(f"It's bright in {room_name}, turn off the light.")
                logger.info(f"It's bright in {room_name}, turn off the light.")
                for light in lights:
                    if light.status == "on":
                        light.turn_off()
                        break


def adjust_temperature(home, room_name, actuator_type):
    temperature_sensors = get_room_sensors(home, room_name)
    temp_actuators = get_room_actuators(home, room_name, actuator_type)

    for temp_sensor in temperature_sensors:
        if temp_sensor.sensor_type == "IndoorTemperature":
            reading = temp_sensor.get_reading()
            if reading is not None:
                for temp_actuator in temp_actuators:
                    if actuator_type == "Heater":
                        if reading < TEMP_LOW:
                            print(
                                f"The temperature in {room_name} is {reading}°C, which is below {TEMP_LOW}°C. Turn on the heater.")
                            logger.info(
                                f"The temperature in {room_name} is {reading}°C, which is below {TEMP_LOW}°C. Turn on the heater.")
                            temp_actuator.turn_on()
                            temp_actuator.set_target_temperature(TEMP_HIGH)
                            time.sleep(TEMP_CHANGE_DURATION_WINDOW)
                        elif reading >= TEMP_HIGH:
                            print(
                                f"The temperature in {room_name} is {reading}°C, which is above {TEMP_HIGH}°C. Turn off the heater.")
                            logger.info(
                                f"The temperature in {room_name} is {reading}°C, which is above {TEMP_HIGH}°C. Turn off the heater.")
                            temp_actuator.turn_off()
                            break
                    elif actuator_type == "AC":
                        if reading > TEMP_HIGH:
                            print(
                                f"The temperature in {room_name} is {reading}°C, which is above {TEMP_HIGH}°C. Turn on the AC.")
                            logger.info(
                                f"The temperature in {room_name} is {reading}°C, which is above {TEMP_HIGH}°C. Turn on the AC.")
                            temp_actuator.turn_on()
                            temp_actuator.set_target_temperature(TEMP_LOW)
                            time.sleep(TEMP_CHANGE_DURATION_WINDOW)
                        elif reading <= TEMP_LOW:
                            print(
                                f"The temperature in {room_name} is {reading}°C, which is below {TEMP_LOW}°C. Turn off the AC.")
                            logger.info(
                                f"The temperature in {room_name} is {reading}°C, which is below {TEMP_LOW}°C. Turn off the AC.")
                            temp_actuator.turn_off()
                            break


def adjust_humidity(home, room_name, actuator_type):
    humidity_sensors = get_room_sensors(home, room_name)
    humidity_actuators = get_room_actuators(home, room_name, actuator_type)

    for humidity_sensor in humidity_sensors:
        if humidity_sensor.sensor_type == "Humidity":
            reading = humidity_sensor.get_reading()
            if reading is not None:
                for humidity_actuator in humidity_actuators:
                    if actuator_type == "Humidifier":
                        if reading < HUMIDITY_LOW:
                            print(
                                f"The humidity in {room_name} is {reading}%, which is below {HUMIDITY_LOW}%. Turn on the humidifier.")
                            logger.info(
                                f"The humidity in {room_name} is {reading}%, which is below {HUMIDITY_LOW}%. Turn on the humidifier.")
                            humidity_actuator.increase_humidity()
                            time.sleep(TEMP_CHANGE_DURATION_WINDOW)
                        elif reading >= HUMIDITY_HIGH:
                            print(
                                f"The humidity in {room_name} is {reading}%, which is above {HUMIDITY_HIGH}%. Turn off the humidifier.")
                            logger.info(
                                f"The humidity in {room_name} is {reading}%, which is above {HUMIDITY_HIGH}%. Turn off the humidifier.")
                            humidity_actuator.decrease_humidity()
                            break
                    # elif actuator_type == "Dehumidifier":  # Add a dehumidifier actuator if needed
                    #     # ... logic for dehumidifier
                    #     break


def check_and_adjust_home_status(home):
    # Home Plan
    # print("Starting Home Plan Now")
    # home = home_plan()
    # get_all_sensors(home, "IndoorTemperature")
    # get_all_actuators(home, "Light")

    for room_name in ["LivingRoom", "Bedroom", "Kitchen", "Bathroom", "Balcony"]:
        # turn on light if dark
        turn_on_light_if_dark(home, room_name)

        # turn off light if bright
        turn_off_light_if_bright(home, room_name)

        # Adjust temperature
        adjust_temperature(home, room_name, "Heater")
        adjust_temperature(home, room_name, "AC")

        # Adjust humidity
        adjust_humidity(home, room_name, "Humidifier")
        # adjust_humidity(home, room_name, "Dehumidifier")


if __name__ == "__main__":
    home = home_plan()
    check_and_adjust_home_status(home)