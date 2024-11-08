# Based on the content of the markdown file, you are working on a smart home project and you need a `function.py` file that will contain the main function. This function should be able to control the temperature, humidity, and light intensity in the home based on the readings from various sensors.
#
# Here is a high-level overview of what the `function.py` file might look like:
#
# 1. Import necessary modules and classes from `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py`.
# 2. Define a `main` function that will control the smart home system.
# 3. In the `main` function, create an instance of the home plan.
# 4. For each room in the home, get the sensor readings for temperature, humidity, and light intensity.
# 5. Based on the sensor readings, control the actuators in each room. For example, if the temperature is higher than 26 degrees, turn on the air conditioners and close the windows. If the humidity is less than 30%, activate the humidifier. If the light intensity is less than 150 lux, turn up the lights, and if it is greater than 11080 lux, draw the curtains and turn on the indoor lights.
#
# Here is a simplified version of the `function.py` file:
#
# ```python
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC, Window, Humidifier, Light, Curtain
from home.home_plan import home_plan
from home.config import TEMP_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    home = home_plan()

    for room in home:
        # Get sensor readings
        temperature = next((sensor.get_reading() for sensor in room.sensors if isinstance(sensor, IndoorTemperatureSensor)), None)
        humidity = next((sensor.get_reading() for sensor in room.sensors if isinstance(sensor, HumiditySensor)), None)
        light_intensity = next((sensor.get_reading() for sensor in room.sensors if isinstance(sensor, LightIntensiveSensor)), None)

        # Control actuators based on sensor readings
        if temperature is not None and temperature > TEMP_HIGH:
            for actuator in room.actuators:
                if isinstance(actuator, AC):
                    actuator.turn_on()
                elif isinstance(actuator, Window):
                    actuator.turn_off()

        if humidity is not None and humidity < HUMIDITY_LOW:
            for actuator in room.actuators:
                if isinstance(actuator, Humidifier):
                    actuator.turn_on()

        if light_intensity is not None:
            for actuator in room.actuators:
                if isinstance(actuator, Light):
                    if light_intensity < LIGHT_INTENSITY_LOW:
                        actuator.turn_on()
                    elif light_intensity > LIGHT_INTENSITY_HIGH:
                        actuator.turn_off()
                elif isinstance(actuator, Curtain):
                    if light_intensity > LIGHT_INTENSITY_HIGH:
                        actuator.turn_on()

if __name__ == "__main__":
    main()
# ```
#
# This code assumes that the `turn_on` and `turn_off` methods of the actuators change the state of the actuators as expected. You may need to adjust this code to fit the actual behavior of your actuators.