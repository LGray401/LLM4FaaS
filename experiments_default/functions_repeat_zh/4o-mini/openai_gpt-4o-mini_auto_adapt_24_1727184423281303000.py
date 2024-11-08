# Based on your functional description and the provided code files, I'll create a `function.py` file that will implement the main functionality for managing the temperature, humidity, and light intensity in the smart home. The main function will periodically check the readings from the sensors and control the actuators accordingly to maintain the desired conditions.
# 
# Here is how `function.py` might look:

# functions/function.py
import time
from home.home_plan import home_plan
from home.config import TEMP_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_LOW

def maintain_environment(home):
    while True:
        for room in home:
            # Check and manage temperature
            temperature_sensor = next((s for s in room.sensors if s.sensor_type == "IndoorTemperature"), None)
            heater = next((a for a in room.actuators if a.actuator_type == "Heater"), None)
            ac = next((a for a in room.actuators if a.actuator_type == "AC"), None)
            
            if temperature_sensor:
                current_temp = temperature_sensor.get_reading()
                if current_temp is not None:
                    if current_temp > TEMP_HIGH:
                        if ac:
                            ac.set_target_temperature(TEMP_HIGH)
                            ac.adjust_temperature(current_temp)
                    elif current_temp < TEMP_LOW:
                        if heater:
                            heater.set_target_temperature(TEMP_LOW)
                            heater.adjust_temperature(current_temp)

            # Check and manage humidity
            humidity_sensor = next((s for s in room.sensors if s.sensor_type == "Humidity"), None)
            humidifier = next((a for a in room.actuators if a.actuator_type == "Humidifier"), None)

            if humidity_sensor:
                current_humidity = humidity_sensor.get_reading()
                if current_humidity is not None:
                    if current_humidity > HUMIDITY_LOW and humidifier:
                        humidifier.decrease_humidity()

            # Check and manage light intensity
            light_sensor = next((s for s in room.sensors if s.sensor_type == "LightIntensive"), None)
            light = next((a for a in room.actuators if a.actuator_type == "Light"), None)

            if light_sensor:
                current_light = light_sensor.get_reading()
                if current_light is not None:
                    if current_light < LIGHT_INTENSITY_LOW and light:
                        light.turn_on()
                    else:
                        light.turn_off()

        time.sleep(5)  # Check every 5 seconds

def main():
    home = home_plan()
    maintain_environment(home)

if __name__ == "__main__":
    main()