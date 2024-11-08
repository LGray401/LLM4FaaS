# Sure! I will create the 'function.py' file based on the given functional description and the provided source code files.
# 
# Here is the 'function.py' file:

from home.home_plan import *
from home.config import *
from home.logger_config import logger


def main():
    home = home_plan()

    # Get all temperature sensors
    temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    # Get all humidity sensors
    humidity_sensors = get_all_sensors(home, "Humidity")
    # Get all light intensity sensors
    light_intensity_sensors = get_all_sensors(home, "LightIntensive")
    # Get all AC actuators
    ac_actuators = get_all_actuators(home, "AC")
    # Get all window actuators
    window_actuators = get_all_actuators(home, "Window")
    # Get all curtain actuators
    curtain_actuators = get_all_actuators(home, "Curtain")
    # Get all lights actuators
    lights_actuators = get_all_actuators(home, "Light")

    # Check temperature and control AC
    for temperature_sensor in temperature_sensors:
        temperature = temperature_sensor.get_reading()
        if temperature is not None:
            if temperature > TEMP_HIGH:
                for ac_actuator in ac_actuators:
                    ac_actuator.turn_on()
                for window_actuator in window_actuators:
                    window_actuator.close()
                logger.info("Temperature is high. AC turned on and windows closed.")
            elif temperature < TEMP_LOW:
                for ac_actuator in ac_actuators:
                    ac_actuator.turn_off()
                logger.info("Temperature is low. AC turned off.")

    # Check humidity and control humidifier
    for humidity_sensor in humidity_sensors:
        humidity = humidity_sensor.get_reading()
        if humidity is not None:
            if humidity < HUMIDITY_LOW:
                for humidifier_actuator in humidifier_actuators:
                    humidifier_actuator.turn_on()
                logger.info("Humidity is low. Humidifier turned on.")
            elif humidity > HUMIDITY_HIGH:
                for humidifier_actuator in humidifier_actuators:
                    humidifier_actuator.turn_off()
                logger.info("Humidity is high. Humidifier turned off.")

    # Check light intensity and control lights
    for light_intensity_sensor in light_intensity_sensors:
        light_intensity = light_intensity_sensor.get_reading()
        if light_intensity is not None:
            if light_intensity < LIGHT_INTENSITY_LOW:
                for light_actuator in lights_actuators:
                    light_actuator.turn_on()
                logger.info("Light intensity is low. Lights turned on.")
            elif light_intensity > LIGHT_INTENSITY_HIGH:
                for light_actuator in lights_actuators:
                    light_actuator.turn_off()
                for curtain_actuator in curtain_actuators:
                    curtain_actuator.close()
                logger.info("Light intensity is high. Lights turned off and curtains closed.")


if __name__ == "__main__":
    main()