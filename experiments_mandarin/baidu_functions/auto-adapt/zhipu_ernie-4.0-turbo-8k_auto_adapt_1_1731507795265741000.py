# Based on your functional description and the provided source code, I will now provide a `function.py` file that contains the main function to adjust the temperature, humidity, and light intensity in your smart home project.
# 
# ### function.py

from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger

def adjust_temperature(target_temperature, home):
    heaters = get_all_actuators(home, "Heater")
    acs = get_all_actuators(home, "AC")
    
    for heater in heaters:
        heater.set_target_temperature(target_temperature)
    
    for ac in acs:
        ac.set_target_temperature(target_temperature)
    
    # Get indoor temperature sensors
    temp_sensors = get_all_sensors(home, "IndoorTemperature")
    
    for sensor in temp_sensors:
        sensor.turn_on()
        current_temp = sensor.get_reading()
        
        # Adjust heater/AC based on current temperature
        if heater.room_name == sensor.room_name:
            heater.adjust_temperature(current_temp)
        elif ac.room_name == sensor.room_name:
            ac.adjust_temperature(current_temp)
        
        sensor.turn_off()  # Turn off sensor after use to save energy

def adjust_humidity(target_humidity, home):
    humidifiers = get_all_actuators(home, "Humidifier")
    
    # Assuming we have a way to decrease humidity if needed, for simplicity, let's use the same actuator
    dehumidifiers = humidifiers  # In reality, you might have separate devices
    
    humidity_sensors = get_all_sensors(home, "Humidity")
    
    for sensor in humidity_sensors:
        sensor.turn_on()
        current_humidity = sensor.get_reading()
        
        for humidifier in humidifiers:
            if humidifier.room_name == sensor.room_name:
                if current_humidity < target_humidity:
                    humidifier.increase_humidity()
                else:
                    # For simplicity, using the same function to represent decreasing humidity
                    humidifier.decrease_humidity()
        
        sensor.turn_off()  # Turn off sensor after use to save energy

def adjust_light_intensity(light_level, home):
    lights = get_all_actuators(home, "Light")
    
    for light in lights:
        light.set_brightness_level(light_level)

def main():
    # Initialize the home plan
    home = home_plan()
    
    # Adjust temperature to 26°
    adjust_temperature(26, home)
    
    # Adjust humidity to 40%
    adjust_humidity(40, home)
    
    # Adjust light intensity to medium
    adjust_light_intensity("medium", home)
    
    logger.info("Adjustments have been made to temperature, humidity, and light intensity.")

if __name__ == "__main__":
    main()