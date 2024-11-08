# Based on your functional description and the provided source code, here is a potential implementation for the `function.py` file. This file will contain a main function that integrates the various components (sensors and actuators), asks for user input regarding their preferences, and performs the necessary actions based on the conditions detected by the sensors.
# 
# ### `function.py`

import random
from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.logger_config import logger
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH

def check_weather_conditions(outdoor_temp, humid_sensor):
    """Check outdoor temperature and humidity conditions to decide actions."""
    if outdoor_temp < TEMP_LOW or outdoor_temp > TEMP_HIGH:
        return "It's too extreme outside. Consider using the AC instead."
    elif humid_sensor.get_reading() < HUMIDITY_LOW:
        return "The air is too dry outside. It might be better to use a humidifier."
    return "Weather conditions are acceptable."

def main():
    home = home_plan()
    
    # Example: Check the Living Room for sensors and actuators
    living_room = get_room_sensors(home, "LivingRoom")
    if living_room is None:
        print("No sensors found in the Living Room.")
        return
    
    # Collect readings from sensors
    outdoor_temp_sensor = next((sensor for sensor in living_room if sensor.sensor_type == "OutdoorTemperature"), None)
    humidity_sensor = next((sensor for sensor in living_room if sensor.sensor_type == "Humidity"), None)

    # Get readings
    if outdoor_temp_sensor and humidity_sensor:
        outdoor_temp = outdoor_temp_sensor.get_reading()
        humidity_reading = humidity_sensor.get_reading()
        
        weather_advice = check_weather_conditions(outdoor_temp, humidity_sensor)
        print(weather_advice)

        # User input to control actuators based on sensor readings
        user_command = input("Do you want to open the window (yes/no)? ").strip().lower()
        if user_command == 'yes':
            window_actuator = next((actuator for actuator in get_room_actuators(home, "LivingRoom") if actuator.actuator_type == "Window"), None)
            if window_actuator:
                if weather_advice == "It's too extreme outside. Consider using the AC instead.":
                    print("Opening the window is not advisable.")
                else:
                    window_actuator.turn_on()
            else:
                print("No window actuator found.")
        
        user_command = input("Would you like to turn on the AC (yes/no)? ").strip().lower()
        if user_command == 'yes':
            ac_actuator = next((actuator for actuator in get_room_actuators(home, "LivingRoom") if actuator.actuator_type == "AC"), None)
            if ac_actuator:
                ac_actuator.turn_on()
            else:
                print("No AC actuator found.")

        user_command = input("Would you like to turn on the humidifier (yes/no)? ").strip().lower()
        if user_command == 'yes':
            humidifier_actuator = next((actuator for actuator in get_room_actuators(home, "LivingRoom") if actuator.actuator_type == "Humidifier"), None)
            if humidifier_actuator:
                humidifier_actuator.increase_humidity()
            else:
                print("No humidifier actuator found.")

if __name__ == "__main__":
    main()