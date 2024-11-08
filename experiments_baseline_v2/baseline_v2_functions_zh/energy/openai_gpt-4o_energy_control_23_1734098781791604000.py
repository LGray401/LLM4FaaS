# To create a smart home application based on your functional description, we will use the provided reference code files. Here's a Python script implementing the required functionality:
# 
# ### Functional Requirements:
# 1. **Turn off the lights when the light intensity increases.**
# 2. **Turn on the heater if the indoor temperature is below 20 degrees Celsius.**
# 3. **Allow the cleaning robot to work Monday to Friday.**
# 4. **Turn on the humidifier if humidity is insufficient when returning home from work.**
# 
# ### Implementation:
# 
# ```python
import datetime
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Light, Heater, CleaningRobot, Humidifier
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, LIGHT_INTENSITY_HIGH, DAILY_ROUTINE_DURATION

def manage_lighting(home):
    light_intensity_sensors = get_all_sensors(home, "LightIntensive")
    lights = get_all_actuators(home, "Light")
    
    for sensor in light_intensity_sensors:
        sensor.turn_on()
        light_intensity = sensor.get_reading()
        if light_intensity and light_intensity > LIGHT_INTENSITY_HIGH:
            for light in lights:
                light.turn_off()
        sensor.turn_off()

def manage_heating(home):
    temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    heaters = get_all_actuators(home, "Heater")

    for sensor in temperature_sensors:
        sensor.turn_on()
        temperature = sensor.get_reading()
        if temperature and temperature < 20:
            for heater in heaters:
                heater.turn_on()
        sensor.turn_off()

def manage_cleaning_robot(home):
    cleaning_robots = get_all_actuators(home, "CleaningRobot")
    current_day = datetime.datetime.now().weekday()

    if 0 <= current_day <= 4:  # Monday to Friday
        for robot in cleaning_robots:
            robot.turn_on()
            robot.daily_routine()

def manage_humidifier(home):
    humidity_sensors = get_all_sensors(home, "Humidity")
    humidifiers = get_all_actuators(home, "Humidifier")

    for sensor in humidity_sensors:
        sensor.turn_on()
        humidity = sensor.get_reading()
        if humidity and humidity < 30:  # Assuming 30 as an arbitrary insufficient humidity level
            for humidifier in humidifiers:
                humidifier.turn_on()
        sensor.turn_off()

def main():
    home = home_plan()
    
    manage_lighting(home)
    manage_heating(home)
    manage_cleaning_robot(home)
    manage_humidifier(home)

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation:
# - **manage_lighting:** Turns off the lights if the light intensity is above a certain threshold.
# - **manage_heating:** Turns on the heater if the indoor temperature is below 20°C.
# - **manage_cleaning_robot:** Activates the cleaning robot on weekdays.
# - **manage_humidifier:** Turns on the humidifier if the humidity is below a specified level.
# 
# ### Running the Application:
# To run this application in a Linux terminal, save the above script as `smart_home.py` and use the following command:
# ```bash
# python3 smart_home.py
# ```
# 
# This command will execute the script, leveraging the sensors and actuators as defined in the provided reference code files.