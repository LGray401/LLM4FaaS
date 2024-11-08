# Given the functional description and the provided code, I will now create the `function.py` file which should contain the main function to control the smart home based on the rules you've described. This file will be placed in the `functions` folder and will utilize the classes and methods from the `sensor.py`, `actuator.py`, and `home_plan.py` files.
# 
# Here is the `function.py`:

# function.py

from home.home_plan import home_plan
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, Light, CleaningRobot, Humidifier

def main():
    # Get the home plan
    home = home_plan()

    # Function to check and act based on light intensity
    def check_light_intensity():
        for room in home:
            light_sensor = room.get_sensor_by_type(LightIntensiveSensor)
            if light_sensor:
                light_intensity = light_sensor.get_reading()
                if light_intensity > 900:  # Assuming the light intensity threshold is 900 lux
                    # Turn off the lights if light is too intense
                    for light in room.get Actuators_by_type(Light):
                        light.turn_off()

    # Function to check and act based on indoor temperature
    def check_indoor_temperature():
        for room in home:
            temp_sensor = room.get_sensor_by_type(IndoorTemperatureSensor)
            if temp_sensor:
                temperature = temp_sensor.get_reading()
                if temperature < 20:  # Assuming the temperature threshold is 20 degrees Celsius
                    # Turn on the heater if temperature is too low
                    for heater in room.get Actuators_by_type(Heater):
                        heater.turn_on()

    # Function to check and act based on humidity level
    def check_humidity_level():
        for room in home:
            humidity_sensor = room.get_sensor_by_type(HumiditySensor)
            if humidity_sensor:
                humidity = humidity_sensor.get_reading()
                if humidity < 40:  # Assuming the humidity threshold is 40%
                    # Turn on the humidifier if humidity is too low
                    for humidifier in room.get Actuators_by_type(Humidifier):
                        humidifier.turn_on()

    # Function to check and act based on weekday and time (for cleaning robot)
    def check_cleaning_robot():
        from datetime import datetime
        weekday = datetime.now().weekday()  # Monday is 0, Sunday is 6
        if weekday < 5:  # Monday to Friday
            for room in home:
                cleaning_robot = room.get Actuators_by_type(CleaningRobot)
                if cleaning_robot:
                    cleaning_robot.daily_routine()

    # Execute functions
    check_light_intensity()
    check_indoor_temperature()
    check_humidity_level()
    check_cleaning_robot()

if __name__ == "__main__":
    main()