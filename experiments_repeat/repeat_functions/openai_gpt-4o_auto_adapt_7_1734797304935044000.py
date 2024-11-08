# Based on your functional description and the provided source code, I'll create a `function.py` file located in the `functions` folder. This file will contain a main function that simulates the smart home functionalities based on temperature, humidity, and light intensity.
# 
# Here's the implementation for `function.py`:
# 
# ```python
from home.home_plan import home_plan, get_room, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_LOW
from home.logger_config import logger

def main():
    # Create the home plan
    home = home_plan()

    # Check and react to temperature
    indoor_temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    acs = get_all_actuators(home, "AC")
    
    for sensor in indoor_temperature_sensors:
        sensor.turn_on()
        temperature = sensor.get_reading()
        if temperature is not None and temperature > TEMP_HIGH:
            logger.info(f"屋里太热了 in {sensor.room_name}. Adjusting AC...")
            for ac in acs:
                if ac.room_name == sensor.room_name:
                    ac.set_target_temperature(TEMP_HIGH)
                    ac.adjust_temperature(temperature)
        sensor.turn_off()

    # Check and react to humidity
    humidity_sensors = get_all_sensors(home, "Humidity")
    humidifiers = get_all_actuators(home, "Humidifier")

    for sensor in humidity_sensors:
        sensor.turn_on()
        humidity = sensor.get_reading()
        if humidity is not None and humidity < HUMIDITY_LOW:
            logger.info(f"屋里有点干 in {sensor.room_name}. Adjusting Humidifier...")
            for humidifier in humidifiers:
                if humidifier.room_name == sensor.room_name:
                    humidifier.turn_on()
                    humidifier.increase_humidity()
        sensor.turn_off()

    # Check and react to light intensity
    light_sensors = get_all_sensors(home, "LightIntensive")
    lights = get_all_actuators(home, "Light")

    for sensor in light_sensors:
        sensor.turn_on()
        light_intensity = sensor.get_reading()
        if light_intensity is not None and light_intensity < LIGHT_INTENSITY_LOW:
            logger.info(f"屋里太暗了 in {sensor.room_name}. Adjusting Lights...")
            for light in lights:
                if light.room_name == sensor.room_name:
                    light.turn_on()
                    light.set_brightness_level("high")
        sensor.turn_off()

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation:
# 
# 1. **Temperature Check**: The script retrieves all `IndoorTemperature` sensors and `AC` actuators. It turns on each sensor to get the temperature reading. If the temperature is above the configured `TEMP_HIGH`, it finds the corresponding `AC` in the same room and adjusts it to the target temperature.
# 
# 2. **Humidity Check**: Similar to the temperature check, it retrieves all `Humidity` sensors and `Humidifier` actuators. If the humidity is below `HUMIDITY_LOW`, it turns on the corresponding `Humidifier` in the room to increase humidity.
# 
# 3. **Light Intensity Check**: For each `LightIntensive` sensor, it checks if the light intensity is below the `LIGHT_INTENSITY_LOW`. If so, it turns on the corresponding `Light` actuators in the room and sets the brightness to high.
# 
# Each actuator and sensor is turned on and off appropriately, and actions are logged using the logger.
# 
# Please ensure that the `logger_config` is properly set up to allow logging in your environment. You may need to adjust the paths to the modules if the directory structure differs.