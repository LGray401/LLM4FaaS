from home.home_plan import get_room, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators
from home.logger_config import logger
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, \
    TEMP_CHANGE_DURATION_WINDOW


def morning_plan(home):
    living_room = get_room(home, "LivingRoom")
    if living_room is not None:
        curtains = get_room_actuators(home, "LivingRoom")
        if curtains is not None:
            for curtain in curtains:
                if curtain.actuator_type == "Curtain":
                    curtain.turn_on()
                    logger.info("Curtains are open.")
                    print("Curtains are open.")


def leave_home_plan(home):
    for room in home:
        lights = get_room_actuators(room, room.name)
        if lights is not None:
            for light in lights:
                if light.actuator_type == "Light":
                    light.turn_off()
                    logger.info(f"Light in {room.name} is turned off.")
                    print(f"Light in {room.name} is turned off.")


def movie_plan(home):
    living_room = get_room(home, "LivingRoom")
    if living_room is not None:
        lights = get_room_actuators(living_room, "LivingRoom")
        if lights is not None:
            for light in lights:
                if light.actuator_type == "Light":
                    light.set_brightness_level("low")
                    logger.info("Light in LivingRoom is set to low brightness.")
                    print("Light in LivingRoom is set to low brightness.")

        tv = get_room_actuators(living_room, "LivingRoom")
        if tv is not None:
            for tv_ in tv:
                if tv_.actuator_type == "SmartTV":
                    tv_.turn_on()
                    logger.info("SmartTV in LivingRoom is turned on.")
                    print("SmartTV in LivingRoom is turned on.")


def temperature_control(home):
    for room in home:
        temperature_sensors = get_room_sensors(home, room.name)
        if temperature_sensors is not None:
            for temperature_sensor in temperature_sensors:
                if temperature_sensor.sensor_type == "IndoorTemperature":
                    temperature_reading = temperature_sensor.get_reading()
                    if temperature_reading is not None:
                        heaters = get_room_actuators(home, room.name)
                        if heaters is not None:
                            for heater in heaters:
                                if heater.actuator_type == "Heater":
                                    heater.adjust_temperature(temperature_reading)
                                    if temperature_reading < TEMP_LOW:
                                        heater.turn_on()
                                        logger.info(f"Heater in {room.name} is turned on.")
                                        print(f"Heater in {room.name} is turned on.")
                                        time.sleep(TEMP_CHANGE_DURATION_WINDOW)
                                    elif temperature_reading > TEMP_HIGH:
                                        heater.turn_off()
                                        logger.info(f"Heater in {room.name} is turned off.")
                                        print(f"Heater in {room.name} is turned off.")
                                        time.sleep(TEMP_CHANGE_DURATION_WINDOW)

                        acs = get_room_actuators(home, room.name)
                        if acs is not None:
                            for ac in acs:
                                if ac.actuator_type == "AC":
                                    ac.adjust_temperature(temperature_reading)
                                    if temperature_reading > TEMP_HIGH:
                                        ac.turn_on()
                                        logger.info(f"AC in {room.name} is turned on.")
                                        print(f"AC in {room.name} is turned on.")
                                        time.sleep(TEMP_CHANGE_DURATION_WINDOW)
                                    elif temperature_reading < TEMP_LOW:
                                        ac.turn_off()
                                        logger.info(f"AC in {room.name} is turned off.")
                                        print(f"AC in {room.name} is turned off.")
                                        time.sleep(TEMP_CHANGE_DURATION_WINDOW)


def humidity_control(home):
    for room in home:
        humidity_sensors = get_room_sensors(home, room.name)
        if humidity_sensors is not None:
            for humidity_sensor in humidity_sensors:
                if humidity_sensor.sensor_type == "Humidity":
                    humidity_reading = humidity_sensor.get_reading()
                    if humidity_reading is not None:
                        humidifiers = get_room_actuators(home, room.name)
                        if humidifiers is not None:
                            for humidifier in humidifiers:
                                if humidifier.actuator_type == "Humidifier":
                                    if humidity_reading < HUMIDITY_LOW:
                                        humidifier.increase_humidity()
                                        logger.info(f"Humidifier in {room.name} is turned on.")
                                        print(f"Humidifier in {room.name} is turned on.")
                                    elif humidity_reading > HUMIDITY_HIGH:
                                        humidifier.decrease_humidity()
                                        logger.info(f"Humidifier in {room.name} is turned off.")
                                        print(f"Humidifier in {room.name} is turned off.")


