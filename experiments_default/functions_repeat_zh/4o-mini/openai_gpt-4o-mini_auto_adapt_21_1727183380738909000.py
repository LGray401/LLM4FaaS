# Here's the implementation of the `function.py` file based on the provided functional description and the existing source code:

# functions/function.py

from home.home_plan import home_plan
from home.config import TEMP_HIGH, LIGHT_INTENSITY_HIGH
from home.actuator import AC, Curtain
from home.sensor import IndoorTemperatureSensor, LightIntensiveSensor

def main():
    # Initialize home plan
    home = home_plan()

    # Iterate through rooms and check conditions for temperature, humidity, and light intensity
    for room in home:
        # Check temperature sensors
        temperature_sensors = [sensor for sensor in room.sensors if isinstance(sensor, IndoorTemperatureSensor)]
        for temp_sensor in temperature_sensors:
            temp_sensor.turn_on()  # Ensure the sensor is on
            current_temp = temp_sensor.get_reading()
            if current_temp is not None and current_temp > TEMP_HIGH:
                ac_units = [actuator for actuator in room.actuators if isinstance(actuator, AC)]
                for ac in ac_units:
                    ac.set_target_temperature(26)  # Set AC target temperature
                    ac.adjust_temperature(current_temp)

        # Check light intensity sensors
        light_sensors = [sensor for sensor in room.sensors if isinstance(sensor, LightIntensiveSensor)]
        for light_sensor in light_sensors:
            light_sensor.turn_on()  # Ensure the sensor is on
            current_light = light_sensor.get_reading()
            if current_light is not None and current_light > LIGHT_INTENSITY_HIGH:
                curtain_units = [actuator for actuator in room.actuators if isinstance(actuator, Curtain)]
                for curtain in curtain_units:
                    curtain.turn_on()  # Open curtains

if __name__ == "__main__":
    main()