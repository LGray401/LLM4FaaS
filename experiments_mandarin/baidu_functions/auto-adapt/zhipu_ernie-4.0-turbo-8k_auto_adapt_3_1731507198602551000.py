# Based on your functional description and the provided source code, I will create a `function.py` file that contains the main function to control the smart home environment. This main function will focus on maintaining the temperature at 26 degrees, humidity at 50%, and light intensity at a moderate level.
# 
# Here is the `function.py` file:

from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, TEMP_LOW, HUMIDITY_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger

def adjust_temperature(sensors, actuators):
    # Get the current temperature readings
    for sensor in sensors:
        if sensor.sensor_type == "IndoorTemperature":
            current_temp = sensor.get_reading()
            # Adjust heaters and ACs based on the current temperature
            for actuator in actuators:
                if actuator.actuator_type == "Heater":
                    if current_temp < 26:
                        actuator.turn_on()
                    else:
                        actuator.turn_off()
                elif actuator.actuator_type == "AC":
                    if current_temp > 26:
                        actuator.turn_on()
                    else:
                        actuator.turn_off()

def adjust_humidity(sensors, actuators):
    # Get the current humidity readings
    for sensor in sensors:
        if sensor.sensor_type == "Humidity":
            current_humidity = sensor.get_reading()
            # Adjust humidifiers based on the current humidity
            for actuator in actuators:
                if actuator.actuator_type == "Humidifier":
                    if current_humidity < 50:
                        actuator.increase_humidity()
                    elif current_humidity > 50:
                        actuator.decrease_humidity()

def adjust_light_intensity(sensors, actuators):
    # Get the current light intensity readings
    for sensor in sensors:
        if sensor.sensor_type == "LightIntensive":
            current_light = sensor.get_reading()
            # Adjust lights based on the current light intensity
            for actuator in actuators:
                if actuator.actuator_type == "Light":
                    if current_light < (LIGHT_INTENSITY_LOW + (LIGHT_INTENSITY_HIGH - LIGHT_INTENSITY_LOW) / 2):  # Moderate level
                        actuator.turn_on()
                        actuator.set_brightness_level("medium")
                    else:
                        actuator.turn_off()

def main():
    # Initialize the home plan
    home = home_plan()
    
    # Get all sensors and actuators
    temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    humidity_sensors = get_all_sensors(home, "Humidity")
    light_sensors = get_all_sensors(home, "LightIntensive")
    
    actuators = []
    for room in home:
        actuators.extend(room.actuators)
    
    # Turn on all sensors
    for sensor in temperature_sensors + humidity_sensors + light_sensors:
        sensor.turn_on()
    
    # Adjust the smart home environment
    while True:
        adjust_temperature(temperature_sensors, actuators)
        adjust_humidity(humidity_sensors, actuators)
        adjust_light_intensity(light_sensors, actuators)
        
        # Sleep for a while before checking again
        # This sleep duration can be adjusted based on how frequently you want to check the sensors
        # For this example, let's check every 10 seconds
        import time
        time.sleep(10)

if __name__ == "__main__":
    main()