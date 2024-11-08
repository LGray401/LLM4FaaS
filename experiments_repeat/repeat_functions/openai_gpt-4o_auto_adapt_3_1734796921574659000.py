# To create a `function.py` file for your smart home project, we can implement a main function that interacts with the existing components (sensors and actuators) based on the functional description you provided. The description specifies optimal parameters for temperature, humidity, and light intensity, so we can create a main function to manage these aspects in a smart home environment.
# 
# Here's an outline of what the `function.py` file might look like:
# 
# ```python
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, AC, Humidifier, Light
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, TEMP_LOW, HUMIDITY_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_HIGH, LIGHT_INTENSITY_LOW

def main():
    # Initialize the home plan
    home = home_plan()

    # Get all relevant sensors
    temp_sensors = get_all_sensors(home, "IndoorTemperature")
    humidity_sensors = get_all_sensors(home, "Humidity")
    light_sensors = get_all_sensors(home, "LightIntensive")

    # Get all relevant actuators
    heaters = get_all_actuators(home, "Heater")
    ac_units = get_all_actuators(home, "AC")
    humidifiers = get_all_actuators(home, "Humidifier")
    lights = get_all_actuators(home, "Light")

    # Desired values based on functional description
    desired_temp = 26  # Celsius
    desired_humidity = 50  # percentage
    desired_light_intensity = (LIGHT_INTENSITY_HIGH + LIGHT_INTENSITY_LOW) / 2  # Assuming medium is the average

    # Adjust temperature
    for sensor in temp_sensors:
        sensor.turn_on()
        current_temp = sensor.get_reading()
        for heater in heaters:
            heater.set_target_temperature(desired_temp)
            heater.adjust_temperature(current_temp)
        for ac in ac_units:
            ac.set_target_temperature(desired_temp)
            ac.adjust_temperature(current_temp)

    # Adjust humidity
    for sensor in humidity_sensors:
        sensor.turn_on()
        current_humidity = sensor.get_reading()
        for humidifier in humidifiers:
            if current_humidity < desired_humidity:
                humidifier.turn_on()
                humidifier.increase_humidity()
            else:
                humidifier.turn_off()
                humidifier.decrease_humidity()

    # Adjust light intensity
    for sensor in light_sensors:
        sensor.turn_on()
        current_light = sensor.get_reading()
        for light in lights:
            if current_light < desired_light_intensity:
                light.turn_on()
                light.set_brightness_level("medium")
            else:
                light.turn_off()

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation:
# - **Temperature Control**: This script checks each indoor temperature sensor's reading and adjusts heaters and AC units to maintain the desired temperature of 26°C.
# - **Humidity Control**: Humidifiers are used to adjust the humidity level to the desired 50%.
# - **Light Control**: Light actuators are adjusted based on the light intensity reading to maintain a medium level of brightness.
# 
# This script assumes the presence of a `Humidifier` actuator in the home plan, which was not present in the original code. You might need to ensure that the home plan includes this actuator or modify the script to fit the actual devices you have.
# 
# Please make sure that all the components in the `home_plan.py` and `config.py` files are properly defined and accessible from the `function.py` for this script to work correctly.