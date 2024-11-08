# Based on the functional description and the provided source code, you need to create a `function.py` file that contains the main function. This function should control the smart home system according to the following rules:
#
# 1. When the light intensity increases, the light turns off automatically.
# 2. When the indoor temperature is below 20 degrees, turn on the heater.
# 3. From Monday to Friday, the robot vacuum cleaner can work.
# 4. When you come back from get off work, if the humidity is insufficient, it can automatically humidify.
#
# Here is a basic implementation of the `function.py` file:
#
# ```python
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, CleaningRobot, Humidifier, Light
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from datetime import datetime

def main():
    # Get the home plan
    home = home_plan()

    # Get all the sensors and actuators
    temp_sensors = get_all_sensors(home, "IndoorTemperature")
    humidity_sensors = get_all_sensors(home, "Humidity")
    light_sensors = get_all_sensors(home, "LightIntensive")

    heaters = get_all_actuators(home, "Heater")
    cleaning_robots = get_all_actuators(home, "CleaningRobot")
    humidifiers = get_all_actuators(home, "Humidifier")
    lights = get_all_actuators(home, "Light")

    # Check the current day of the week
    current_day = datetime.today().weekday()  # Monday is 0 and Sunday is 6

    # Iterate over all the rooms
    for temp_sensor, humidity_sensor, light_sensor, heater, cleaning_robot, humidifier, light in zip(temp_sensors, humidity_sensors, light_sensors, heaters, cleaning_robots, humidifiers, lights):
        # Get the current readings
        temp = temp_sensor.get_reading()
        humidity = humidity_sensor.get_reading()
        light_intensity = light_sensor.get_reading()

        # Control the heater
        if temp < 20:
            heater.turn_on()
        else:
            heater.turn_off()

        # Control the light
        if light_intensity > 900:
            light.turn_off()
        else:
            light.turn_on()

        # Control the cleaning robot
        if 0 <= current_day <= 4:  # From Monday to Friday
            cleaning_robot.turn_on()
        else:
            cleaning_robot.turn_off()

        # Control the humidifier
        if humidity < 30:  # Assuming that the humidity is insufficient if it's less than 30%
            humidifier.turn_on()
        else:
            humidifier.turn_off()

if __name__ == "__main__":
    main()
# ```
#
# This script will control the smart home system according to the rules. Please note that you need to adjust the conditions and the thresholds according to your needs. Also, the script assumes that there is the same number of each type of sensor and actuator in the home. If this is not the case, you will need to adjust the script accordingly.