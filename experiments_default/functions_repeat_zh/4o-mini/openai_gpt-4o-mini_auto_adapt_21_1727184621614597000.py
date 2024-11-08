# Based on your functional description and the provided source code, I'll create a `function.py` file that includes a main function to monitor the sensors and control the actuators for temperature, humidity, and light intensity as specified.
# 
# Here's the content for `function.py`:

# functions/function.py

from home.home_plan import home_plan
from home.config import TEMP_HIGH, LIGHT_INTENSITY_HIGH
from home.logger_config import logger

def main():
    # Initialize the home plan
    home = home_plan()

    # Monitor sensors and control actuators
    while True:
        for room in home:
            # Check temperature sensors
            temperature_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "IndoorTemperature"]
            for temp_sensor in temperature_sensors:
                current_temp = temp_sensor.get_reading()
                if current_temp is not None and current_temp > TEMP_HIGH:
                    ac_units = [actuator for actuator in room.actuators if actuator.actuator_type == "AC"]
                    for ac in ac_units:
                        ac.set_target_temperature(25)  # Set the AC to a comfortable temperature
                        ac.adjust_temperature(current_temp)

            # Check humidity sensors
            humidity_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "Humidity"]
            for humidity_sensor in humidity_sensors:
                current_humidity = humidity_sensor.get_reading()
                if current_humidity is not None:
                    if current_humidity < 30:
                        humidifiers = [actuator for actuator in room.actuators if actuator.actuator_type == "Humidifier"]
                        for humidifier in humidifiers:
                            humidifier.turn_on()
                            humidifier.increase_humidity()
                    elif current_humidity > 50:
                        humidifiers = [actuator for actuator in room.actuators if actuator.actuator_type == "Humidifier"]
                        for humidifier in humidifiers:
                            humidifier.turn_on()
                            humidifier.decrease_humidity()

            # Check light intensity sensors
            light_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "LightIntensive"]
            for light_sensor in light_sensors:
                current_light = light_sensor.get_reading()
                if current_light is not None and current_light > LIGHT_INTENSITY_HIGH:
                    curtains = [actuator for actuator in room.actuators if actuator.actuator_type == "Curtain"]
                    for curtain in curtains:
                        curtain.turn_on()  # Opens the curtains to block excessive sunlight

        # You might want to add a sleep duration here to avoid an infinite tight loop
        # For example:
        import time
        time.sleep(5)  # Check every 5 seconds

if __name__ == "__main__":
    main()