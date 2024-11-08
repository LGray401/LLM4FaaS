# Based on your functional description and the provided source code, I will create a `function.py` file that contains the main function to handle temperature, humidity, and light intensity checks, and perform actions accordingly. This file will be located in the `functions` folder.
# 
# Here is the `function.py` file:

from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW
from home.logger_config import logger

def check_and_adjust_temperature(room_name):
    home = home_plan()
    heaters = get_all_actuators(home, "Heater")
    acs = get_all_actuators(home, "AC")
    temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    
    for sensor in temperature_sensors:
        if sensor.room_name == room_name:
            sensor.turn_on()
            temp = sensor.get_reading()
            
            # Adjust heaters
            for heater in heaters:
                if heater.room_name == room_name:
                    heater.set_target_temperature(TEMP_HIGH - 1)  # Set slightly lower than high threshold for comfort
                    heater.adjust_temperature(temp)
            
            # Adjust ACs
            for ac in acs:
                if ac.room_name == room_name:
                    ac.set_target_temperature(TEMP_LOW + 1)  # Set slightly higher than low threshold for comfort
                    ac.adjust_temperature(temp)
            
            sensor.turn_off()
            break  # Assuming only one temperature sensor per room for this example

def check_and_adjust_humidity(room_name):
    home = home_plan()
    humidifiers = get_all_actuators(home, "Humidifier")
    humidity_sensors = get_all_sensors(home, "Humidity")
    
    for sensor in humidity_sensors:
        if sensor.room_name == room_name:
            sensor.turn_on()
            humidity = sensor.get_reading()
            
            # Adjust humidifiers
            for humidifier in humidifiers:
                if humidifier.room_name == room_name:
                    if humidity < HUMIDITY_LOW:
                        humidifier.increase_humidity()
                    elif humidity > HUMIDITY_HIGH:
                        humidifier.decrease_humidity()
            
            sensor.turn_off()
            break  # Assuming only one humidity sensor per room for this example

def check_and_adjust_light_intensity(room_name):
    home = home_plan()
    lights = get_all_actuators(home, "Light")
    light_sensors = get_all_sensors(home, "LightIntensive")
    
    for sensor in light_sensors:
        if sensor.room_name == room_name:
            sensor.turn_on()
            light_intensity = sensor.get_reading()
            
            # Adjust lights
            for light in lights:
                if light.room_name == room_name:
                    if light_intensity < LIGHT_INTENSITY_LOW:
                        light.turn_on()
                        light.set_brightness_level("high")
                    else:
                        light.turn_off()  # Or adjust to a lower brightness level if desired
            
            sensor.turn_off()
            break  # Assuming only one light sensor per room for this example

def main():
    room_name = "LivingRoom"  # Example room, can be changed or taken as input
    
    # Check and adjust temperature
    check_and_adjust_temperature(room_name)
    
    # Check and adjust humidity
    check_and_adjust_humidity(room_name)
    
    # Check and adjust light intensity
    check_and_adjust_light_intensity(room_name)

if __name__ == "__main__":
    main()
    logger.info("Main function executed")