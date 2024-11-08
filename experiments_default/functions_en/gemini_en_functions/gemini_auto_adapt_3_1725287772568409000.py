from home.home_plan import get_room, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, \
    OutdoorTemperatureSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, \
    SmartSocket, Door, \
    CleaningRobot, SmartTV, Humidifier
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger
from home.config import TEMP_CHANGE_DURATION_WINDOW, DAILY_ROUTINE_DURATION

# Example usage
from home.home_plan import home_plan
home = home_plan()


def main():
    # Check the Temperature in LivingRoom
    living_room = get_room(home, "LivingRoom")
    sensors = get_room_sensors(home, "LivingRoom")
    for sensor in sensors:
        if sensor.sensor_type == "IndoorTemperature":
            temp = sensor.get_reading()
            print(f"The current temperature in the LivingRoom is {temp} degrees Celsius.")
            logger.info(f"The current temperature in the LivingRoom is {temp} degrees Celsius.")
            if temp < TEMP_LOW:
                print(f"The temperature in the LivingRoom is too low. Turning on the heater.")
                logger.info(f"The temperature in the LivingRoom is too low. Turning on the heater.")
                # Turn on the heater
                for actuator in living_room.actuators:
                    if actuator.actuator_type == "Heater":
                        actuator.turn_on()
                        actuator.set_target_temperature(TEMP_HIGH)
                        break
            elif temp > TEMP_HIGH:
                print(f"The temperature in the LivingRoom is too high. Turning on the AC.")
                logger.info(f"The temperature in the LivingRoom is too high. Turning on the AC.")
                # Turn on the AC
                for actuator in living_room.actuators:
                    if actuator.actuator_type == "AC":
                        actuator.turn_on()
                        actuator.set_target_temperature(TEMP_LOW)
                        break
            else:
                print(f"The temperature in the LivingRoom is comfortable.")
                logger.info(f"The temperature in the LivingRoom is comfortable.")

    # Check the humidity in the LivingRoom
    for sensor in sensors:
        if sensor.sensor_type == "Humidity":
            humidity = sensor.get_reading()
            print(f"The current humidity in the LivingRoom is {humidity}%.")
            logger.info(f"The current humidity in the LivingRoom is {humidity}%.")
            if humidity < HUMIDITY_LOW:
                print(f"The humidity in the LivingRoom is too low. Turning on the humidifier.")
                logger.info(f"The humidity in the LivingRoom is too low. Turning on the humidifier.")
                # Turn on the humidifier
                for actuator in living_room.actuators:
                    if actuator.actuator_type == "Humidifier":
                        actuator.turn_on()
                        actuator.increase_humidity()
                        break
            elif humidity > HUMIDITY_HIGH:
                print(f"The humidity in the LivingRoom is too high. Turning off the humidifier.")
                logger.info(f"The humidity in the LivingRoom is too high. Turning off the humidifier.")
                # Turn off the humidifier
                for actuator in living_room.actuators:
                    if actuator.actuator_type == "Humidifier":
                        actuator.turn_off()
                        break
            else:
                print(f"The humidity in the LivingRoom is comfortable.")
                logger.info(f"The humidity in the LivingRoom is comfortable.")

    # Check the light intensity in the LivingRoom
    for sensor in sensors:
        if sensor.sensor_type == "LightIntensive":
            light_intensity = sensor.get_reading()
            print(f"The current light intensity in the LivingRoom is {light_intensity} lux.")
            logger.info(f"The current light intensity in the LivingRoom is {light_intensity} lux.")
            if light_intensity < LIGHT_INTENSITY_LOW:
                print(f"The light intensity in the LivingRoom is too low. Turning on the light.")
                logger.info(f"The light intensity in the LivingRoom is too low. Turning on the light.")
                # Turn on the light
                for actuator in living_room.actuators:
                    if actuator.actuator_type == "Light":
                        actuator.turn_on()
                        actuator.set_brightness_level("medium")
                        break
            else:
                print(f"The light intensity in the LivingRoom is sufficient.")
                logger.info(f"The light intensity in the LivingRoom is sufficient.")

    # Check the temperature in the Bedroom
    bedroom = get_room(home, "Bedroom")
    sensors = get_room_sensors(home, "Bedroom")
    for sensor in sensors:
        if sensor.sensor_type == "IndoorTemperature":
            temp = sensor.get_reading()
            print(f"The current temperature in the Bedroom is {temp} degrees Celsius.")
            logger.info(f"The current temperature in the Bedroom is {temp} degrees Celsius.")
            if temp < TEMP_LOW:
                print(f"The temperature in the Bedroom is too low. Turning on the heater.")
                logger.info(f"The temperature in the Bedroom is too low. Turning on the heater.")
                # Turn on the heater
                for actuator in bedroom.actuators:
                    if actuator.actuator_type == "Heater":
                        actuator.turn_on()
                        actuator.set_target_temperature(TEMP_HIGH)
                        break
            elif temp > TEMP_HIGH:
                print(f"The temperature in the Bedroom is too high. Turning on the AC.")
                logger.info(f"The temperature in the Bedroom is too high. Turning on the AC.")
                # Turn on the AC
                for actuator in bedroom.actuators:
                    if actuator.actuator_type == "AC":
                        actuator.turn_on()
                        actuator.set_target_temperature(TEMP_LOW)
                        break
            else:
                print(f"The temperature in the Bedroom is comfortable.")
                logger.info(f"The temperature in the Bedroom is comfortable.")

    # Check the humidity in the Bedroom
    for sensor in sensors:
        if sensor.sensor_type == "Humidity":
            humidity = sensor.get_reading()
            print(f"The current humidity in the Bedroom is {humidity}%.")
            logger.info(f"The current humidity in the Bedroom is {humidity}%.")
            if humidity < HUMIDITY_LOW:
                print(f"The humidity in the Bedroom is too low. Turning on the humidifier.")
                logger.info(f"The humidity in the Bedroom is too low. Turning on the humidifier.")
                # Turn on the humidifier
                for actuator in bedroom.actuators:
                    if actuator.actuator_type == "Humidifier":
                        actuator.turn_on()
                        actuator.increase_humidity()
                        break
            elif humidity > HUMIDITY_HIGH:
                print(f"The humidity in the Bedroom is too high. Turning off the humidifier.")
                logger.info(f"The humidity in the Bedroom is too high. Turning off the humidifier.")
                # Turn off the humidifier
                for actuator in bedroom.actuators:
                    if actuator.actuator_type == "Humidifier":
                        actuator.turn_off()
                        break
            else:
                print(f"The humidity in the Bedroom is comfortable.")
                logger.info(f"The humidity in the Bedroom is comfortable.")

    # Check the light intensity in the Bedroom
    for sensor in sensors:
        if sensor.sensor_type == "LightIntensive":
            light_intensity = sensor.get_reading()
            print(f"The current light intensity in the Bedroom is {light_intensity} lux.")
            logger.info(f"The current light intensity in the Bedroom is {light_intensity} lux.")
            if light_intensity < LIGHT_INTENSITY_LOW:
                print(f"The light intensity in the Bedroom is too low. Turning on the light.")
                logger.info(f"The light intensity in the Bedroom is too low. Turning on the light.")
                # Turn on the light
                for actuator in bedroom.actuators:
                    if actuator.actuator_type == "Light":
                        actuator.turn_on()
                        actuator.set_brightness_level("medium")
                        break
            else:
                print(f"The light intensity in the Bedroom is sufficient.")
                logger.info(f"The light intensity in the Bedroom is sufficient.")

    # Check the temperature in the Kitchen
    kitchen = get_room(home, "Kitchen")
    sensors = get_room_sensors(home, "Kitchen")
    for sensor in sensors:
        if sensor.sensor_type == "IndoorTemperature":
            temp = sensor.get_reading()
            print(f"The current temperature in the Kitchen is {temp} degrees Celsius.")
            logger.info(f"The current temperature in the Kitchen is {temp} degrees Celsius.")
            if temp < TEMP_LOW:
                print(f"The temperature in the Kitchen is too low. Turning on the heater.")
                logger.info(f"The temperature in the Kitchen is too low. Turning on the heater.")
                # Turn on the heater
                for actuator in kitchen.actuators:
                    if actuator.actuator_type == "Heater":
                        actuator.turn_on()
                        actuator.set_target_temperature(TEMP_HIGH)
                        break
            elif temp > TEMP_HIGH:
                print(f"The temperature in the Kitchen is too high. Turning on the AC.")
                logger.info(f"The temperature in the Kitchen is too high. Turning on the AC.")
                # Turn on the AC
                for actuator in kitchen.actuators:
                    if actuator.actuator_type == "AC":
                        actuator.turn_on()
                        actuator.set_target_temperature(TEMP_LOW)
                        break
            else:
                print(f"The temperature in the Kitchen is comfortable.")
                logger.info(f"The temperature in the Kitchen is comfortable.")

    # Check the humidity in the Kitchen
    for sensor in sensors:
        if sensor.sensor_type == "Humidity":
            humidity = sensor.get_reading()
            print(f"The current humidity in the Kitchen is {humidity}%.")
            logger.info(f"The current humidity in the Kitchen is {humidity}%.")
            if humidity < HUMIDITY_LOW:
                print(f"The humidity in the Kitchen is too low. Turning on the humidifier.")
                logger.info(f"The humidity in the Kitchen is too low. Turning on the humidifier.")
                # Turn on the humidifier
                for actuator in kitchen.actuators:
                    if actuator.actuator_type == "Humidifier":
                        actuator.turn_on()
                        actuator.increase_humidity()
                        break
            elif humidity > HUMIDITY_HIGH:
                print(f"The humidity in the Kitchen is too high. Turning off the humidifier.")
                logger.info(f"The humidity in the Kitchen is too high. Turning off the humidifier.")
                # Turn off the humidifier
                for actuator in kitchen.actuators:
                    if actuator.actuator_type == "Humidifier":
                        actuator.turn_off()
                        break
            else:
                print(f"The humidity in the Kitchen is comfortable.")
                logger.info(f"The humidity in the Kitchen is comfortable.")

    # Check the smoke in the Kitchen
    for sensor in sensors:
        if sensor.sensor_type == "Smoke":
            smoke_level = sensor.get_reading()
            print(f"The current smoke level in the Kitchen is {smoke_level}%.")
            logger.info(f"The current smoke level in the Kitchen is {smoke_level}%.")
            if smoke_level > 0:
                print(f"Smoke detected in the Kitchen. Turning on the notification sender and opening the windows.")
                logger.warning(f"Smoke detected in the Kitchen. Turning on the notification sender and opening the windows.")
                # Turn on the notification sender
                for actuator in kitchen.actuators:
                    if actuator.actuator_type == "NotificationSender":
                        actuator.turn_on()
                        actuator.notification_sender("Smoke detected in the Kitchen! Please check.")
                        break
                # Open the windows
                for actuator in kitchen.actuators:
                    if actuator.actuator_type == "Window":
                        actuator.turn_on()
                        break

    # Check the temperature in the Bathroom
    bathroom = get_room(home, "Bathroom")
    sensors = get_room_sensors(home, "Bathroom")
    for sensor in sensors:
        if sensor.sensor_type == "IndoorTemperature":
            temp = sensor.get_reading()
            print(f"The current temperature in the Bathroom is {temp} degrees Celsius.")
            logger.info(f"The current temperature in the Bathroom is {temp} degrees Celsius.")
            if temp < TEMP_LOW:
                print(f"The temperature in the Bathroom is too low. Turning on the heater.")
                logger.info(f"The temperature in the Bathroom is too low. Turning on the heater.")
                # Turn on the heater
                for actuator in bathroom.actuators:
                    if actuator.actuator_type == "Heater":
                        actuator.turn_on()
                        actuator.set_target_temperature(TEMP_HIGH)
                        break
            elif temp > TEMP_HIGH:
                print(f"The temperature in the Bathroom is too high. Turning on the AC.")
                logger.info(f"The temperature in the Bathroom is too high. Turning on the AC.")
                # Turn on the AC
                for actuator in bathroom.actuators:
                    if actuator.actuator_type == "AC":
                        actuator.turn_on()
                        actuator.set_target_temperature(TEMP_LOW)
                        break
            else:
                print(f"The temperature in the Bathroom is comfortable.")
                logger.info(f"The temperature in the Bathroom is comfortable.")

    # Check the humidity in the Bathroom
    for sensor in sensors:
        if sensor.sensor_type == "Humidity":
            humidity = sensor.get_reading()
            print(f"The current humidity in the Bathroom is {humidity}%.")
            logger.info(f"The current humidity in the Bathroom is {humidity}%.")
            if humidity < HUMIDITY_LOW:
                print(f"The humidity in the Bathroom is too low. Turning on the humidifier.")
                logger.info(f"The humidity in the Bathroom is too low. Turning on the humidifier.")
                # Turn on the humidifier
                for actuator in bathroom.actuators:
                    if actuator.actuator_type == "Humidifier":
                        actuator.turn_on()
                        actuator.increase_humidity()
                        break
            elif humidity > HUMIDITY_HIGH:
                print(f"The humidity in the Bathroom is too high. Turning off the humidifier.")
                logger.info(f"The humidity in the Bathroom is too high. Turning off the humidifier.")
                # Turn off the humidifier
                for actuator in bathroom.actuators:
                    if actuator.actuator_type == "Humidifier":
                        actuator.turn_off()
                        break
            else:
                print(f"The humidity in the Bathroom is comfortable.")
                logger.info(f"The humidity in the Bathroom is comfortable.")

    # Check the temperature in the Balcony
    balcony = get_room(home, "Balcony")
    sensors = get_room_sensors(home, "Balcony")
    for sensor in sensors:
        if sensor.sensor_type == "OutdoorTemperature":
            temp = sensor.get_reading()
            print(f"The current temperature in the Balcony is {temp} degrees Celsius.")
            logger.info(f"The current temperature in the Balcony is {temp} degrees Celsius.")

    # Start daily cleaning routine
    print(f"Starting daily cleaning routine.")
    logger.info(f"Starting daily cleaning routine.")
    for room in home:
        for actuator in room.actuators:
            if actuator.actuator_type == "CleaningRobot":
                actuator.turn_on()
                actuator.daily_routine()
                break

    print(f"Daily cleaning routine completed.")
    logger.info(f"Daily cleaning routine completed.")

    # Run the main loop
    while True:
        # Check the temperature in each room and adjust the heater or AC accordingly
        for room_name in ["LivingRoom", "Bedroom", "Kitchen", "Bathroom"]:
            room = get_room(home, room_name)
            sensors = get_room_sensors(home, room_name)
            for sensor in sensors:
                if sensor.sensor_type == "IndoorTemperature":
                    temp = sensor.get_reading()
                    print(f"The current temperature in the {room_name} is {temp} degrees Celsius.")
                    logger.info(f"The current temperature in the {room_name} is {temp} degrees Celsius.")
                    if temp < TEMP_LOW:
                        print(f"The temperature in the {room_name} is too low. Turning on the heater.")
                        logger.info(f"The temperature in the {room_name} is too low. Turning on the heater.")
                        # Turn on the heater
                        for actuator in room.actuators:
                            if actuator.actuator_type == "Heater":
                                actuator.turn_on()
                                actuator.set_target_temperature(TEMP_HIGH)
                                break
                    elif temp > TEMP_HIGH:
                        print(f"The temperature in the {room_name} is too high. Turning on the AC.")
                        logger.info(f"The temperature in the {room_name} is too high. Turning on the AC.")
                        # Turn on the AC
                        for actuator in room.actuators:
                            if actuator.actuator_type == "AC":
                                actuator.turn_on()
                                actuator.set_target_temperature(TEMP_LOW)
                                break
                    else:
                        print(f"The temperature in the {room_name} is comfortable.")
                        logger.info(f"The temperature in the {room_name} is comfortable.")

        # Check the humidity in each room and adjust the humidifier accordingly
        for room_name in ["LivingRoom", "Bedroom", "Kitchen", "Bathroom"]:
            room = get_room(home, room_name)
            sensors = get_room_sensors(home, room_name)
            for sensor in sensors:
                if sensor.sensor_type == "Humidity":
                    humidity = sensor.get_reading()
                    print(f"The current humidity in the {room_name} is {humidity}%.")
                    logger.info(f"The current humidity in the {room_name} is {humidity}%.")
                    if humidity < HUMIDITY_LOW:
                        print(f"The humidity in the {room_name} is too low. Turning on the humidifier.")
                        logger.info(f"The humidity in the {room_name} is too low. Turning on the humidifier.")
                        # Turn on the humidifier
                        for actuator in room.actuators:
                            if actuator.actuator_type == "Humidifier":
                                actuator.turn_on()
                                actuator.increase_humidity()
                                break
                    elif humidity > HUMIDITY_HIGH:
                        print(f"The humidity in the {room_name} is too high. Turning off the humidifier.")
                        logger.info(f"The humidity in the {room_name} is too high. Turning off the humidifier.")
                        # Turn off the humidifier
                        for actuator in room.actuators:
                            if actuator.actuator_type == "Humidifier":
                                actuator.turn_off()
                                break
                    else:
                        print(f"The humidity in the {room_name} is comfortable.")
                        logger.info(f"The humidity in the {room_name} is comfortable.")

        # Check the light intensity in each room and adjust the light accordingly
        for room_name in ["LivingRoom", "Bedroom", "Kitchen", "Bathroom"]:
            room = get_room(home, room_name)
            sensors = get_room_sensors(home, room_name)
            for sensor in sensors:
                if sensor.sensor_type == "LightIntensive":
                    light_intensity = sensor.get_reading()
                    print(f"The current light intensity in the {room_name} is {light_intensity} lux.")
                    logger.info(f"The current light intensity in the {room_name} is {light_intensity} lux.")
                    if light_intensity < LIGHT_INTENSITY_LOW:
                        print(f"The light intensity in the {room_name} is too low. Turning on the light.")
                        logger.info(f"The light intensity in the {room_name} is too low. Turning on the light.")
                        # Turn on the light
                        for actuator in room.actuators:
                            if actuator.actuator_type == "Light":
                                actuator.turn_on()
                                actuator.set_brightness_level("medium")
                                break
                    else:
                        print(f"The light intensity in the {room_name} is sufficient.")
                        logger.info(f"The light intensity in the {room_name} is sufficient.")

        # Check the smoke in the Kitchen and adjust the notification sender and windows accordingly
        kitchen = get_room(home, "Kitchen")
        sensors = get_room_sensors(home, "Kitchen")
        for sensor in sensors:
            if sensor.sensor_type == "Smoke":
                smoke_level = sensor.get_reading()
                print(f"The current smoke level in the Kitchen is {smoke_level}%.")
                logger.info(f"The current smoke level in the Kitchen is {smoke_level}%.")
                if smoke_level > 0:
                    print(f"Smoke detected in the Kitchen. Turning on the notification sender and opening the windows.")
                    logger.warning(f"Smoke detected in the Kitchen. Turning on the notification sender and opening the windows.")
                    # Turn on the notification sender
                    for actuator in kitchen.actuators:
                        if actuator.actuator_type == "NotificationSender":
                            actuator.turn_on()
                            actuator.notification_sender("Smoke detected in the Kitchen! Please check.")
                            break
                    # Open the windows
                    for actuator in kitchen.actuators:
                        if actuator.actuator_type == "Window":
                            actuator.turn_on()
                            break

        # Wait for a short period before checking the sensors again
        time.sleep(TEMP_CHANGE_DURATION_WINDOW)


if __name__ == "__main__":
    main()
