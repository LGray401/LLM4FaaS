# Based on your provided functional description and the existing source code files, I'll create a `function.py` file that will be located in the `functions` folder. This file will include the main function, which will initialize the home plan and control the sensors and actuators according to the specified conditions: Temperature of 26 degrees, Humidity of 50, and Moderate light.
# 
# Here is the content of the `function.py` file:
# 
# ### function.py

from home.home_plan import home_plan, get_all_actuators, get_all_sensors
from home.config import TEMP_HIGH, TEMP_LOW, HUMIDITY_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_HIGH, LIGHT_INTENSITY_LOW

def main():
    home = home_plan()

    # Set temperature, humidity, and light intensity to the specified values
    desired_temperature = 26
    desired_humidity = 50
    desired_light_intensity = 'medium'  # Assuming medium corresponds to moderate light

    # Control temperature using AC and Heater
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    for sensor in indoor_temp_sensors:
        sensor.turn_on()
        current_temp = sensor.get_reading()
        heaters = get_all_actuators(home, "Heater")
        acs = get_all_actuators(home, "AC")
        for heater in heaters:
            heater.set_target_temperature(desired_temperature)
            heater.adjust_temperature(current_temp)
        for ac in acs:
            ac.set_target_temperature(desired_temperature)
            ac.adjust_temperature(current_temp)

    # Control humidity using Humidifier
    humidity_sensors = get_all_sensors(home, "Humidity")
    for sensor in humidity_sensors:
        sensor.turn_on()
        current_humidity = sensor.get_reading()
        humidifiers = get_all_actuators(home, "Humidifier")
        for humidifier in humidifiers:
            if current_humidity < desired_humidity:
                humidifier.turn_on()
                humidifier.increase_humidity()
            elif current_humidity > desired_humidity:
                humidifier.turn_on()
                humidifier.decrease_humidity()
            else:
                humidifier.turn_off()

    # Control light intensity using Light
    light_sensors = get_all_sensors(home, "LightIntensive")
    for sensor in light_sensors:
        sensor.turn_on()
        current_light_intensity = sensor.get_reading()
        lights = get_all_actuators(home, "Light")
        for light in lights:
            light.turn_on()
            light.set_brightness_level(desired_light_intensity)

if __name__ == "__main__":
    main()