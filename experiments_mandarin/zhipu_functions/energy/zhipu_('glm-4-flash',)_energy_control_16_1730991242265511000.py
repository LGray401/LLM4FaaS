# Given the functional description "节能" which translates to "energy-saving," I will create a `function.py` that will serve as a main function to control and optimize the smart home system's energy consumption. This script will use the sensors and actuators to adjust the environment to a more energy-efficient state.
# 
# Here's the `function.py` file in the `functions` folder:

# functions/function.py

from home.sensor import Sensor, IndoorTemperatureSensor, OutdoorTemperatureSensor, HumiditySensor, \
    LightIntensiveSensor
from home.actuator import Actuator, Heater, AC, Light, Humidifier, Window, Door, Curtain, CleaningRobot
from home.home_plan import home_plan
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def optimize_energy_usage():
    home = home_plan()

    # Turn off unnecessary lights
    for room in home:
        light = next((actuator for actuator in room.actuators if isinstance(actuator, Light)), None)
        if light and not any(isinstance(sensor, LightIntensiveSensor) and sensor.get_reading() < LIGHT_INTENSITY_LOW for sensor in room.sensors):
            light.turn_off()

    # Adjust AC and Heater based on temperature
    for room in home:
        if IndoorTemperatureSensor in room.sensors:
            temp_sensor = next((sensor for sensor in room.sensors if isinstance(sensor, IndoorTemperatureSensor)), None)
            if temp_sensor:
                current_temp = temp_sensor.get_reading()
                if current_temp < TEMP_LOW:
                    if AC in room.actuators:
                        ac = next((actuator for actuator in room.actuators if isinstance(actuator, AC)), None)
                        ac.turn_on()
                    if Heater in room.actuators:
                        heater = next((actuator for actuator in room.actuators if isinstance(actuator, Heater)), None)
                        heater.turn_on()
                elif current_temp > TEMP_HIGH:
                    if AC in room.actuators:
                        ac = next((actuator for actuator in room.actuators if isinstance(actuator, AC)), None)
                        ac.turn_off()
                    if Heater in room.actuators:
                        heater = next((actuator for actuator in room.actuators if isinstance(actuator, Heater)), None)
                        heater.turn_off()

    # Adjust Humidifier based on humidity
    for room in home:
        if HumiditySensor in room.sensors:
            humidity_sensor = next((sensor for sensor in room.sensors if isinstance(sensor, HumiditySensor)), None)
            if humidity_sensor:
                humidity = humidity_sensor.get_reading()
                if humidity < HUMIDITY_LOW:
                    if Humidifier in room.actuators:
                        humidifier = next((actuator for actuator in room.actuators if isinstance(actuator, Humidifier)), None)
                        humidifier.increase_humidity()
                elif humidity > HUMIDITY_HIGH:
                    if Humidifier in room.actuators:
                        humidifier = next((actuator for actuator in room.actuators if isinstance(actuator, Humidifier)), None)
                        humidifier.decrease_humidity()

    # Turn off unnecessary heating and cooling
    for room in home:
        if IndoorTemperatureSensor in room.sensors:
            temp_sensor = next((sensor for sensor in room.sensors if isinstance(sensor, IndoorTemperatureSensor)), None)
            if temp_sensor:
                current_temp = temp_sensor.get_reading()
                if current_temp < TEMP_LOW and AC in room.actuators:
                    ac = next((actuator for actuator in room.actuators if isinstance(actuator, AC)), None)
                    ac.turn_off()
                elif current_temp > TEMP_HIGH and Heater in room.actuators:
                    heater = next((actuator for actuator in room.actuators if isinstance(actuator, Heater)), None)
                    heater.turn_off()

    # Open windows if necessary
    for room in home:
        if IndoorTemperatureSensor in room.sensors and LightIntensiveSensor in room.sensors:
            temp_sensor = next((sensor for sensor in room.sensors if isinstance(sensor, IndoorTemperatureSensor)), None)
            light_sensor = next((sensor for sensor in room.sensors if isinstance(sensor, LightIntensiveSensor)), None)
            if temp_sensor and light_sensor:
                current_temp = temp_sensor.get_reading()
                light_intensity = light_sensor.get_reading()
                if current_temp > TEMP_HIGH and light_intensity > LIGHT_INTENSITY_LOW and Window in room.actuators:
                    window = next((actuator for actuator in room.actuators if isinstance(actuator, Window)), None)
                    window.turn_on()

    # Perform daily cleaning routine
    for room in home:
        if CleaningRobot in room.actuators:
            cleaning_robot = next((actuator for actuator in room.actuators if isinstance(actuator, CleaningRobot)), None)
            cleaning_robot.daily_routine()

# Run the energy optimization function
if __name__ == "__main__":
    optimize_energy_usage()