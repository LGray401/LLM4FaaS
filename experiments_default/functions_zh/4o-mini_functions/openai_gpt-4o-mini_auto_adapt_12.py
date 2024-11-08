# Based on the provided functional description and source code, I'll create the `function.py` file for your smart home project. This file will contain a main function that will utilize the components from the other modules (`sensor.py`, `actuator.py`, `home_plan.py`, and `config.py`) to demonstrate the smart home functionalities, particularly focusing on temperature, humidity, and light intensity.
# 
# Here's the `function.py` file:

# function.py
from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.actuator import Heater, AC, Light, Humidifier
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor

def main():
    # Create the home plan
    home = home_plan()

    # Define the target values based on the functional description
    target_temperature = 22  # Celsius
    target_humidity = (HUMIDITY_LOW + HUMIDITY_HIGH) / 2  # Moderate humidity
    target_light_intensity = (LIGHT_INTENSITY_LOW + LIGHT_INTENSITY_HIGH) / 2  # Weak light intensity

    # Accessing a specific room (for example, "LivingRoom")
    room = get_room(home, "LivingRoom")
    if room:
        # Get sensors and actuators from the room
        temperature_sensor = get_room_sensors(home, "LivingRoom")
        humidity_sensor = get_room_sensors(home, "LivingRoom")
        light_sensor = get_room_sensors(home, "LivingRoom")
        
        heater = get_room_actuators(home, "LivingRoom")[0]  # Assuming the first actuator is the Heater
        ac = get_room_actuators(home, "LivingRoom")[1]      # Assuming the second actuator is the AC
        light = get_room_actuators(home, "LivingRoom")[2]    # Assuming the third actuator is the Light
        humidifier = get_room_actuators(home, "LivingRoom")[3]  # Assuming the fourth actuator is the Humidifier

        # Turn on sensors
        for sensor in temperature_sensor:
            sensor.turn_on()
            current_temperature = sensor.get_reading()

            # Control the heater or AC based on the temperature
            if current_temperature is not None:
                if current_temperature < target_temperature:
                    heater.set_target_temperature(target_temperature)
                    heater.adjust_temperature(current_temperature)
                else:
                    ac.set_target_temperature(target_temperature)
                    ac.adjust_temperature(current_temperature)

        for sensor in humidity_sensor:
            sensor.turn_on()
            current_humidity = sensor.get_reading()

            # Control the humidifier based on humidity
            if current_humidity is not None:
                if current_humidity < HUMIDITY_LOW:
                    humidifier.increase_humidity()
                elif current_humidity > HUMIDITY_HIGH:
                    humidifier.decrease_humidity()

        for sensor in light_sensor:
            sensor.turn_on()
            current_light_intensity = sensor.get_reading()

            # Control the light based on light intensity
            if current_light_intensity is not None:
                if current_light_intensity < LIGHT_INTENSITY_LOW:
                    light.set_brightness_level("high")
                elif LIGHT_INTENSITY_LOW <= current_light_intensity <= LIGHT_INTENSITY_HIGH:
                    light.set_brightness_level("medium")
                else:
                    light.set_brightness_level("low")

        # Turn off sensors after use
        for sensor in temperature_sensor + humidity_sensor + light_sensor:
            sensor.turn_off()

if __name__ == "__main__":
    main()