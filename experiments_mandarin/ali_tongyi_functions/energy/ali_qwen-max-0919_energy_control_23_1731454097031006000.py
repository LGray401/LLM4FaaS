# Based on your functional description and the provided source code, I will create a `function.py` file that contains the main function to control the smart home system. The main function will implement the following functionalities:
# 
# 1. **Light Control**: When light intensity increases, turn off the lights.
# 2. **Heater Control**: If the indoor temperature is below 20 degrees Celsius, turn on the heater.
# 3. **Cleaning Robot**: Allow the cleaning robot to work from Monday to Friday.
# 4. **Humidifier Control**: If the humidity is low when you come back from work, turn on the humidifier.
# 
# Here is the `function.py` file:

# functions/function.py

import datetime
from home.sensor import LightIntensiveSensor, IndoorTemperatureSensor, HumiditySensor
from home.actuator import Light, Heater, CleaningRobot, Humidifier
from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.config import TEMP_LOW, HUMIDITY_LOW, LIGHT_INTENSITY_HIGH, DAILY_ROUTINE_DURATION

def control_lights(home):
    for room in home:
        light_intensity_sensors = [sensor for sensor in get_room_sensors(home, room.name) if isinstance(sensor, LightIntensiveSensor)]
        lights = [actuator for actuator in get_room_actuators(home, room.name) if isinstance(actuator, Light)]

        for sensor in light_intensity_sensors:
            sensor.turn_on()
            reading = sensor.get_reading()
            sensor.turn_off()

            if reading and reading > LIGHT_INTENSITY_HIGH:
                for light in lights:
                    if light.status == "on":
                        light.turn_off()

def control_heater(home):
    for room in home:
        temperature_sensors = [sensor for sensor in get_room_sensors(home, room.name) if isinstance(sensor, IndoorTemperatureSensor)]
        heaters = [actuator for actuator in get_room_actuators(home, room.name) if isinstance(actuator, Heater)]

        for sensor in temperature_sensors:
            sensor.turn_on()
            reading = sensor.get_reading()
            sensor.turn_off()

            if reading and reading < 20:
                for heater in heaters:
                    heater.set_target_temperature(20)
                    heater.adjust_temperature(reading)

def control_cleaning_robot(home):
    current_day = datetime.datetime.now().weekday()  # Monday is 0, Sunday is 6
    if 0 <= current_day <= 4:  # Monday to Friday
        for room in home:
            cleaning_robots = [actuator for actuator in get_room_actuators(home, room.name) if isinstance(actuator, CleaningRobot)]

            for robot in cleaning_robots:
                robot.turn_on()
                robot.daily_routine()

def control_humidifier(home):
    for room in home:
        humidity_sensors = [sensor for sensor in get_room_sensors(home, room.name) if isinstance(sensor, HumiditySensor)]
        humidifiers = [actuator for actuator in get_room_actuators(home, room.name) if isinstance(actuator, Humidifier)]

        for sensor in humidity_sensors:
            sensor.turn_on()
            reading = sensor.get_reading()
            sensor.turn_off()

            if reading and reading < HUMIDITY_LOW:
                for humidifier in humidifiers:
                    humidifier.turn_on()
                    humidifier.increase_humidity()

def main():
    home = home_plan()
    
    control_lights(home)
    control_heater(home)
    control_cleaning_robot(home)
    control_humidifier(home)

if __name__ == "__main__":
    main()