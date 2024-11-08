# Based on your functional description of automatically adjusting indoor temperature, humidity, and light intensity, I'll create the `function.py` file. This file will include a main function that orchestrates the interaction between sensors and actuators to achieve the desired adjustments.
# 
# Here is the content of `function.py`:

# functions/function.py

from home.home_plan import home_plan, print_home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
import time

def adjust_environment(home):
    for room in home:
        # Get sensors and actuators in the room
        temperature_sensors = get_all_sensors(home, "IndoorTemperature")
        humidity_sensors = get_all_sensors(home, "Humidity")
        light_sensors = get_all_sensors(home, "LightIntensive")

        heaters = get_all_actuators(home, "Heater")
        ac_units = get_all_actuators(home, "AC")
        humidifiers = get_all_actuators(home, "Humidifier")
        lights = get_all_actuators(home, "Light")

        # Get readings from sensors
        current_temperature = sum(sensor.get_reading() for sensor in temperature_sensors) / len(temperature_sensors) if temperature_sensors else None
        current_humidity = sum(sensor.get_reading() for sensor in humidity_sensors) / len(humidity_sensors) if humidity_sensors else None
        current_light_intensity = sum(sensor.get_reading() for sensor in light_sensors) / len(light_sensors) if light_sensors else None

        # Adjust temperature
        if current_temperature is not None:
            for heater in heaters:
                heater.adjust_temperature(current_temperature)
            for ac in ac_units:
                ac.adjust_temperature(current_temperature)

        # Adjust humidity
        if current_humidity is not None:
            for humidifier in humidifiers:
                if current_humidity < HUMIDITY_LOW:
                    humidifier.increase_humidity()
                elif current_humidity > HUMIDITY_HIGH:
                    humidifier.decrease_humidity()

        # Adjust light intensity
        if current_light_intensity is not None:
            for light in lights:
                if current_light_intensity < LIGHT_INTENSITY_LOW:
                    light.turn_on()
                elif current_light_intensity > LIGHT_INTENSITY_HIGH:
                    light.turn_off()

def main():
    home = home_plan()
    print_home_plan(home)

    while True:
        adjust_environment(home)
        time.sleep(10)  # Adjust every 10 seconds

if __name__ == "__main__":
    main()