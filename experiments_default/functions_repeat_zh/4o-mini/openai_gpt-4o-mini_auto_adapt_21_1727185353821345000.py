# Based on your functional description and the provided source code files, I'll create a `function.py` file that implements the desired functionalities for your smart home project. The main function will include logic to monitor temperature, humidity, and light intensity, and will activate the necessary actuators when the respective thresholds are crossed.
# 
# Here's the `function.py` file:

# functions/function.py

from home.home_plan import home_plan
from home.config import TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_HIGH
from home.actuator import AC, Humidifier, Curtain
from home.logger_config import logger

def monitor_home():
    # Get the home plan
    home = home_plan()

    for room in home:
        # Get sensors in the room
        temperature_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "IndoorTemperature"]
        humidity_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "Humidity"]
        light_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "LightIntensive"]

        # Check temperature
        for temp_sensor in temperature_sensors:
            temp_sensor.turn_on()  # Ensure sensor is on
            current_temp = temp_sensor.get_reading()
            if current_temp is not None and current_temp > TEMP_HIGH:
                ac_units = [actuator for actuator in room.actuators if isinstance(actuator, AC)]
                for ac in ac_units:
                    ac.set_target_temperature(TEMP_HIGH)
                    ac.adjust_temperature(current_temp)

        # Check humidity
        for humidity_sensor in humidity_sensors:
            humidity_sensor.turn_on()  # Ensure sensor is on
            current_humidity = humidity_sensor.get_reading()
            if current_humidity is not None:
                humidifier_units = [actuator for actuator in room.actuators if isinstance(actuator, Humidifier)]
                if current_humidity < HUMIDITY_LOW:
                    for humidifier in humidifier_units:
                        humidifier.increase_humidity()
                elif current_humidity > HUMIDITY_HIGH:
                    for humidifier in humidifier_units:
                        humidifier.decrease_humidity()

        # Check light intensity
        for light_sensor in light_sensors:
            light_sensor.turn_on()  # Ensure sensor is on
            current_light = light_sensor.get_reading()
            if current_light is not None and current_light > LIGHT_INTENSITY_HIGH:
                curtain_units = [actuator for actuator in room.actuators if isinstance(actuator, Curtain)]
                for curtain in curtain_units:
                    curtain.turn_on()  # Open curtains if light intensity is high

if __name__ == "__main__":
    monitor_home()