# Based on the provided functional descriptions and source code, here's the `function.py` file that should be placed in the `functions` folder. This script will contain the main function that monitors the sensors and controls the actuators accordingly.

# functions/function.py
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger

def main():
    # Initialize the home plan
    home = home_plan()

    # Get all relevant sensors and actuators
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    humidity_sensors = get_all_sensors(home, "Humidity")
    light_sensors = get_all_sensors(home, "LightIntensive")

    ac_actuators = get_all_actuators(home, "AC")
    humidifiers = get_all_actuators(home, "Humidifier")
    curtains = get_all_actuators(home, "Curtain")

    # Turn on all sensors to start getting readings
    for sensor in indoor_temp_sensors + humidity_sensors + light_sensors:
        sensor.turn_on()

    # Loop through all relevant sensors and take actions based on their readings
    for sensor in indoor_temp_sensors:
        reading = sensor.get_reading()
        if reading is not None and reading >= TEMP_HIGH:
            logger.info(f"Indoor temperature in {sensor.room_name} is {reading}℃, turning on AC.")
            for ac in ac_actuators:
                if ac.room_name == sensor.room_name:
                    ac.turn_on()
                    ac.set_target_temperature(TEMP_HIGH - 1)

    for sensor in humidity_sensors:
        reading = sensor.get_reading()
        if reading is not None and reading < HUMIDITY_LOW:
            logger.info(f"Indoor humidity in {sensor.room_name} is {reading}%, turning on Humidifier.")
            for humidifier in humidifiers:
                if humidifier.room_name == sensor.room_name:
                    humidifier.turn_on()
                    humidifier.increase_humidity()

    for sensor in light_sensors:
        reading = sensor.get_reading()
        if reading is not None and reading > LIGHT_INTENSITY_HIGH:
            logger.info(f"Light intensity in {sensor.room_name} is {reading} lux, drawing curtains.")
            for curtain in curtains:
                if curtain.room_name == sensor.room_name:
                    curtain.turn_on()

if __name__ == "__main__":
    main()