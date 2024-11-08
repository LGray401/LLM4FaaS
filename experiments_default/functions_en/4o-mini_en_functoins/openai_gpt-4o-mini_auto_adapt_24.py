# Here is the `function.py` file that meets your functional description. This script will maintain the indoor temperature below 26 degrees, keep humidity below 30%, and manage light intensity by checking the current readings from the sensors and adjusting the actuators accordingly.
# 
# Please ensure that the `functions` folder exists in your project structure where this file will be saved.

# functions/function.py

from home.home_plan import home_plan
from home.config import TEMP_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_LOW
from home.actuator import Heater, AC, Humidifier, Light
from home.logger_config import logger

def main():
    # Create the home setup
    home = home_plan()

    # Iterate through each room to manage the environment
    for room in home:
        # Get necessary sensors and actuators
        temperature_sensor = next((sensor for sensor in room.sensors if sensor.sensor_type == "IndoorTemperature"), None)
        humidity_sensor = next((sensor for sensor in room.sensors if sensor.sensor_type == "Humidity"), None)
        light_sensor = next((sensor for sensor in room.sensors if sensor.sensor_type == "LightIntensive"), None)
        
        heater = next((actuator for actuator in room.actuators if isinstance(actuator, Heater)), None)
        ac = next((actuator for actuator in room.actuators if isinstance(actuator, AC)), None)
        humidifier = next((actuator for actuator in room.actuators if isinstance(actuator, Humidifier)), None)
        light = next((actuator for actuator in room.actuators if isinstance(actuator, Light)), None)

        # Maintain indoor temperature
        if temperature_sensor:
            current_temp = temperature_sensor.get_reading()
            if current_temp is not None:
                if current_temp > TEMP_HIGH:
                    if ac:
                        ac.set_target_temperature(TEMP_HIGH)
                        ac.adjust_temperature(current_temp)
                elif heater:
                    heater.turn_off()  # Turn off heater if temperature is okay

        # Maintain humidity
        if humidity_sensor:
            current_humidity = humidity_sensor.get_reading()
            if current_humidity is not None:
                if current_humidity > HUMIDITY_LOW:
                    if humidifier:
                        humidifier.decrease_humidity()  # Assume humidifier can decrease humidity
                else:
                    if humidifier:
                        humidifier.turn_off()  # Turn off humidifier if humidity is okay

        # Manage Light Intensity
        if light_sensor and light:
            current_light_intensity = light_sensor.get_reading()
            if current_light_intensity is not None:
                if current_light_intensity < LIGHT_INTENSITY_LOW:
                    light.turn_on()
                else:
                    light.turn_off()

if __name__ == "__main__":
    main()