# Based on the functional description and the provided source code files, I'll create a `function.py` file for your smart home project. This file will contain a main function that monitors the sensors for temperature, humidity, and light intensity, and will control the actuators accordingly to maintain the specified conditions.
# 
# Here’s how the `function.py` file will look:

# function.py
from home.home_plan import home_plan
from home.config import TEMP_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from time import sleep

def main():
    # Initialize the home plan
    home = home_plan()

    while True:
        for room in home:
            # Get sensors and actuators in the room
            temp_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "IndoorTemperature"]
            humidity_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "Humidity"]
            light_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "LightIntensive"]
            heaters = [actuator for actuator in room.actuators if actuator.actuator_type == "Heater"]
            acs = [actuator for actuator in room.actuators if actuator.actuator_type == "AC"]
            lights = [actuator for actuator in room.actuators if actuator.actuator_type == "Light"]

            # Check temperature
            for sensor in temp_sensors:
                current_temp = sensor.get_reading()
                if current_temp is not None:
                    for heater in heaters:
                        heater.set_target_temperature(TEMP_HIGH)
                        heater.adjust_temperature(current_temp)
                    for ac in acs:
                        ac.set_target_temperature(TEMP_HIGH)
                        ac.adjust_temperature(current_temp)

            # Check humidity
            for sensor in humidity_sensors:
                current_humidity = sensor.get_reading()
                if current_humidity is not None:
                    for h in heaters:
                        if current_humidity > HUMIDITY_LOW:
                            h.turn_on()  # Turn on heater to decrease humidity
                        else:
                            h.turn_off()
                    for h in acs:
                        if current_humidity > HUMIDITY_LOW:
                            h.turn_on()  # Turn on AC to decrease humidity
                        else:
                            h.turn_off()

            # Check light intensity
            for sensor in light_sensors:
                current_light = sensor.get_reading()
                if current_light is not None:
                    for light in lights:
                        if current_light < LIGHT_INTENSITY_LOW:
                            light.turn_on()  # Turn on light if light intensity is low
                        elif current_light > LIGHT_INTENSITY_HIGH:
                            light.turn_off()  # Turn off light if light intensity is high

        sleep(5)  # Wait for a few seconds before checking again

if __name__ == "__main__":
    main()