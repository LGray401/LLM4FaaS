# Based on the provided functional description and the source code for your smart home project, I will create the `function.py` file located in the `functions` folder. This file will contain the main function that controls the temperature, humidity, and light intensity according to your specifications.
# 
# ### functions/function.py

from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.config import TEMP_HIGH, TEMP_LOW, HUMIDITY_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC, Heater, Humidifier, Light
import time

def main():
    # Initialize home plan
    home = home_plan()

    # Target settings
    target_temp = 26  # Celsius
    target_humidity = 60  # Percentage

    while True:
        # Control indoor temperature
        indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
        for sensor in indoor_temp_sensors:
            sensor.turn_on()
            current_temp = sensor.get_reading()
            if current_temp is not None:
                room_actuators = get_room_actuators(home, sensor.room_name)
                ac = next((actuator for actuator in room_actuators if isinstance(actuator, AC)), None)
                heater = next((actuator for actuator in room_actuators if isinstance(actuator, Heater)), None)
                if current_temp > target_temp and ac:
                    ac.set_target_temperature(target_temp)
                    ac.adjust_temperature(current_temp)
                elif current_temp < target_temp and heater:
                    heater.set_target_temperature(target_temp)
                    heater.adjust_temperature(current_temp)

        # Control humidity
        humidity_sensors = get_all_sensors(home, "Humidity")
        for sensor in humidity_sensors:
            sensor.turn_on()
            current_humidity = sensor.get_reading()
            if current_humidity is not None:
                room_actuators = get_room_actuators(home, sensor.room_name)
                humidifier = next((actuator for actuator in room_actuators if isinstance(actuator, Humidifier)), None)
                if current_humidity < target_humidity and humidifier:
                    humidifier.increase_humidity()
                elif current_humidity > target_humidity and humidifier:
                    humidifier.decrease_humidity()

        # Control light intensity
        light_sensors = get_all_sensors(home, "LightIntensive")
        for sensor in light_sensors:
            sensor.turn_on()
            current_light_intensity = sensor.get_reading()
            if current_light_intensity is not None:
                room_actuators = get_room_actuators(home, sensor.room_name)
                light = next((actuator for actuator in room_actuators if isinstance(actuator, Light)), None)
                if light:
                    light.turn_on()
                    if "work" in sensor.room_name.lower():
                        light.set_brightness_level("high")
                    elif "relax" in sensor.room_name.lower():
                        light.set_brightness_level("medium")
                    elif "rest" in sensor.room_name.lower():
                        light.turn_off()

        # Wait for a while before next reading
        time.sleep(60)  # Adjust the sleep duration as needed

if __name__ == "__main__":
    main()