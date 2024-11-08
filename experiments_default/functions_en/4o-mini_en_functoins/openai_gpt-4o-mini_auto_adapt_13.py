# Based on your functional description and the provided source code, I'll create a `function.py` file that will contain a main function to manage the interactions between sensors and actuators in your smart home project. 
# 
# The main function will check the readings from the sensors and control the actuators according to the specified conditions for temperature, humidity, and light intensity.
# 
# Here's the content of `function.py`:

# functions/function.py

from home.home_plan import home_plan
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
import time

def control_home():
    home = home_plan()

    for room in home:
        # Get sensors and actuators in the room
        temperature_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "IndoorTemperature"]
        humidity_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "Humidity"]
        light_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "LightIntensive"]
        
        lights = [actuator for actuator in room.actuators if actuator.actuator_type == "Light"]
        heaters = [actuator for actuator in room.actuators if actuator.actuator_type == "Heater"]
        acs = [actuator for actuator in room.actuators if actuator.actuator_type == "AC"]

        # Control Temperature
        for temp_sensor in temperature_sensors:
            temp_sensor.turn_on()
            current_temp = temp_sensor.get_reading()
            if current_temp is not None:
                for heater in heaters:
                    heater.set_target_temperature(TEMP_HIGH)
                    heater.adjust_temperature(current_temp)
                for ac in acs:
                    ac.set_target_temperature(TEMP_LOW)
                    ac.adjust_temperature(current_temp)

        # Control Humidity
        for humidity_sensor in humidity_sensors:
            humidity_sensor.turn_on()
            current_humidity = humidity_sensor.get_reading()
            if current_humidity is not None:
                if current_humidity < HUMIDITY_LOW:
                    for humidifier in [actuator for actuator in room.actuators if actuator.actuator_type == "Humidifier"]:
                        humidifier.increase_humidity()
                elif current_humidity > HUMIDITY_HIGH:
                    for humidifier in [actuator for actuator in room.actuators if actuator.actuator_type == "Humidifier"]:
                        humidifier.decrease_humidity()

        # Control Light Intensity
        for light_sensor in light_sensors:
            light_sensor.turn_on()
            current_light = light_sensor.get_reading()
            if current_light is not None:
                for light in lights:
                    if current_light < LIGHT_INTENSITY_LOW:
                        light.turn_on()
                        light.set_brightness_level("high")
                    elif current_light > LIGHT_INTENSITY_HIGH:
                        light.turn_off()

        # Brief pause before the next iteration
        time.sleep(2)

if __name__ == "__main__":
    control_home()