def light_intensity_control(home):
    for room in home:
        light_intensity_sensors = get_room_sensors(home, room.name)
        if light_intensity_sensors is not None:
            for light_intensity_sensor in light_intensity_sensors:
                if light_intensity_sensor.sensor_type == "LightIntensive":
                    light_intensity_reading = light_intensity_sensor.get_reading()
                    if light_intensity_reading is not None:
                        lights = get_room_actuators(home, room.name)
                        if lights is not None:
                            for light in lights:
                                if light.actuator_type == "Light":
                                    if light_intensity_reading < LIGHT_INTENSITY_LOW:
                                        light.turn_on()
                                        logger.info(f"Light in {room.name} is turned on.")
                                        print(f"Light in {room.name} is turned on.")
                                    elif light_intensity_reading > LIGHT_INTENSITY_HIGH:
                                        light.turn_off()
                                        logger.info(f"Light in {room.name} is turned off.")
                                        print(f"Light in {room.name} is turned off.")


def smoke_detection(home):
    for room in home:
        smoke_sensors = get_room_sensors(home, room.name)
        if smoke_sensors is not None:
            for smoke_sensor in smoke_sensors:
                if smoke_sensor.sensor_type == "Smoke":
                    smoke_reading = smoke_sensor.get_reading()
                    if smoke_reading is not None and smoke_reading > 50:
                        notification_senders = get_all_actuators(home, "NotificationSender")
                        if notification_senders is not None:
                            for notification_sender in notification_senders:
                                notification_sender.notification_sender(
                                    f"Smoke detected in {room.name}! Please check.")
                                logger.warning(f"Smoke detected in {room.name}! Please check.")
                                print(f"Smoke detected in {room.name}! Please check.")


def main():
    home = home_plan()

    # Example usage:
    morning_plan(home)
    leave_home_plan(home)
    movie_plan(home)
    temperature_control(home)
    humidity_control(home)
    light_intensity_control(home)
    smoke_detection(home)


if __name__ == "__main__":
    main()

# This code file `function.py` includes functions for different smart home scenarios. 
# The functions leverage the classes defined in `sensor.py`, `actuator.py`, and `home_plan.py`.
# Here's a breakdown of what the functions do:

# **`morning_plan`:**
# - Opens the curtains in the LivingRoom.

# **`leave_home_plan`:**
# - Turns off all lights in all rooms.

# **`movie_plan`:**
# - Sets the lights in the LivingRoom to low brightness.
# - Turns on the SmartTV in the LivingRoom.

# **`temperature_control`:**
# - Checks the temperature readings from indoor temperature sensors in each room.
# - Adjusts the temperature using heaters and ACs based on the readings and predefined thresholds (TEMP_LOW and TEMP_HIGH).

# **`humidity_control`:**
# - Checks the humidity readings from humidity sensors in each room.
# - Adjusts the humidity using humidifiers based on the readings and predefined thresholds (HUMIDITY_LOW and HUMIDITY_HIGH).

# **`light_intensity_control`:**
# - Checks the light intensity readings from light intensity sensors in each room.
# - Turns on/off lights based on the readings and predefined thresholds (LIGHT_INTENSITY_LOW and LIGHT_INTENSITY_HIGH).

# **`smoke_detection`:**
# - Checks the smoke readings from smoke sensors in each room.
# - Sends a notification to all notification senders if smoke is detected (reading > 50).

# **`main`:**
# - Creates the home plan using `home_plan()`.
# - Calls each scenario function to demonstrate how they work.

# This file effectively orchestrates the actions of your smart home system based on different user needs and sensor readings.
