from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_actuators, get_all_sensors
from home.config import TEMP_HIGH, TEMP_LOW, HUMIDITY_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_HIGH, LIGHT_INTENSITY_LOW
from home.logger_config import logger


def morning_plan(home):
    print("----Start Morning Plan----")
    logger.info("----Start Morning Plan----")
    living_room = get_room(home, "LivingRoom")
    if living_room is not None:
        living_room_lights = get_room_actuators(home, "LivingRoom")
        for light in living_room_lights:
            if light.actuator_type == "Light":
                light.turn_on()
                light.set_brightness_level("medium")
    else:
        print("Cannot find LivingRoom")
        logger.warning("Cannot find LivingRoom")


def leave_home_plan(home):
    print("----Start Leave Home Plan----")
    logger.info("----Start Leave Home Plan----")
    all_lights = get_all_actuators(home, "Light")
    for light in all_lights:
        light.turn_off()
    all_doors = get_all_actuators(home, "Door")
    for door in all_doors:
        door.lock()


def movie_plan(home):
    print("----Start Movie Plan----")
    logger.info("----Start Movie Plan----")
    living_room = get_room(home, "LivingRoom")
    if living_room is not None:
        living_room_lights = get_room_actuators(home, "LivingRoom")
        for light in living_room_lights:
            if light.actuator_type == "Light":
                light.turn_on()
                light.set_brightness_level("low")
        living_room_tv = get_room_actuators(home, "LivingRoom")
        for tv in living_room_tv:
            if tv.actuator_type == "SmartTV":
                tv.turn_on()
                tv.play_channel("Netflix")
    else:
        print("Cannot find LivingRoom")
        logger.warning("Cannot find LivingRoom")


def smart_home_system_run():
    home = home_plan()
    print_home_plan(home)

    morning_plan(home)
    # time.sleep(3)  # Simulate some time passing
    leave_home_plan(home)
    # time.sleep(3)  # Simulate some time passing
    movie_plan(home)

    # # Adjust temperature and humidity based on sensor readings
    # while True:
    #     all_temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    #     for temp_sensor in all_temperature_sensors:
    #         current_temperature = temp_sensor.get_reading()
    #         if current_temperature is not None:
    #             adjust_temperature(home, current_temperature)
    #
    #     all_humidity_sensors = get_all_sensors(home, "Humidity")
    #     for humidity_sensor in all_humidity_sensors:
    #         current_humidity = humidity_sensor.get_reading()
    #         if current_humidity is not None:
    #             adjust_humidity(home, current_humidity)
    #
    #     time.sleep(TEMP_CHANGE_DURATION_WINDOW)


def adjust_temperature(home, current_temperature):
    print(f"Current temperature is {current_temperature}°C.")
    logger.info(f"Current temperature is {current_temperature}°C.")
    all_heaters = get_all_actuators(home, "Heater")
    all_acs = get_all_actuators(home, "AC")

    for heater in all_heaters:
        heater.adjust_temperature(current_temperature)

    for ac in all_acs:
        ac.adjust_temperature(current_temperature)


def adjust_humidity(home, current_humidity):
    print(f"Current humidity is {current_humidity}%")
    logger.info(f"Current humidity is {current_humidity}%")
    all_humidifiers = get_all_actuators(home, "Humidifier")

    for humidifier in all_humidifiers:
        if current_humidity < HUMIDITY_LOW:
            humidifier.increase_humidity()
        elif current_humidity > HUMIDITY_HIGH:
            humidifier.decrease_humidity()

def adjust_light_intensity(home, current_light_intensity):
    print(f"Current Light Intensity is {current_light_intensity} lux")
    logger.info(f"Current Light Intensity is {current_light_intensity} lux")

    all_lights = get_all_actuators(home, "Light")
    for light in all_lights:
        if current_light_intensity < LIGHT_INTENSITY_LOW:
            light.turn_on()
            light.set_brightness_level("high")
        elif current_light_intensity > LIGHT_INTENSITY_HIGH:
            light.set_brightness_level("low")


if __name__ == '__main__':
    smart_home_system_run()