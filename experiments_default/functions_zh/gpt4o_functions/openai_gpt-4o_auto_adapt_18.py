# Given the functional description and the provided source code, we need to create a `function.py` file within the `functions` folder that includes a main function. This main function will instantiate the sensors and actuators based on the provided details and make use of them accordingly.
# 
# Here's a `function.py` file that meets your requirements:

# functions/function.py

from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, AC, Light, Humidifier
from home.home_plan import home_plan, print_home_plan, get_room_sensors, get_room_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    home = home_plan()

    # Print the home plan
    print_home_plan(home)

    # Get the sensors and actuators for the LivingRoom
    living_room_sensors = get_room_sensors(home, "LivingRoom")
    living_room_actuators = get_room_actuators(home, "LivingRoom")

    # Turn on all sensors and get readings
    print("\nTurning on all sensors and getting readings:")
    sensor_readings = {}
    for sensor in living_room_sensors:
        sensor.turn_on()
        reading = sensor.get_reading()
        sensor_readings[sensor.sensor_type] = reading

    # Print sensor readings
    print("\nSensor Readings:")
    for sensor_type, reading in sensor_readings.items():
        print(f"{sensor_type}: {reading}")

    # Control actuators based on sensor readings
    print("\nControlling actuators based on sensor readings:")

    for actuator in living_room_actuators:
        if isinstance(actuator, Heater):
            actuator.set_target_temperature(TEMP_HIGH)
            actuator.adjust_temperature(sensor_readings.get("IndoorTemperature"))
        elif isinstance(actuator, AC):
            actuator.set_target_temperature(TEMP_LOW)
            actuator.adjust_temperature(sensor_readings.get("IndoorTemperature"))
        elif isinstance(actuator, Light):
            actuator.turn_on()
            if sensor_readings.get("LightIntensive") < LIGHT_INTENSITY_LOW:
                actuator.set_brightness_level("high")
            elif sensor_readings.get("LightIntensive") < LIGHT_INTENSITY_HIGH:
                actuator.set_brightness_level("medium")
            else:
                actuator.set_brightness_level("low")
        elif isinstance(actuator, Humidifier):
            actuator.turn_on()
            if sensor_readings.get("Humidity") < HUMIDITY_LOW:
                actuator.increase_humidity()
            elif sensor_readings.get("Humidity") > HUMIDITY_HIGH:
                actuator.decrease_humidity()

    # Turn off sensors and actuators after use
    print("\nTurning off all sensors and actuators:")
    for sensor in living_room_sensors:
        sensor.turn_off()
    for actuator in living_room_actuators:
        actuator.turn_off()

if __name__ == "__main__":
    main()