# Here's the `function.py` file based on your functional description and the provided source code files. This script will ensure that the main function maintains the temperature, humidity, and light intensity within the specified ranges:

# functions/function.py

from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, HUMIDITY_HIGH, LIGHT_INTENSITY_HIGH
from home.config import TEMP_CHANGE_DURATION_WINDOW
from time import sleep


def main():
    # Initialize home plan
    home = home_plan()

    # Get all sensors and actuators
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    humidity_sensors = get_all_sensors(home, "Humidity")
    light_sensors = get_all_sensors(home, "LightIntensive")

    ac_units = get_all_actuators(home, "AC")
    humidifiers = get_all_actuators(home, "Humidifier")
    lights = get_all_actuators(home, "Light")
    curtains = get_all_actuators(home, "Curtain")

    while True:
        # Temperature Control
        for temp_sensor in indoor_temp_sensors:
            temp_sensor.turn_on()
            temp_reading = temp_sensor.get_reading()
            if temp_reading is not None and temp_reading > TEMP_HIGH:
                for ac in ac_units:
                    if ac.room_name == temp_sensor.room_name:
                        ac.set_target_temperature(TEMP_HIGH)
                        ac.adjust_temperature(temp_reading)

        # Humidity Control
        for humidity_sensor in humidity_sensors:
            humidity_sensor.turn_on()
            humidity_reading = humidity_sensor.get_reading()
            if humidity_reading is not None and humidity_reading > HUMIDITY_HIGH:
                for humidifier in humidifiers:
                    if humidifier.room_name == humidity_sensor.room_name:
                        humidifier.decrease_humidity()

        # Light Intensity Control
        for light_sensor in light_sensors:
            light_sensor.turn_on()
            light_reading = light_sensor.get_reading()
            if light_reading is not None:
                if light_reading > LIGHT_INTENSITY_HIGH:
                    for curtain in curtains:
                        if curtain.room_name == light_sensor.room_name:
                            curtain.turn_on()
                elif light_reading < LIGHT_INTENSITY_HIGH:
                    for light in lights:
                        if light.room_name == light_sensor.room_name:
                            light.turn_on()
                            light.set_brightness_level("high")

        # Wait for a while before the next check
        sleep(TEMP_CHANGE_DURATION_WINDOW)


if __name__ == "__main__":
    main()