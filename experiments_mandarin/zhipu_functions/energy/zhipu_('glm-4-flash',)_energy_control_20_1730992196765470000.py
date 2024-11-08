# Based on the provided functional description and source code, here's the `function.py` file located in the `functions` folder. This file will contain the main function to automatically regulate indoor temperature, humidity, and light intensity:

# function.py
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, AC, Humidifier, Light
from home.logger_config import logger

# Constants from config.py
TEMP_CHANGE_DURATION_WINDOW = 1
TEMP_LOW = 15
TEMP_HIGH = 25
HUMIDITY_LOW = 30
HUMIDITY_HIGH = 50
LIGHT_INTENSITY_LOW = 300
LIGHT_INTENSITY_HIGH = 900

def main():
    logger.info("Starting smart home automation.")

    # Create a home plan
    home = home_plan()

    # Fetch all sensors and actuators
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    humidity_sensors = get_all_sensors(home, "Humidity")
    light_intensity_sensors = get_all_sensors(home, "LightIntensive")
    heaters = get_all_actuators(home, "Heater")
    acs = get_all_actuators(home, "AC")
    humidifiers = get_all_actuators(home, "Humidifier")
    lights = get_all_actuators(home, "Light")

    try:
        while True:
            # Read sensor values
            for sensor in indoor_temp_sensors:
                temp = sensor.get_reading()
                if temp is not None:
                    logger.info(f"Current indoor temperature: {temp}°C in {sensor.room_name}")

            for sensor in humidity_sensors:
                humidity = sensor.get_reading()
                if humidity is not None:
                    logger.info(f"Current humidity: {humidity}% in {sensor.room_name}")

            for sensor in light_intensity_sensors:
                light_intensity = sensor.get_reading()
                if light_intensity is not None:
                    logger.info(f"Current light intensity: {light_intensity} lux in {sensor.room_name}")

            # Adjust actuators based on sensor readings
            for sensor, heater in zip(indoor_temp_sensors, heaters):
                current_temp = sensor.get_reading()
                if current_temp is not None:
                    if current_temp < TEMP_LOW:
                        heater.turn_on()
                    elif current_temp > TEMP_HIGH:
                        heater.turn_off()

            for sensor, ac in zip(indoor_temp_sensors, acs):
                current_temp = sensor.get_reading()
                if current_temp is not None:
                    if current_temp < TEMP_LOW:
                        ac.turn_on()
                    elif current_temp > TEMP_HIGH:
                        ac.turn_off()

            for sensor, humidifier in zip(humidity_sensors, humidifiers):
                humidity = sensor.get_reading()
                if humidity is not None:
                    if humidity < HUMIDITY_LOW:
                        humidifier.increase_humidity()
                    elif humidity > HUMIDITY_HIGH:
                        humidifier.decrease_humidity()

            for sensor, light in zip(light_intensity_sensors, lights):
                light_intensity = sensor.get_reading()
                if light_intensity is not None:
                    if light_intensity < LIGHT_INTENSITY_LOW:
                        light.set_brightness_level("high")
                    elif light_intensity > LIGHT_INTENSITY_HIGH:
                        light.set_brightness_level("low")

            # Wait for a while before checking again
            time.sleep(TEMP_CHANGE_DURATION_WINDOW)

    except KeyboardInterrupt:
        logger.info("Smart home automation stopped by user.")

if __name__ == "__main__":
    main()