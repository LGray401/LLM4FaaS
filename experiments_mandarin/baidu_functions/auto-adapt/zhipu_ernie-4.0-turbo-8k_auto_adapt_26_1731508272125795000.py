# Based on the functional description and the provided source code, here is the `function.py` file that you can use to control the temperature, humidity, and light intensity in your smart home project. This file will be located in the `functions` folder and will contain the main function to achieve the desired functionality.

# functions/function.py

from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger

def maintain_temperature(target_temperature=26):
    home = home_plan()
    
    # Get all temperature sensors and heaters/ACs
    temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    heaters = get_all_actuators(home, "Heater")
    acs = get_all_actuators(home, "AC")
    
    for sensor in temperature_sensors:
        sensor.turn_on()
        reading = sensor.get_reading()
        
        # Control heaters
        for heater in heaters:
            if reading < target_temperature:
                heater.turn_on()
                heater.set_target_temperature(target_temperature)
            else:
                heater.turn_off()
        
        # Control ACs
        for ac in acs:
            if reading > target_temperature:
                ac.turn_on()
                ac.set_target_temperature(target_temperature)
            else:
                ac.turn_off()
        
        sensor.turn_off()

def maintain_humidity(target_humidity=60):
    home = home_plan()
    
    # Get all humidity sensors and humidifiers
    humidity_sensors = get_all_sensors(home, "Humidity")
    humidifiers = get_all_actuators(home, "Humidifier")
    
    for sensor in humidity_sensors:
        sensor.turn_on()
        reading = sensor.get_reading()
        
        # Control humidifiers (assuming bidirectional control for simplicity)
        for humidifier in humidifiers:
            if reading < target_humidity:
                humidifier.increase_humidity()
            elif reading > target_humidity:
                humidifier.decrease_humidity()
        
        sensor.turn_off()

def adjust_light_intensity(activity="work"):
    home = home_plan()
    
    # Get all light intensity sensors and lights
    light_sensors = get_all_sensors(home, "LightIntensive")
    lights = get_all_actuators(home, "Light")
    
    brightness_level = "medium"  # Default level
    
    if activity == "work":
        brightness_level = "high"
    elif activity == "relax":
        brightness_level = "medium"
    elif activity == "rest":
        brightness_level = "low"
    
    for sensor in light_sensors:
        sensor.turn_on()
        reading = sensor.get_reading()
        
        # Control lights
        for light in lights:
            light.turn_on()
            light.set_brightness_level(brightness_level)
            
            # If the activity is rest, turn off the lights
            if activity == "rest":
                light.turn_off()
        
        sensor.turn_off()

def main():
    # Maintain temperature at 26 degrees Celsius
    maintain_temperature()
    
    # Maintain humidity at 60%
    maintain_humidity()
    
    # Adjust light intensity based on current activity (default to "work")
    adjust_light_intensity("work")

if __name__ == "__main__":
    main()