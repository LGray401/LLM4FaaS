# Sure! Here is the 'function.py' file based on your functional description and the provided source code:

from home.home_plan import get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Light, AC
from home.logger_config import logger
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    # Get the sensors and actuators for the rooms
    living_room_sensors = get_room_sensors(home, "LivingRoom")
    living_room_actuators = get_room_actuators(home, "LivingRoom")
    bedroom_sensors = get_room_sensors(home, "Bedroom")
    bedroom_actuators = get_room_actuators(home, "Bedroom")
    kitchen_sensors = get_room_sensors(home, "Kitchen")
    kitchen_actuators = get_room_actuators(home, "Kitchen")

    # Get all temperature sensors
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")

    # Get all humidity sensors
    humidity_sensors = get_all_sensors(home, "Humidity")

    # Get all light intensity sensors
    light_intensity_sensors = get_all_sensors(home, "LightIntensive")

    # Loop to keep the smart home running
    while True:
        # Check and adjust the temperature in the living room
        for sensor in living_room_sensors:
            if isinstance(sensor, IndoorTemperatureSensor):
                current_temperature = sensor.get_reading()
                if current_temperature < TEMP_LOW:
                    logger.info(f"Temperature in Living Room is too low: {current_temperature}°C. Turning on AC.")
                    for actuator in living_room_actuators:
                        if isinstance(actuator, AC):
                            actuator.turn_on()
                elif current_temperature > TEMP_HIGH:
                    logger.info(f"Temperature in Living Room is too high: {current_temperature}°C. Turning on AC.")
                    for actuator in living_room_actuators:
                        if isinstance(actuator, AC):
                            actuator.turn_on()
                else:
                    for actuator in living_room_actuators:
                        if isinstance(actuator, AC):
                            actuator.turn_off()

        # Check and adjust the humidity in the bedroom
        for sensor in bedroom_sensors:
            if isinstance(sensor, HumiditySensor):
                current_humidity = sensor.get_reading()
                if current_humidity < HUMIDITY_LOW:
                    logger.info(f"Humidity in Bedroom is too low: {current_humidity}%. Turning on Humidifier.")
                    for actuator in bedroom_actuators:
                        if isinstance(actuator, Humidifier):
                            actuator.turn_on()
                            actuator.increase_humidity()
                elif current_humidity > HUMIDITY_HIGH:
                    logger.info(f"Humidity in Bedroom is too high: {current_humidity}%. Turning on Dehumidifier.")
                    for actuator in bedroom_actuators:
                        if isinstance(actuator, Humidifier):
                            actuator.turn_on()
                            actuator.decrease_humidity()
                else:
                    for actuator in bedroom_actuators:
                        if isinstance(actuator, Humidifier):
                            actuator.turn_off()

        # Check and adjust the light intensity in the kitchen
        for sensor in kitchen_sensors:
            if isinstance(sensor, LightIntensiveSensor):
                current_light_intensity = sensor.get_reading()
                if current_light_intensity < LIGHT_INTENSITY_LOW:
                    logger.info(f"Light intensity in Kitchen is too low: {current_light_intensity} lux. Turning on Light.")
                    for actuator in kitchen_actuators:
                        if isinstance(actuator, Light):
                            actuator.turn_on()
                            actuator.set_brightness_level("medium")
                elif current_light_intensity > LIGHT_INTENSITY_HIGH:
                    logger.info(f"Light intensity in Kitchen is too high: {current_light_intensity} lux. Turning off Light.")
                    for actuator in kitchen_actuators:
                        if isinstance(actuator, Light):
                            actuator.turn_off()
                else:
                    for actuator in kitchen_actuators:
                        if isinstance(actuator, Light):
                            actuator.turn_off()

        # Check and adjust all the temperatures
        for sensor in indoor_temp_sensors:
            current_temperature = sensor.get_reading()
            if current_temperature < TEMP_LOW:
                logger.info(f"Temperature is too low: {current_temperature}°C. Turning on Heater.")
                for actuator in get_all_actuators(home, "Heater"):
                    actuator.turn_on()
                    actuator.set_target_temperature(TEMP_HIGH)
                    actuator.adjust_temperature(current_temperature)
            elif current_temperature > TEMP_HIGH:
                logger.info(f"Temperature is too high: {current_temperature}°C. Turning on AC.")
                for actuator in get_all_actuators(home, "AC"):
                    actuator.turn_on()
                    actuator.set_target_temperature(TEMP_LOW)
                    actuator.adjust_temperature(current_temperature)
            else:
                for actuator in get_all_actuators(home, "Heater"):
                    actuator.turn_off()
                for actuator in get_all_actuators(home, "AC"):
                    actuator.turn_off()

        # Sleep for a while before checking the readings again
        time.sleep(TEMP_CHANGE_DURATION_WINDOW)

if __name__ == "__main__":
    main()