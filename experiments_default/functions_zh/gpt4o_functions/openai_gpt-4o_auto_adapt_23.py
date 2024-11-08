# Sure, based on the provided functional description and the existing code, I will create a `function.py` file that reads the sensor data and takes actions according to the functional description.
# 
# ### functions/function.py

import sys
sys.path.append('..')

from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, AC, Humidifier, Light
from home.home_plan import home_plan, get_room_sensors, get_room_actuators

def main():
    # Initialize home with the predefined plan
    home = home_plan()

    # Get sensors and actuators for the LivingRoom
    room_name = "LivingRoom"
    sensors = get_room_sensors(home, room_name)
    actuators = get_room_actuators(home, room_name)

    # Define target values based on the functional description
    target_temperature = 23
    target_humidity = "人感觉舒适"
    target_light_intensity = "柔和"

    # Create a dictionary to store sensor readings
    sensor_readings = {}

    # Turn on all sensors and get readings
    for sensor in sensors:
        sensor.turn_on()
        reading = sensor.get_reading()
        sensor_readings[sensor.sensor_type] = reading

    # Perform actions based on readings and target values
    for actuator in actuators:
        if isinstance(actuator, Heater) and sensor_readings.get("IndoorTemperature") is not None:
            actuator.set_target_temperature(target_temperature)
            actuator.adjust_temperature(sensor_readings["IndoorTemperature"])

        if isinstance(actuator, AC) and sensor_readings.get("IndoorTemperature") is not None:
            actuator.set_target_temperature(target_temperature)
            actuator.adjust_temperature(sensor_readings["IndoorTemperature"])

        if isinstance(actuator, Humidifier) and sensor_readings.get("Humidity") is not None:
            if target_humidity == "人感觉舒适":
                if sensor_readings["Humidity"] < 40:
                    actuator.turn_on()
                    actuator.increase_humidity()
                elif sensor_readings["Humidity"] > 60:
                    actuator.turn_on()
                    actuator.decrease_humidity()
                else:
                    actuator.turn_off()

        if isinstance(actuator, Light) and sensor_readings.get("LightIntensive") is not None:
            if target_light_intensity == "柔和":
                if sensor_readings["LightIntensive"] < 500:
                    actuator.turn_on()
                    actuator.set_brightness_level("medium")
                elif sensor_readings["LightIntensive"] > 800:
                    actuator.turn_on()
                    actuator.set_brightness_level("low")
                else:
                    actuator.turn_off()

if __name__ == "__main__":
    main()