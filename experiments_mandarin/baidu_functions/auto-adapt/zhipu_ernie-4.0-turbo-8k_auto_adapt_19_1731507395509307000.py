# Based on your functional description and the provided source code, I will create a `function.py` file that contains the main function to control the smart home environment. This function will check the sensor readings and adjust the actuators accordingly. Specifically, it will handle scenarios related to temperature, humidity, and light intensity as described.
# 
# Here is the `function.py` file:

from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger

def adjust_smart_home():
    # Get the home plan
    home = home_plan()
    
    # Adjust temperature
    temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    heaters = get_all_actuators(home, "Heater")
    acs = get_all_actuators(home, "AC")
    
    for sensor in temperature_sensors:
        sensor.turn_on()
        reading = sensor.get_reading()
        
        # Find the corresponding heater/AC for the room
        room_heaters = [heater for heater in heaters if heater.room_name == sensor.room_name]
        room_acs = [ac for ac in acs if ac.room_name == sensor.room_name]
        
        if room_heaters and reading < TEMP_LOW:
            for heater in room_heaters:
                heater.turn_on()
                heater.set_target_temperature(TEMP_HIGH)
                heater.adjust_temperature(reading)
        elif room_acs and reading > TEMP_HIGH:
            for ac in room_acs:
                ac.turn_on()
                ac.set_target_temperature(TEMP_LOW)
                ac.adjust_temperature(reading)
        
        sensor.turn_off()
    
    # Adjust humidity
    humidity_sensors = get_all_sensors(home, "Humidity")
    humidifiers = get_all_actuators(home, "Humidifier")
    
    for sensor in humidity_sensors:
        sensor.turn_on()
        reading = sensor.get_reading()
        
        # Find the corresponding humidifier for the room
        room_humidifiers = [humidifier for humidifier in humidifiers if humidifier.room_name == sensor.room_name]
        
        if room_humidifiers:
            for humidifier in room_humidifiers:
                if reading < HUMIDITY_LOW:
                    humidifier.turn_on()
                    humidifier.increase_humidity()
                elif reading > HUMIDITY_HIGH:
                    humidifier.turn_on()
                    humidifier.decrease_humidity()
                else:
                    humidifier.turn_off()
        
        sensor.turn_off()
    
    # Adjust light intensity
    light_sensors = get_all_sensors(home, "LightIntensive")
    lights = get_all_actuators(home, "Light")
    
    for sensor in light_sensors:
        sensor.turn_on()
        reading = sensor.get_reading()
        
        # Find the corresponding lights for the room
        room_lights = [light for light in lights if light.room_name == sensor.room_name]
        
        if room_lights:
            for light in room_lights:
                if reading > LIGHT_INTENSITY_HIGH:
                    light.turn_on()
                    light.set_brightness_level("low")
                elif reading < LIGHT_INTENSITY_LOW:
                    light.turn_on()
                    light.set_brightness_level("high")
                else:
                    light.turn_off()
        
        sensor.turn_off()

if __name__ == "__main__":
    adjust_smart_home()
    logger.info("Smart home adjustment completed.")