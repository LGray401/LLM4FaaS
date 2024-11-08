# Based on your functional description and the provided source code, here's the `function.py` file that you can use to control your smart home environment. This file will be located in the `functions` folder and will contain the main functions to handle temperature, humidity, and light intensity.
# 
# ### function.py

from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.config import TEMP_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger

def check_and_adjust_temperature(room_name):
    rooms = home_plan()
    sensors = get_room_sensors(rooms, room_name)
    actuators = get_room_actuators(rooms, room_name)
    
    if sensors:
        for sensor in sensors:
            if sensor.sensor_type == "IndoorTemperature":
                sensor.turn_on()
                temperature = sensor.get_reading()
                sensor.turn_off()
                
                # Adjust AC and Heater accordingly
                for actuator in actuators:
                    if actuator.actuator_type == "AC" and temperature > TEMP_HIGH:
                        actuator.turn_on()  # Turn on AC
                        logger.info(f"Turned on AC in {room_name} due to high temperature: {temperature}°C")
                    elif actuator.actuator_type == "Heater" and temperature < TEMP_HIGH:
                        actuator.turn_off()  # Ensure heater is off
                        
                    elif actuator.actuator_type == "Heater" and temperature < TEMP_LOW:
                        actuator.turn_on()  # Turn on Heater
                        logger.info(f"Turned on Heater in {room_name} due to low temperature: {temperature}°C")
                    elif actuator.actuator_type == "AC" and temperature >= TEMP_LOW:
                        actuator.turn_off()  # Ensure AC is off
                        
                    # Close windows if AC or Heater is on
                    if actuator.actuator_type == "Window" and (temperature > TEMP_HIGH or temperature < TEMP_LOW):
                        actuator.turn_off()  # Close window
                        logger.info(f"Closed window in {room_name} to adjust temperature")

def check_and_adjust_humidity(room_name):
    rooms = home_plan()
    sensors = get_room_sensors(rooms, room_name)
    actuators = get_room_actuators(rooms, room_name)
    
    if sensors:
        for sensor in sensors:
            if sensor.sensor_type == "Humidity":
                sensor.turn_on()
                humidity = sensor.get_reading()
                sensor.turn_off()
                
                for actuator in actuators:
                    if actuator.actuator_type == "Humidifier" and humidity < HUMIDITY_LOW:
                        actuator.turn_on()  # Turn on Humidifier
                        logger.info(f"Turned on Humidifier in {room_name} due to low humidity: {humidity}%")
                    elif actuator.actuator_type == "Humidifier" and humidity >= HUMIDITY_LOW:
                        actuator.turn_off()  # Ensure Humidifier is off if humidity is fine

def check_and_adjust_light_intensity(room_name):
    rooms = home_plan()
    sensors = get_room_sensors(rooms, room_name)
    actuators = get_room_actuators(rooms, room_name)
    
    if sensors:
        for sensor in sensors:
            if sensor.sensor_type == "LightIntensive":
                sensor.turn_on()
                light_intensity = sensor.get_reading()
                sensor.turn_off()
                
                for actuator in actuators:
                    if actuator.actuator_type == "Light":
                        if light_intensity < LIGHT_INTENSITY_LOW:
                            actuator.turn_on()  # Turn on light
                            actuator.set_brightness_level("high")
                            logger.info(f"Turned on light in {room_name} due to low light intensity: {light_intensity} lux")
                        elif light_intensity > LIGHT_INTENSITY_HIGH:
                            actuator.turn_off()  # Turn off light if it's too bright
                            logger.info(f"Turned off light in {room_name} due to high light intensity: {light_intensity} lux")
                        else:
                            # Adjust light brightness based on the current light intensity
                            # (You can add more logic here to fine-tune the brightness level)
                            actuator.turn_on()
                            actuator.set_brightness_level("medium")
                            logger.info(f"Adjusted light brightness in {room_name} to medium")

# Main function to check and adjust all environmental factors
def main():
    rooms_to_check = ["LivingRoom", "Bedroom", "Kitchen", "Bathroom"]  # Add or remove rooms as needed
    
    for room in rooms_to_check:
        check_and_adjust_temperature(room)
        check_and_adjust_humidity(room)
        check_and_adjust_light_intensity(room)

if __name__ == "__main__":
    main()