# Based on your functional description and the provided source code, here's a `function.py` file that contains the main function to control and monitor the smart home environment. This function will specifically focus on maintaining the temperature at 23°C, humidity at a comfortable level, and light intensity at a soft level.

# functions/function.py

from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger

def maintain_comfortable_environment(home):
    # Get all relevant sensors and actuators
    temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    humidity_sensors = get_all_sensors(home, "Humidity")
    light_sensors = get_all_sensors(home, "LightIntensive")
    
    heaters = get_all_actuators(home, "Heater")
    acs = get_all_actuators(home, "AC")
    humidifiers = get_all_actuators(home, "Humidifier")
    lights = get_all_actuators(home, "Light")
    
    # Set target temperature and humidity
    target_temperature = 23
    target_humidity = (HUMIDITY_LOW + HUMIDITY_HIGH) / 2  # Midpoint of comfortable humidity range
    target_light_intensity = (LIGHT_INTENSITY_LOW + LIGHT_INTENSITY_HIGH) / 2  # Midpoint of light intensity range
    
    # Turn on all sensors
    for sensor in temperature_sensors + humidity_sensors + light_sensors:
        if sensor.get_status() == "off":
            sensor.turn_on()
    
    # Read sensor data
    temperature_readings = [sensor.get_reading() for sensor in temperature_sensors if sensor.get_reading() is not None]
    humidity_readings = [sensor.get_reading() for sensor in humidity_sensors if sensor.get_reading() is not None]
    light_readings = [sensor.get_reading() for sensor in light_sensors if sensor.get_reading() is not None]
    
    # Average the readings
    if temperature_readings:
        average_temperature = sum(temperature_readings) / len(temperature_readings)
    else:
        average_temperature = None
        
    if humidity_readings:
        average_humidity = sum(humidity_readings) / len(humidity_readings)
    else:
        average_humidity = None
        
    if light_readings:
        average_light_intensity = sum(light_readings) / len(light_readings)
    else:
        average_light_intensity = None
    
    # Adjust heaters and ACs
    if average_temperature is not None:
        for heater in heaters:
            if average_temperature < TEMP_LOW:
                heater.turn_on()
                heater.set_target_temperature(target_temperature)
            else:
                heater.turn_off()
                
        for ac in acs:
            if average_temperature > TEMP_HIGH:
                ac.turn_on()
                ac.set_target_temperature(target_temperature)
            else:
                ac.turn_off()
    
    # Adjust humidifiers
    if average_humidity is not None:
        for humidifier in humidifiers:
            if average_humidity < HUMIDITY_LOW:
                humidifier.increase_humidity()
            elif average_humidity > HUMIDITY_HIGH:
                humidifier.decrease_humidity()
    
    # Adjust lights
    if average_light_intensity is not None:
        for light in lights:
            if light.status == "on" and average_light_intensity > target_light_intensity:
                light.set_brightness_level("low")
            elif light.status == "off" or average_light_intensity < target_light_intensity:
                light.turn_on()
                light.set_brightness_level("medium")
    
    # Log the adjustments
    logger.info(f"Average Temperature: {average_temperature}, Target Temperature: {target_temperature}")
    logger.info(f"Average Humidity: {average_humidity}, Target Humidity: {target_humidity}")
    logger.info(f"Average Light Intensity: {average_light_intensity}, Target Light Intensity: {target_light_intensity}")

if __name__ == "__main__":
    # Initialize home plan
    home = home_plan()
    
    # Maintain a comfortable environment
    maintain_comfortable_environment(home)