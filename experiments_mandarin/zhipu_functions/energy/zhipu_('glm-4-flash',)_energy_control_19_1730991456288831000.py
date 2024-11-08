# Based on your functional description and the source code you've provided, I'll create a `function.py` file that includes a `main` function that represents the logic for handling user requests and system recommendations. The `main` function will be structured to handle the scenarios you've described, including checking external conditions, system modes, and user preferences.
# 
# Here is the `function.py` file:

import logging
from home.sensor import get_all_sensors
from home.actuator import get_all_actuators
from home_plan import home_plan
from config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def check_outdoor_conditions():
    outdoor_sensors = get_all_sensors(home_plan(), "OutdoorTemperature")
    if outdoor_sensors:
        outdoor_temp = outdoor_sensors[0].get_reading()
        logging.info(f"Outdoor temperature is: {outdoor_temp}°C")
        return outdoor_temp
    else:
        logging.error("No outdoor temperature sensor found.")
        return None

def check_humidity():
    humidity_sensors = get_all_sensors(home_plan(), "Humidity")
    if humidity_sensors:
        humidity = humidity_sensors[0].get_reading()
        logging.info(f"Humidity is: {humidity}%")
        return humidity
    else:
        logging.error("No humidity sensor found.")
        return None

def check_light_intensity():
    light_intensity_sensors = get_all_sensors(home_plan(), "LightIntensive")
    if light_intensity_sensors:
        light_intensity = light_intensity_sensors[0].get_reading()
        logging.info(f"Light intensity is: {light_intensity} lux")
        return light_intensity
    else:
        logging.error("No light intensity sensor found.")
        return None

def user_preference_query():
    preference = input("Do you want to enable any specific features? (yes/no): ")
    return preference.lower() == 'yes'

def main():
    outdoor_temp = check_outdoor_conditions()
    humidity = check_humidity()
    light_intensity = check_light_intensity()

    if outdoor_temp is None or humidity is None or light_intensity is None:
        logging.error("Unable to get outdoor conditions, humidity, or light intensity.")
        return

    actuators = get_all_actuators(home_plan())
    for actuator in actuators:
        if isinstance(actuator, AC) or isinstance(actuator, Heater):
            if outdoor_temp > TEMP_HIGH:
                actuator.turn_on()
                logging.info(f"{actuator.id} turned on due to high outdoor temperature.")
            elif outdoor_temp < TEMP_LOW:
                actuator.turn_off()
                logging.info(f"{actuator.id} turned off due to low outdoor temperature.")
        elif isinstance(actuator, Humidifier):
            if humidity > HUMIDITY_HIGH:
                actuator.decrease_humidity()
                logging.info(f"{actuator.id} is decreasing humidity.")
            elif humidity < HUMIDITY_LOW:
                actuator.increase_humidity()
                logging.info(f"{actuator.id} is increasing humidity.")
        elif isinstance(actuator, Light):
            if light_intensity > LIGHT_INTENSITY_HIGH:
                actuator.turn_on()
                logging.info(f"{actuator.id} turned on due to high light intensity.")
            elif light_intensity < LIGHT_INTENSITY_LOW:
                actuator.turn_off()
                logging.info(f"{actuator.id} turned off due to low light intensity.")

    if user_preference_query():
        # This part of the code can be extended to handle user preferences for more complex scenarios.
        pass

if __name__ == "__main__":
    main()