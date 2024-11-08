# Based on the functional description and the provided source code files, I've created the `function.py` file that contains the main function to implement the required smart home features. This implementation will monitor the temperature, humidity, and light intensity, and take actions accordingly.
# 
# Here is the content for `function.py`:
# 
# ```python
# function.py
from home.home_plan import home_plan
from home.config import TEMP_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_LOW
from home.actuator import AC, Humidifier, Light
from home.logger_config import logger


def control_home_environment(home):
    for room in home:
        # Check temperature sensors
        temp_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "IndoorTemperature"]
        current_temp = temp_sensors[0].get_reading() if temp_sensors else None

        # Check humidity sensors
        humidity_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "Humidity"]
        current_humidity = humidity_sensors[0].get_reading() if humidity_sensors else None

        # Check light intensity sensors
        light_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "LightIntensive"]
        current_light = light_sensors[0].get_reading() if light_sensors else None

        # Control AC for temperature
        if current_temp is not None:
            if current_temp > TEMP_HIGH:
                ac = next((actuator for actuator in room.actuators if isinstance(actuator, AC)), None)
                if ac:
                    ac.turn_on()
                    logger.info(f"AC turned ON in {room.name} due to high temperature.")
            else:
                ac = next((actuator for actuator in room.actuators if isinstance(actuator, AC)), None)
                if ac:
                    ac.turn_off()
                    logger.info(f"AC turned OFF in {room.name} as temperature is normal.")

        # Control Humidifier for humidity
        if current_humidity is not None:
            if current_humidity < HUMIDITY_LOW:
                humidifier = next((actuator for actuator in room.actuators if isinstance(actuator, Humidifier)), None)
                if humidifier:
                    humidifier.increase_humidity()
                    logger.info(f"Humidifier turned ON in {room.name} due to low humidity.")
            else:
                humidifier = next((actuator for actuator in room.actuators if isinstance(actuator, Humidifier)), None)
                if humidifier:
                    humidifier.decrease_humidity()
                    logger.info(f"Humidifier turned OFF in {room.name} as humidity is normal.")

        # Control Light for light intensity
        if current_light is not None:
            light = next((actuator for actuator in room.actuators if isinstance(actuator, Light)), None)
            if light:
                if current_light < LIGHT_INTENSITY_LOW:
                    light.turn_on()
                    logger.info(f"Light turned ON in {room.name} due to low light intensity.")
                else:
                    light.turn_off()
                    logger.info(f"Light turned OFF in {room.name} as light intensity is sufficient.")


def main():
    home = home_plan()
    control_home_environment(home)


if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation of `function.py`:
# 
# - **Imports**: The necessary classes and constants are imported from the other files in the project.
# - **control_home_environment function**: This function iterates through each room in the home, checking the readings from the sensors and controlling the actuators based on the conditions specified:
#   - If the indoor temperature exceeds the defined threshold, the AC is turned on; otherwise, it is turned off.
#   - If the humidity is below an acceptable level, the humidifier is activated; otherwise, it is deactivated.
#   - If the light intensity is low, the lights are turned on; otherwise, they are turned off.
# - **main function**: This function initializes the home plan and then calls the control function to manage the environment based on sensor readings.
# - **Entry Point**: The script runs the main function when executed directly.
# 
# This `function.py` file should be placed in the `functions` folder of your smart home project.