# Based on your functional description and the provided source code, I will create a `function.py` file that contains the main function for automatically adjusting the indoor temperature, humidity, and light intensity in your smart home project. This main function will utilize the classes and methods defined in the `sensor.py`, `actuator.py`, and `home_plan.py` files.
# 
# Here is the `function.py` file:

from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger

def adjust_temperature(actuators, current_temp):
    for actuator in actuators:
        if actuator.actuator_type == "Heater":
            actuator.adjust_temperature(current_temp)
        elif actuator.actuator_type == "AC":
            actuator.adjust_temperature(current_temp)

def adjust_humidity(actuators, current_humidity):
    for actuator in actuators:
        if actuator.actuator_type == "Humidifier":
            if current_humidity < HUMIDITY_LOW:
                actuator.increase_humidity()
            elif current_humidity > HUMIDITY_HIGH:
                actuator.decrease_humidity()

def adjust_light_intensity(actuators, current_intensity):
    for actuator in actuators:
        if actuator.actuator_type == "Light":
            if current_intensity < LIGHT_INTENSITY_LOW:
                actuator.set_brightness_level("high")  # or appropriate logic to increase intensity
            elif current_intensity > LIGHT_INTENSITY_HIGH:
                actuator.set_brightness_level("low")  # or appropriate logic to decrease intensity

def main():
    # Initialize the home plan
    home = home_plan()
    
    # Get all relevant sensors and actuators
    temp_sensors = get_all_sensors(home, "IndoorTemperature")
    humidity_sensors = get_all_sensors(home, "Humidity")
    light_sensors = get_all_sensors(home, "LightIntensive")
    
    heaters = get_all_actuators(home, "Heater")
    acs = get_all_actuators(home, "AC")
    humidifiers = get_all_actuators(home, "Humidifier")
    lights = get_all_actuators(home, "Light")
    
    # Turn on all sensors
    for sensor in temp_sensors + humidity_sensors + light_sensors:
        sensor.turn_on()
    
    # Read sensor data and adjust accordingly
    for room in home:
        # Assuming each room has one of each sensor type for simplicity
        for sensor in room.sensors:
            if sensor.sensor_type == "IndoorTemperature":
                current_temp = sensor.get_reading()
                adjust_temperature(room.actuators, current_temp)
            elif sensor.sensor_type == "Humidity":
                current_humidity = sensor.get_reading()
                adjust_humidity(room.actuators, current_humidity)
            elif sensor.sensor_type == "LightIntensive":
                current_intensity = sensor.get_reading()
                adjust_light_intensity(room.actuators, current_intensity)
    
    # Turn off all sensors to save energy
    for sensor in temp_sensors + humidity_sensors + light_sensors:
        sensor.turn_off()

if __name__ == "__main__":
    main()