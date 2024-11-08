# Based on the functional description and the provided source code, you need to create a `function.py` file that contains the main function for your smart home project. The main function should control the temperature, humidity, and light intensity in the home according to the rules described in the functional description.
#
# Here is a rough plan for the `function.py` file:
#
# 1. Import necessary modules and classes from `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py`.
# 2. Define a function for each of the conditions described in the functional description. Each function should get the relevant sensor readings, check if the readings meet the condition, and if so, perform the necessary actions using the actuators.
# 3. Define the main function that calls the above functions in a loop.
#
# Here is the code for `function.py`:
#
# ```python
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC, Window, Humidifier, Light, Curtain
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def control_temperature(home):
    temp_sensors = get_all_sensors(home, "IndoorTemperature")
    acs = get_all_actuators(home, "AC")
    windows = get_all_actuators(home, "Window")

    for sensor in temp_sensors:
        temp = sensor.get_reading()
        if temp > TEMP_HIGH:
            for ac in acs:
                ac.turn_on()
            for window in windows:
                window.turn_off()

def control_humidity(home):
    humidity_sensors = get_all_sensors(home, "Humidity")
    humidifiers = get_all_actuators(home, "Humidifier")

    for sensor in humidity_sensors:
        humidity = sensor.get_reading()
        if humidity < HUMIDITY_LOW:
            for humidifier in humidifiers:
                humidifier.turn_on()

def control_light_intensity(home):
    light_sensors = get_all_sensors(home, "LightIntensive")
    lights = get_all_actuators(home, "Light")
    curtains = get_all_actuators(home, "Curtain")

    for sensor in light_sensors:
        light_intensity = sensor.get_reading()
        if light_intensity < LIGHT_INTENSITY_LOW:
            for light in lights:
                light.turn_on()
        elif light_intensity > LIGHT_INTENSITY_HIGH:
            for curtain in curtains:
                curtain.turn_on()
            for light in lights:
                light.turn_on()

def main():
    home = home_plan()
    while True:
        control_temperature(home)
        control_humidity(home)
        control_light_intensity(home)

if __name__ == "__main__":
    main()
# ```
#
# This code should be placed in the `function.py` file in the 'functions' folder. It will continuously monitor the sensor readings and control the actuators to maintain the desired conditions in the home.