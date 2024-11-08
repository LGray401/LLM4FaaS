# Based on your functional description and the provided source code files, I'll create the `function.py` file that contains the main functionality for your smart home project. This script will utilize the sensors and actuators to implement the described behaviors:
# 
# 1. Turn off the light when light intensity increases.
# 2. Turn on the heater if indoor temperature is below 20 degrees.
# 3. Allow the robot vacuum cleaner to work from Monday to Friday.
# 4. Automatically humidify when you come back from work if humidity is insufficient.
# 
# Here's how the `function.py` file will look:

# functions/function.py

import datetime
from home.home_plan import home_plan
from home.config import TEMP_LOW, HUMIDITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger

def main():
    home = home_plan()  # Initialize the home plan

    # Example for daily routine
    current_day = datetime.datetime.now().weekday()  # Monday is 0 and Sunday is 6
    is_weekday = current_day < 5  # Monday to Friday

    for room in home:
        # Check sensors and actuators in each room
        for sensor in room.sensors:
            if isinstance(sensor, LightIntensiveSensor):
                light_reading = sensor.get_reading()
                if light_reading and light_reading > LIGHT_INTENSITY_HIGH:
                    light_actuator = next((act for act in room.actuators if isinstance(act, Light)), None)
                    if light_actuator:
                        light_actuator.turn_off()
            elif isinstance(sensor, IndoorTemperatureSensor):
                temperature_reading = sensor.get_reading()
                if temperature_reading and temperature_reading < TEMP_LOW:
                    heater_actuator = next((act for act in room.actuators if isinstance(act, Heater)), None)
                    if heater_actuator:
                        heater_actuator.set_target_temperature(20)  # Set target temperature to 20 degrees
                        heater_actuator.adjust_temperature(temperature_reading)
            elif isinstance(sensor, HumiditySensor):
                humidity_reading = sensor.get_reading()
                if humidity_reading and humidity_reading < HUMIDITY_LOW:
                    humidifier_actuator = next((act for act in room.actuators if isinstance(act, Humidifier)), None)
                    if humidifier_actuator:
                        humidifier_actuator.increase_humidity()

        # Check if robot vacuum cleaner can operate
        cleaning_robot = next((act for act in room.actuators if isinstance(act, CleaningRobot)), None)
        if cleaning_robot and is_weekday:
            cleaning_robot.turn_on()
            cleaning_robot.daily_routine()

if __name__ == "__main__":
    main()