# Sure! Based on your functional description and the provided source code, I will create a `function.py` file that will contain the main function to manage your smart home project. This function will initialize the home plan, check the sensors, and control the actuators based on the given conditions.
# 
# Here's the `function.py` file:

# functions/function.py

from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, TEMP_LOW, HUMIDITY_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    # Initialize the home plan
    home = home_plan()

    # Get all sensors of each type
    temp_sensors = get_all_sensors(home, "IndoorTemperature")
    humidity_sensors = get_all_sensors(home, "Humidity")
    light_sensors = get_all_sensors(home, "LightIntensive")

    # Get all actuators of each type
    heaters = get_all_actuators(home, "Heater")
    humidifiers = get_all_actuators(home, "Humidifier")
    lights = get_all_actuators(home, "Light")

    # Turn on all sensors
    for sensor in temp_sensors + humidity_sensors + light_sensors:
        sensor.turn_on()

    # Read all sensor values and adjust actuators accordingly
    for sensor in temp_sensors:
        temp = sensor.get_reading()
        if temp is not None:
            for heater in heaters:
                heater.set_target_temperature(TEMP_HIGH if temp < TEMP_LOW else TEMP_LOW)
                heater.adjust_temperature(temp)

    for sensor in humidity_sensors:
        humidity = sensor.get_reading()
        if humidity is not None:
            for humidifier in humidifiers:
                if humidity < HUMIDITY_LOW:
                    humidifier.turn_on()
                elif humidity > HUMIDITY_HIGH:
                    humidifier.turn_off()

    for sensor in light_sensors:
        light_intensity = sensor.get_reading()
        if light_intensity is not None:
            for light in lights:
                if light_intensity < LIGHT_INTENSITY_LOW:
                    light.turn_on()
                    light.set_brightness_level("high")
                elif light_intensity > LIGHT_INTENSITY_HIGH:
                    light.turn_off()

    # Turn off all sensors
    for sensor in temp_sensors + humidity_sensors + light_sensors:
        sensor.turn_off()

if __name__ == "__main__":
    main()