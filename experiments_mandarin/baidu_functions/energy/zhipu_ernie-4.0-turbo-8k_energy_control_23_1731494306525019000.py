# Based on your functional description and the provided source code, I will now provide a `function.py` file that contains the main function to control the smart home system as per the specified requirements.
# 
# Here is the `function.py` file:

from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.sensor import Sensor
from home.actuator import Actuator, Heater, Light, CleaningRobot, Humidifier
from home.config import TEMP_LOW, HUMIDITY_LOW, LIGHT_INTENSITY_HIGH
import time

def main():
    # Initialize the home plan
    home = home_plan()
    
    while True:
        # Get all the necessary sensors and actuators
        light_sensors = get_all_sensors(home, "LightIntensive")
        temp_sensors = get_all_sensors(home, "IndoorTemperature")
        humidity_sensors = get_all_sensors(home, "Humidity")
        
        lights = get_all_actuators(home, "Light")
        heaters = get_all_actuators(home, "Heater")
        cleaning_robots = get_all_actuators(home, "CleaningRobot")
        humidifiers = get_all_actuators(home, "Humidifier")
        
        # Check light intensity and turn off lights if it's too bright
        for sensor in light_sensors:
            if sensor.get_status() == "on" and sensor.get_reading() > LIGHT_INTENSITY_HIGH:
                for light in lights:
                    if light.room_name == sensor.room_name:
                        light.turn_off()
        
        # Check indoor temperature and turn on heater if it's too cold
        for sensor in temp_sensors:
            if sensor.get_status() == "on" and sensor.get_reading() < TEMP_LOW:
                for heater in heaters:
                    if heater.room_name == sensor.room_name:
                        heater.turn_on()
                        heater.set_target_temperature(20)  # Set target temperature to 20 degrees Celsius
        
        # Check if it's Monday to Friday and allow cleaning robots to work
        current_time = time.localtime()
        if 0 <= current_time.tm_wday <= 4:  # tm_wday: 0=Monday, 1=Tuesday, ..., 6=Sunday
            for robot in cleaning_robots:
                robot.turn_on()
                robot.daily_routine()
        else:
            for robot in cleaning_robots:
                robot.turn_off()
        
        # Check humidity and turn on humidifier if it's too low
        for sensor in humidity_sensors:
            if sensor.get_status() == "on" and sensor.get_reading() < HUMIDITY_LOW:
                for humidifier in humidifiers:
                    if humidifier.room_name == sensor.room_name:
                        humidifier.turn_on()
                        humidifier.increase_humidity()
        
        # Sleep for a while before checking again
        time.sleep(60)  # Check every 60 seconds

if __name__ == "__main__":
    main()