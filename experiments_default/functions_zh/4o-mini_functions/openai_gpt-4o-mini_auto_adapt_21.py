# Based on your functional description and the provided source code, I'll create a `function.py` file that will implement the main function to monitor the sensors and control the actuators according to the specified conditions. The file will include logic to control the air conditioning based on temperature, humidifier based on humidity, and curtains based on light intensity.
# 
# Here's how the `function.py` file will look:

# functions/function.py

from time import sleep
from home.home_plan import home_plan
from home.config import TEMP_HIGH, LIGHT_INTENSITY_HIGH, HUMIDITY_HIGH

def main():
    # Set up the home plan (rooms with sensors and actuators)
    home = home_plan()
    
    while True:
        for room in home:
            # Check temperature sensors and control AC
            temperature_sensors = room.sensors
            indoor_temp_sensor = next((s for s in temperature_sensors if s.sensor_type == "IndoorTemperature"), None)
            ac = next((a for a in room.actuators if a.actuator_type == "AC"), None)

            if indoor_temp_sensor and ac:
                indoor_temp_sensor.turn_on()  # Ensure the sensor is on
                current_temp = indoor_temp_sensor.get_reading()
                if current_temp is not None:
                    if current_temp > TEMP_HIGH:
                        ac.set_target_temperature(26)  # Set target temperature for AC
                        ac.adjust_temperature(current_temp)
                    else:
                        ac.turn_off()
            
            # Check humidity sensors and control humidifier if needed
            humidity_sensors = room.sensors
            humidity_sensor = next((s for s in humidity_sensors if s.sensor_type == "Humidity"), None)
            humidifier = next((a for a in room.actuators if a.actuator_type == "Humidifier"), None)

            if humidity_sensor and humidifier:
                humidity_sensor.turn_on()  # Ensure the sensor is on
                current_humidity = humidity_sensor.get_reading()
                if current_humidity is not None:
                    if current_humidity > HUMIDITY_HIGH:
                        humidifier.decrease_humidity()
                    else:
                        humidifier.increase_humidity()

            # Check light intensity sensors and control curtains
            light_sensors = room.sensors
            light_sensor = next((s for s in light_sensors if s.sensor_type == "LightIntensive"), None)
            curtains = [a for a in room.actuators if a.actuator_type == "Curtain"]

            if light_sensor:
                light_sensor.turn_on()  # Ensure the sensor is on
                current_light = light_sensor.get_reading()
                if current_light is not None:
                    if current_light > LIGHT_INTENSITY_HIGH:
                        for curtain in curtains:
                            curtain.turn_on()  # Open curtains
                    else:
                        for curtain in curtains:
                            curtain.turn_off()  # Close curtains

        sleep(5)  # Wait for some time before the next check

if __name__ == "__main__":
    main()