# Based on your functional description and the provided source code, I will now provide a `function.py` file that contains the main function to control and monitor the smart home environment. This main function will initialize the sensors and actuators, turn them on, get readings from the sensors, and adjust the actuators based on the readings.
# 
# Here is the `function.py` file:

from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, AC, Humidifier, Light
from home.home_plan import home_plan, get_room_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger

def main():
    # Initialize the home plan
    home = home_plan()

    # Dictionary to store target values for actuators
    target_values = {
        "Temperature": 26,
        "Humidity": 40,
        "LightIntensity": 80
    }

    # Function to adjust heaters and ACs based on temperature readings
    def adjust_temperature(room_name, current_temp):
        heaters = get_all_actuators(home, "Heater")
        acs = get_all_actuators(home, "AC")
        target_temp = target_values["Temperature"]

        for heater in heaters:
            if heater.room_name == room_name:
                heater.set_target_temperature(target_temp)
                heater.adjust_temperature(current_temp)

        for ac in acs:
            if ac.room_name == room_name:
                ac.set_target_temperature(target_temp)
                ac.adjust_temperature(current_temp)

    # Function to adjust humidifiers based on humidity readings
    def adjust_humidity(room_name, current_humidity):
        humidifiers = get_all_actuators(home, "Humidifier")
        target_humidity = target_values["Humidity"]

        for humidifier in humidifiers:
            if humidifier.room_name == room_name:
                if current_humidity < target_humidity:
                    humidifier.increase_humidity()
                else:
                    humidifier.decrease_humidity()

    # Function to adjust lights based on light intensity readings
    def adjust_light(room_name, current_intensity):
        lights = get_all_actuators(home, "Light")
        target_intensity = target_values["LightIntensity"]  # Assuming this value is a percentage

        for light in lights:
            if light.room_name == room_name:
                # Convert target intensity to appropriate brightness level
                if current_intensity < (target_intensity - 10):
                    light.set_brightness_level("low")
                elif (current_intensity >= (target_intensity - 10)) and (current_intensity < (target_intensity + 10)):
                    light.set_brightness_level("medium")
                else:
                    light.set_brightness_level("high")

    # Loop through each room to get sensor readings and adjust actuators accordingly
    for room in home:
        sensors = get_room_sensors(home, room.name)
        for sensor in sensors:
            sensor.turn_on()
            reading = sensor.get_reading()
            if reading is not None:
                if sensor.sensor_type == "IndoorTemperature":
                    adjust_temperature(room.name, reading)
                elif sensor.sensor_type == "Humidity":
                    adjust_humidity(room.name, reading)
                elif sensor.sensor_type == "LightIntensive":
                    adjust_light(room.name, reading)
            sensor.turn_off()

if __name__ == "__main__":
    main()