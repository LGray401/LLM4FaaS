# Based on your functional description and the provided source code, here is the `function.py` file that implements the main function for your smart home project. This function will monitor the sensors and control the actuators based on the specified conditions for temperature, humidity, and light intensity.

# functions/function.py

from home.home_plan import home_plan
from home.config import TEMP_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_LOW
from home.actuator import AC, Humidifier, Light
from home.logger_config import logger

def main():
    # Initialize the home plan with rooms and their components
    home = home_plan()

    # Loop through each room to monitor sensors and control actuators
    for room in home:
        # Check for Indoor Temperature Sensor
        indoor_temp_sensor = next((sensor for sensor in room.sensors if sensor.sensor_type == "IndoorTemperature"), None)
        if indoor_temp_sensor:
            indoor_temp_sensor.turn_on()  # Ensure the sensor is on
            current_temp = indoor_temp_sensor.get_reading()
            if current_temp is not None and current_temp > TEMP_HIGH:
                # Control the AC and close the windows
                ac = next((actuator for actuator in room.actuators if isinstance(actuator, AC)), None)
                window = next((actuator for actuator in room.actuators if isinstance(actuator, Window)), None)
                if ac:
                    ac.turn_on()
                if window:
                    window.turn_off()  # Assume turning off means closing the window
                logger.info(f"AC turned on and windows closed in {room.name} due to high temperature.")

        # Check for Humidity Sensor
        humidity_sensor = next((sensor for sensor in room.sensors if sensor.sensor_type == "Humidity"), None)
        if humidity_sensor:
            humidity_sensor.turn_on()  # Ensure the sensor is on
            current_humidity = humidity_sensor.get_reading()
            if current_humidity is not None and current_humidity < HUMIDITY_LOW:
                # Control the Humidifier
                humidifier = next((actuator for actuator in room.actuators if isinstance(actuator, Humidifier)), None)
                if humidifier:
                    humidifier.turn_on()
                    humidifier.increase_humidity()
                logger.info(f"Humidifier turned on in {room.name} due to low humidity.")

        # Check for Light Intensity Sensor
        light_sensor = next((sensor for sensor in room.sensors if sensor.sensor_type == "LightIntensive"), None)
        if light_sensor:
            light_sensor.turn_on()  # Ensure the sensor is on
            current_light = light_sensor.get_reading()
            if current_light is not None and current_light < LIGHT_INTENSITY_LOW:
                # Control the Lights
                lights = [actuator for actuator in room.actuators if isinstance(actuator, Light)]
                for light in lights:
                    light.turn_on()
                    light.set_brightness_level("high")  # Adjust brightness as needed
                logger.info(f"Lights turned on in {room.name} due to low light intensity.")

if __name__ == "__main__":
    main()