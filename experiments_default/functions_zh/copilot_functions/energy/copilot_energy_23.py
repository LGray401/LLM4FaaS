# Based on the functional description and the provided source code, you want to create a `function.py` file that controls the smart home system. The functional description is in Chinese, but I can translate it for you:
#
# "When the light intensity increases, the light automatically turns off. When the indoor temperature is below 20 degrees, turn on the heater. The cleaning robot can work from Monday to Friday during work hours. When you come back from work, if the humidity is insufficient, it can automatically humidify."
#
# Here is the Python code that implements this functionality:
#
# ```python
from home.sensor import IndoorTemperatureSensor, LightIntensiveSensor, HumiditySensor
from home.actuator import Heater, Light, CleaningRobot, Humidifier
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, LIGHT_INTENSITY_HIGH, HUMIDITY_LOW
import datetime

def main():
    home = home_plan()

    # Get all sensors and actuators
    temp_sensors = get_all_sensors(home, "IndoorTemperature")
    light_sensors = get_all_sensors(home, "LightIntensive")
    humidity_sensors = get_all_sensors(home, "Humidity")

    heaters = get_all_actuators(home, "Heater")
    lights = get_all_actuators(home, "Light")
    cleaning_robots = get_all_actuators(home, "CleaningRobot")
    humidifiers = get_all_actuators(home, "Humidifier")

    # Check each room
    for temp_sensor, light_sensor, humidity_sensor in zip(temp_sensors, light_sensors, humidity_sensors):
        # Get sensor readings
        temp = temp_sensor.get_reading()
        light = light_sensor.get_reading()
        humidity = humidity_sensor.get_reading()

        # Control heater
        for heater in heaters:
            if temp < TEMP_LOW:
                heater.turn_on()
            else:
                heater.turn_off()

        # Control light
        for light in lights:
            if light > LIGHT_INTENSITY_HIGH:
                light.turn_off()
            else:
                light.turn_on()

        # Control cleaning robot
        for cleaning_robot in cleaning_robots:
            if datetime.datetime.today().weekday() < 5:  # Monday to Friday
                cleaning_robot.turn_on()
            else:
                cleaning_robot.turn_off()

        # Control humidifier
        for humidifier in humidifiers:
            if humidity < HUMIDITY_LOW:
                humidifier.turn_on()
            else:
                humidifier.turn_off()

if __name__ == "__main__":
    main()
# ```
#
# This code should be placed in a new file named `function.py` in the `functions` folder. It uses the sensors to get readings for temperature, light intensity, and humidity. Then, it controls the actuators (heater, light, cleaning robot, and humidifier) based on these readings and the current day of the week.