# Based on your functional description and the provided source code for your smart home project, I will create the `function.py` file. This file will include a main function to manage the sensors and actuators effectively according to the specified requirements for temperature, humidity, and light intensity.
# 
# Here's the implementation of `function.py`:

# functions/function.py

from home.home_plan import home_plan
from home.config import TEMP_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
import time

def main():
    # Initialize the home setup
    home = home_plan()

    while True:
        for room in home:
            # Get current readings from sensors
            temp_sensor = next((s for s in room.sensors if s.sensor_type == "IndoorTemperature"), None)
            humidity_sensor = next((s for s in room.sensors if s.sensor_type == "Humidity"), None)
            light_sensor = next((s for s in room.sensors if s.sensor_type == "LightIntensive"), None)

            current_temperature = temp_sensor.get_reading() if temp_sensor else None
            current_humidity = humidity_sensor.get_reading() if humidity_sensor else None
            current_light_intensity = light_sensor.get_reading() if light_sensor else None

            # Act on temperature readings
            if current_temperature is not None:
                if current_temperature > TEMP_HIGH:
                    heater = next((a for a in room.actuators if a.actuator_type == "Heater"), None)
                    if heater:
                        heater.turn_off()
                    ac = next((a for a in room.actuators if a.actuator_type == "AC"), None)
                    if ac:
                        ac.set_target_temperature(TEMP_HIGH)
                        ac.turn_on()
                else:
                    heater = next((a for a in room.actuators if a.actuator_type == "Heater"), None)
                    if heater:
                        heater.turn_off()
                    ac = next((a for a in room.actuators if a.actuator_type == "AC"), None)
                    if ac:
                        ac.turn_off()

            # Act on humidity readings
            if current_humidity is not None:
                if current_humidity > HUMIDITY_LOW:
                    humidifier = next((a for a in room.actuators if a.actuator_type == "Humidifier"), None)
                    if humidifier:
                        humidifier.decrease_humidity()
                else:
                    humidifier = next((a for a in room.actuators if a.actuator_type == "Humidifier"), None)
                    if humidifier:
                        humidifier.increase_humidity()

            # Act on light intensity readings
            if current_light_intensity is not None:
                if current_light_intensity < LIGHT_INTENSITY_LOW:
                    light = next((a for a in room.actuators if a.actuator_type == "Light"), None)
                    if light:
                        light.turn_on()
                elif current_light_intensity > LIGHT_INTENSITY_HIGH:
                    light = next((a for a in room.actuators if a.actuator_type == "Light"), None)
                    if light:
                        light.turn_off()

        # Sleep for a while before the next reading
        time.sleep(5)  # Adjust the sleep time as needed

if __name__ == "__main__":
    main()