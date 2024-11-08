# Based on your functional description and the provided source code, I will now provide you with a `function.py` file that contains the main function to control the smart home environment as per your requirements.
# 
# ### function.py

from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.sensor import Sensor
from home.actuator import Actuator, Heater, AC, Light
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH


def main():
    # Initialize the home plan
    home = home_plan()

    # Set the desired temperature, humidity, and light intensity levels
    desired_temperature = 17
    desired_humidity = (HUMIDITY_LOW + HUMIDITY_HIGH) / 2  # Midpoint of acceptable humidity range
    desired_light_intensity = 0  # No light intensity (as per requirement: "不要光照" which means "no light")

    # Get all relevant sensors and actuators
    temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    humidity_sensors = get_all_sensors(home, "Humidity")
    light_sensors = get_all_sensors(home, "LightIntensive")

    heaters = get_all_actuators(home, "Heater")
    acs = get_all_actuators(home, "AC")
    lights = get_all_actuators(home, "Light")

    # Turn on all sensors
    for sensor in temperature_sensors + humidity_sensors + light_sensors:
        sensor.turn_on()

    # Adjust temperature
    for sensor, actuator in zip(temperature_sensors, heaters + acs):
        reading = sensor.get_reading()
        if reading is not None:
            if reading < desired_temperature:
                if isinstance(actuator, Heater):
                    actuator.turn_on()
                    actuator.set_target_temperature(desired_temperature)
                    actuator.adjust_temperature(reading)
                elif isinstance(actuator, AC):
                    actuator.turn_off()  # Turn off AC if it's on and the temperature is below the desired level
            else:
                if isinstance(actuator, AC):
                    actuator.turn_on()
                    actuator.set_target_temperature(desired_temperature)
                    actuator.adjust_temperature(reading)
                elif isinstance(actuator, Heater):
                    actuator.turn_off()  # Turn off heater if it's on and the temperature is above the desired level

    # Adjust humidity (maintain within the acceptable range)
    # Since the requirement only states "湿度正常就行" (humidity should be normal),
    # we will not change the humidity actively but monitor it.
    for sensor in humidity_sensors:
        reading = sensor.get_reading()
        if reading is not None:
            if reading < HUMIDITY_LOW or reading > HUMIDITY_HIGH:
                print(f"Humidity in {sensor.room_name} is out of range: {reading}%")

    # Adjust light intensity (turn off all lights as per requirement)
    for light in lights:
        light.turn_off()

    # Optionally, you can print the status of all sensors and actuators for verification
    for room in home:
        room.print_info()


if __name__ == "__main__":
    main()