# Based on the functional description you provided, we need to read temperature, humidity, and light intensity from sensors and perform some actions based on these readings. We can assume that you want to keep the temperature around 26°C, humidity around 50%, and ensure the light level is appropriate.
# 
# Below is the implementation of `function.py` located in the `functions` folder. This file contains the main function which will orchestrate reading from sensors and controlling actuators to maintain the desired conditions.
# 
# ```python
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, TEMP_LOW, HUMIDITY_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    # Create the home plan
    home = home_plan()
    
    # Get all the sensors
    temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    humidity_sensors = get_all_sensors(home, "Humidity")
    light_sensors = get_all_sensors(home, "LightIntensive")

    # Get all the actuators
    heaters = get_all_actuators(home, "Heater")
    acs = get_all_actuators(home, "AC")
    humidifiers = get_all_actuators(home, "Humidifier")
    lights = get_all_actuators(home, "Light")
    
    # Monitor and control temperature
    for sensor in temperature_sensors:
        sensor.turn_on()
        current_temperature = sensor.get_reading()
        
        for heater in heaters:
            heater.set_target_temperature(TEMP_HIGH)
            heater.adjust_temperature(current_temperature)
        
        for ac in acs:
            ac.set_target_temperature(TEMP_LOW)
            ac.adjust_temperature(current_temperature)

    # Monitor and control humidity
    for sensor in humidity_sensors:
        sensor.turn_on()
        current_humidity = sensor.get_reading()
        
        for humidifier in humidifiers:
            if current_humidity < HUMIDITY_LOW:
                humidifier.turn_on()
            elif current_humidity > HUMIDITY_HIGH:
                humidifier.turn_off()

    # Monitor and control light intensity
    for sensor in light_sensors:
        sensor.turn_on()
        current_light_intensity = sensor.get_reading()

        for light in lights:
            if current_light_intensity < LIGHT_INTENSITY_LOW:
                light.turn_on()
                light.set_brightness_level("medium")
            elif current_light_intensity > LIGHT_INTENSITY_HIGH:
                light.turn_off()
    
    # Turn off all sensors after use
    for sensor in temperature_sensors + humidity_sensors + light_sensors:
        sensor.turn_off()

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation
# 
# 1. **Temperature Control**: The code checks the current temperature from the `IndoorTemperature` sensors and uses heaters and ACs to maintain the temperature between the specified low and high thresholds.
# 
# 2. **Humidity Control**: The code checks the current humidity level and adjusts humidifiers to keep the humidity within the specified range.
# 
# 3. **Light Control**: The code uses light sensors to check the light intensity and adjusts the brightness of lights accordingly.
# 
# 4. **Actuator Management**: The code ensures that actuators are only turned on when necessary to save energy.
# 
# 5. **Sensor Management**: Sensors are turned on to get readings and turned off when not in use to simulate a real-world scenario of power management.
# 
# This implementation assumes that the sensor readings and actuator adjustments are instantaneous, which is typical for a simulation. In a real-world application, you would need to handle delays and asynchronous events.