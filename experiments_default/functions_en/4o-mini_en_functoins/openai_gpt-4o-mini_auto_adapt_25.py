# Based on the provided functional description and the existing code files, I will create a `function.py` file that implements the specified logic for managing the smart home functionalities. This will include monitoring the indoor temperature and humidity to control the air conditioning unit and adjusting the curtains based on light intensity.
# 
# Here's the code for `function.py`:

# function.py

from home.home_plan import home_plan
from home.actuator import AC, Curtain
from home.config import TEMP_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    # Create home plan
    home = home_plan()

    # Iterate through each room to monitor sensors and control actuators
    for room in home:
        # Get relevant sensors and actuators
        temperature_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "IndoorTemperature"]
        humidity_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "Humidity"]
        light_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "LightIntensive"]
        
        ac_units = [actuator for actuator in room.actuators if isinstance(actuator, AC)]
        curtains = [actuator for actuator in room.actuators if isinstance(actuator, Curtain)]

        # Check temperature
        for temp_sensor in temperature_sensors:
            temp_sensor.turn_on()  # Ensure the sensor is on
            current_temp = temp_sensor.get_reading()
            if current_temp is not None:
                if current_temp >= TEMP_HIGH:
                    for ac in ac_units:
                        ac.turn_on()  # Turn on AC to cool down
                else:
                    for ac in ac_units:
                        ac.turn_off()  # Turn off AC if temperature is lower than threshold

        # Check humidity
        for humidity_sensor in humidity_sensors:
            humidity_sensor.turn_on()  # Ensure the sensor is on
            current_humidity = humidity_sensor.get_reading()
            if current_humidity is not None:
                if current_humidity < HUMIDITY_LOW:
                    for ac in ac_units:
                        ac.turn_on()  # Turn on AC to humidify
                else:
                    for ac in ac_units:
                        ac.turn_off()  # Turn off AC if humidity is sufficient

        # Check light intensity
        for light_sensor in light_sensors:
            light_sensor.turn_on()  # Ensure the sensor is on
            current_light = light_sensor.get_reading()
            if current_light is not None and current_light > LIGHT_INTENSITY_HIGH:
                for curtain in curtains:
                    curtain.turn_on()  # Draw the curtains
            else:
                for curtain in curtains:
                    curtain.turn_off()  # Open the curtains if light is below threshold


if __name__ == "__main__":
    main()