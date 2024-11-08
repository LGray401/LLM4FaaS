# Based on your functional description and the provided source code, I will create a `function.py` file that contains the main function to control the smart home environment. This main function will focus on maintaining the temperature at 22°C, humidity at a moderate level, and light intensity at a low level.
# 
# Here's the `function.py` file:

from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.sensor import Sensor
from home.actuator import Actuator, Heater, AC, Humidifier, Light
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def maintain_optimal_conditions(home):
    # Get all relevant sensors and actuators
    temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    humidity_sensors = get_all_sensors(home, "Humidity")
    light_sensors = get_all_sensors(home, "LightIntensive")
    
    heaters = get_all_actuators(home, "Heater")
    acs = get_all_actuators(home, "AC")
    humidifiers = get_all_actuators(home, "Humidifier")
    lights = get_all_actuators(home, "Light")
    
    # Set target values
    target_temperature = 22
    target_humidity = (HUMIDITY_LOW + HUMIDITY_HIGH) / 2  # Moderate humidity
    target_light_intensity = LIGHT_INTENSITY_LOW  # Low light intensity
    
    # Turn on all sensors
    for sensor in temperature_sensors + humidity_sensors + light_sensors:
        if sensor.get_status() == "off":
            sensor.turn_on()
    
    # Adjust temperature
    for sensor, actuator in zip(temperature_sensors, heaters + acs):
        reading = sensor.get_reading()
        if reading is not None:
            if reading < target_temperature:
                if isinstance(actuator, Heater):
                    actuator.turn_on()
                    actuator.set_target_temperature(target_temperature)
                    actuator.adjust_temperature(reading)
                elif isinstance(actuator, AC):
                    actuator.turn_off()
            else:
                if isinstance(actuator, AC):
                    actuator.turn_on()
                    actuator.set_target_temperature(target_temperature)
                    actuator.adjust_temperature(reading)
                elif isinstance(actuator, Heater):
                    actuator.turn_off()
    
    # Adjust humidity
    for sensor, actuator in zip(humidity_sensors, humidifiers):
        reading = sensor.get_reading()
        if reading is not None:
            if reading < target_humidity:
                actuator.increase_humidity()
            else:
                actuator.decrease_humidity()
    
    # Adjust light intensity
    for sensor, actuator in zip(light_sensors, lights):
        reading = sensor.get_reading()
        if reading is not None:
            if reading > target_light_intensity:
                # Assuming light intensity can be adjusted, set to low brightness level
                actuator.set_brightness_level("low")
            else:
                # Keep the current setting or adjust as necessary
                pass
    
    # Turn off sensors to save energy
    for sensor in temperature_sensors + humidity_sensors + light_sensors:
        sensor.turn_off()

def main():
    # Initialize the home plan
    home = home_plan()
    
    # Maintain optimal conditions
    maintain_optimal_conditions(home)

if __name__ == "__main__":
    main()