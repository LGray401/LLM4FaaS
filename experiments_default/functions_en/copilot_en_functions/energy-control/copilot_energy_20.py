# Based on the content of the markdown file, you are working on a smart home project and you need a `function.py` file. This file should contain the main function that will control the indoor temperature, humidity, and light intensity automatically.
#
# Here is a high-level plan for the `function.py` file:
#
# 1. Import necessary modules and classes from `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py`.
# 2. Define a `main` function.
# 3. Inside the `main` function, create an instance of the home plan.
# 4. Get all the necessary sensors and actuators from the home plan.
# 5. Create a loop that will continuously check the sensor readings and adjust the actuators accordingly.
#
# Here is the Python code for `function.py`:
#
# ```python
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, AC, Light
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    # Create an instance of the home plan
    home = home_plan()

    # Get all the necessary sensors
    temp_sensors = get_all_sensors(home, "IndoorTemperature")
    humidity_sensors = get_all_sensors(home, "Humidity")
    light_sensors = get_all_sensors(home, "LightIntensive")

    # Get all the necessary actuators
    heaters = get_all_actuators(home, "Heater")
    acs = get_all_actuators(home, "AC")
    lights = get_all_actuators(home, "Light")

    while True:
        # Check the sensor readings and adjust the actuators accordingly
        for sensor in temp_sensors:
            reading = sensor.get_reading()
            if reading is not None:
                if reading < TEMP_LOW:
                    for heater in heaters:
                        heater.turn_on()
                elif reading > TEMP_HIGH:
                    for ac in acs:
                        ac.turn_on()

        for sensor in humidity_sensors:
            reading = sensor.get_reading()
            if reading is not None:
                if reading < HUMIDITY_LOW:
                    # Increase humidity
                    pass
                elif reading > HUMIDITY_HIGH:
                    # Decrease humidity
                    pass

        for sensor in light_sensors:
            reading = sensor.get_reading()
            if reading is not None:
                if reading < LIGHT_INTENSITY_LOW:
                    for light in lights:
                        light.turn_on()
                elif reading > LIGHT_INTENSITY_HIGH:
                    for light in lights:
                        light.turn_off()

if __name__ == "__main__":
    main()
# ```
#
# Please note that the code for increasing and decreasing humidity is not provided because the `actuator.py` file does not contain any actuators that can control humidity. You may need to add a humidifier and dehumidifier class to your `actuator.py` file.