# Here is the `function.py` file based on your functional description and the provided source code. This file implements the main function to monitor the indoor temperature, humidity, and light intensity and control the respective actuators (AC, Humidifier, and Light) accordingly.
# 
# ```python
# functions/function.py

from home.home_plan import home_plan
from home.config import TEMP_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_LOW
from home.actuator import AC, Humidifier, Light
from home.logger_config import logger


def main():
    # Create a home plan
    home = home_plan()

    # Iterate through each room
    for room in home:
        # Get sensors in the room
        temp_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "IndoorTemperature"]
        humidity_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "Humidity"]
        light_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "LightIntensive"]

        # Assuming there's only one sensor of each type in each room
        if temp_sensors:
            current_temp = temp_sensors[0].get_reading()
            if current_temp is not None:
                # Control AC based on temperature
                ac_units = [actuator for actuator in room.actuators if isinstance(actuator, AC)]
                for ac in ac_units:
                    if current_temp > TEMP_HIGH:
                        ac.turn_on()
                    else:
                        ac.turn_off()

        if humidity_sensors:
            current_humidity = humidity_sensors[0].get_reading()
            if current_humidity is not None:
                # Control Humidifier based on humidity
                humidifiers = [actuator for actuator in room.actuators if isinstance(actuator, Humidifier)]
                for humidifier in humidifiers:
                    if current_humidity < HUMIDITY_LOW:
                        humidifier.turn_on()
                        humidifier.increase_humidity()
                    else:
                        humidifier.turn_off()

        if light_sensors:
            current_light = light_sensors[0].get_reading()
            if current_light is not None:
                # Control Light based on light intensity
                lights = [actuator for actuator in room.actuators if isinstance(actuator, Light)]
                for light in lights:
                    if current_light < LIGHT_INTENSITY_LOW:
                        light.turn_on()
                        light.set_brightness_level("high")  # Adjust brightness as needed
                    else:
                        light.turn_off()

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation:
# 1. **Home Plan**: The `home_plan` function is called to create the home structure, including rooms, sensors, and actuators.
# 2. **Sensor Readings**: The program checks the readings from the relevant sensors (Indoor Temperature, Humidity, and Light Intensity).
# 3. **Actuator Control**:
#    - **AC**: Turns on if the temperature exceeds the defined high-temperature threshold.
#    - **Humidifier**: Turns on if the humidity is below the defined low-humidity threshold and increases humidity.
#    - **Light**: Turns on if the light intensity is below the defined low-light threshold and adjusts the brightness level.
# 4. **Logging**: Each action is logged for monitoring and debugging purposes.
# 
# This should be placed in the `functions` folder as `function.py`. Make sure that the necessary logging and configurations are properly set up to see the expected outputs when running the program.