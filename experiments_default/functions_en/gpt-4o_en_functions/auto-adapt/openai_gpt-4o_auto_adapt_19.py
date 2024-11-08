# Based on the provided functional description and the source code files, I'll create a `function.py` file located in the `functions` folder. This file will contain the main function to monitor and control the smart home environment based on temperature, humidity, and light intensity. The functional description given indicates the need to handle conditions where it is too hot, too dry, or too bright.
# 
# Here is the `function.py` file:

# functions/function.py
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC, Heater, Humidifier, Light
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    home = home_plan()

    # Turn on all sensors
    all_sensors = get_all_sensors(home, "IndoorTemperature") + get_all_sensors(home, "Humidity") + get_all_sensors(home, "LightIntensive")
    for sensor in all_sensors:
        sensor.turn_on()

    # Check Temperature
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    for sensor in indoor_temp_sensors:
        reading = sensor.get_reading()
        if reading and reading > TEMP_HIGH:
            # Turn on AC to cool down
            acs = get_all_actuators(home, "AC")
            for ac in acs:
                ac.set_target_temperature(TEMP_HIGH)
                ac.adjust_temperature(reading)

    # Check Humidity
    humidity_sensors = get_all_sensors(home, "Humidity")
    for sensor in humidity_sensors:
        reading = sensor.get_reading()
        if reading and reading < HUMIDITY_LOW:
            # Turn on Humidifier to increase humidity
            humidifiers = get_all_actuators(home, "Humidifier")
            for humidifier in humidifiers:
                humidifier.increase_humidity()

    # Check Light Intensity
    light_sensors = get_all_sensors(home, "LightIntensive")
    for sensor in light_sensors:
        reading = sensor.get_reading()
        if reading and reading > LIGHT_INTENSITY_HIGH:
            # Adjust lights to reduce brightness
            lights = get_all_actuators(home, "Light")
            for light in lights:
                light.turn_on()
                light.set_brightness_level("low")

if __name__ == "__main__":
    main()