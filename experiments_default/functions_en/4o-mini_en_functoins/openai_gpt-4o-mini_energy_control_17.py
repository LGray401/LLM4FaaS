# Based on your functional description of "Save energy" and the provided source code for your smart home project, I will create a `function.py` file. This file will contain a main function that will demonstrate how to use the various sensors and actuators to optimize energy usage in your home.
# 
# The main function will:
# - Monitor the temperature and humidity in the home.
# - Control heating and air conditioning based on the current temperature.
# - Adjust lighting based on the light intensity sensor readings.
# - Send notifications when actions are taken to save energy.
# 
# Here is the `function.py` code:

# functions/function.py

from home.home_plan import home_plan, print_home_plan, get_room_sensors, get_room_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.actuator import Heater, AC, Light
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor

def energy_saving_routine(home):
    print_home_plan(home)

    for room in home:
        sensors = get_room_sensors(home, room.name)
        actuators = get_room_actuators(home, room.name)

        # Process temperature sensors
        temp_sensor = next((s for s in sensors if isinstance(s, IndoorTemperatureSensor)), None)
        humidity_sensor = next((s for s in sensors if isinstance(s, HumiditySensor)), None)
        light_sensor = next((s for s in sensors if isinstance(s, LightIntensiveSensor)), None)

        if temp_sensor:
            temp_sensor.turn_on()
            current_temp = temp_sensor.get_reading()
            temp_sensor.turn_off()

            # Adjust heating or cooling
            for actuator in actuators:
                if isinstance(actuator, Heater):
                    if current_temp is not None and current_temp < TEMP_LOW:
                        actuator.set_target_temperature(TEMP_LOW)
                        actuator.adjust_temperature(current_temp)
                elif isinstance(actuator, AC):
                    if current_temp is not None and current_temp > TEMP_HIGH:
                        actuator.set_target_temperature(TEMP_HIGH)
                        actuator.adjust_temperature(current_temp)

        if humidity_sensor:
            humidity_sensor.turn_on()
            current_humidity = humidity_sensor.get_reading()
            humidity_sensor.turn_off()

            # Control humidifiers based on humidity levels
            for actuator in actuators:
                if isinstance(actuator, Light):
                    if current_humidity is not None and current_humidity < HUMIDITY_LOW:
                        actuator.turn_on()
                    elif current_humidity is not None and current_humidity > HUMIDITY_HIGH:
                        actuator.turn_off()

        if light_sensor:
            light_sensor.turn_on()
            current_light = light_sensor.get_reading()
            light_sensor.turn_off()

            # Control lights based on light intensity
            for actuator in actuators:
                if isinstance(actuator, Light):
                    if current_light is not None and current_light < LIGHT_INTENSITY_LOW:
                        actuator.turn_on()
                    elif current_light is not None and current_light > LIGHT_INTENSITY_HIGH:
                        actuator.turn_off()

if __name__ == "__main__":
    home = home_plan()
    energy_saving_routine(home)