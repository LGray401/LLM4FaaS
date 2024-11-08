# Sure, here is the 'function.py' file based on your given functional description:

import time
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_LOW


def main():
    # Get the home plan
    home = home_plan()

    # Get all the sensors
    temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    humidity_sensors = get_all_sensors(home, "Humidity")
    light_sensors = get_all_sensors(home, "LightIntensive")

    # Get all the actuators
    heaters = get_all_actuators(home, "Heater")
    humidifiers = get_all_actuators(home, "Humidifier")
    lights = get_all_actuators(home, "Light")

    while True:
        # Check temperature
        for sensor in temperature_sensors:
            temperature = sensor.get_reading()
            if temperature > TEMP_HIGH:
                for heater in heaters:
                    heater.turn_on()
            else:
                for heater in heaters:
                    heater.turn_off()

        # Check humidity
        for sensor in humidity_sensors:
            humidity = sensor.get_reading()
            if humidity < HUMIDITY_LOW:
                for humidifier in humidifiers:
                    humidifier.increase_humidity()
            else:
                for humidifier in humidifiers:
                    humidifier.decrease_humidity()

        # Check light intensity
        for sensor in light_sensors:
            light_intensity = sensor.get_reading()
            if light_intensity < LIGHT_INTENSITY_LOW:
                for light in lights:
                    light.turn_on()
            else:
                for light in lights:
                    light.turn_off()

        # Sleep for 1 minute before checking again
        time.sleep(60)


if __name__ == "__main__":
    main()