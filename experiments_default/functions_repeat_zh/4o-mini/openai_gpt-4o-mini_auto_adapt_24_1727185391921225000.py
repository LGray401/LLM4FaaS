# Based on your functional description and the provided source code, I'll create a `function.py` file that implements the main function to maintain the indoor temperature, humidity, and light intensity as specified.
# 
# Here's how `function.py` will look:

# functions/function.py

from home.home_plan import home_plan
from home.config import TEMP_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_HIGH
from home.actuator import Heater, AC, Humidifier, Light
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor

def maintain_environment(home):
    for room in home:
        # Get relevant sensors and actuators
        temperature_sensor = next((sensor for sensor in room.sensors if isinstance(sensor, IndoorTemperatureSensor)), None)
        humidity_sensor = next((sensor for sensor in room.sensors if isinstance(sensor, HumiditySensor)), None)
        light_sensor = next((sensor for sensor in room.sensors if isinstance(sensor, LightIntensiveSensor)), None)

        heater = next((actuator for actuator in room.actuators if isinstance(actuator, Heater)), None)
        ac = next((actuator for actuator in room.actuators if isinstance(actuator, AC)), None)
        humidifier = next((actuator for actuator in room.actuators if isinstance(actuator, Humidifier)), None)
        light = next((actuator for actuator in room.actuators if isinstance(actuator, Light)), None)

        # Maintain temperature
        if temperature_sensor and heater and ac:
            current_temp = temperature_sensor.get_reading()
            if current_temp is not None:
                if current_temp > TEMP_HIGH:
                    ac.set_target_temperature(TEMP_HIGH)
                    ac.adjust_temperature(current_temp)
                elif current_temp < TEMP_HIGH - 1:  # A threshold to prevent frequent toggling
                    heater.set_target_temperature(TEMP_HIGH)
                    heater.adjust_temperature(current_temp)

        # Maintain humidity
        if humidity_sensor and humidifier:
            current_humidity = humidity_sensor.get_reading()
            if current_humidity is not None:
                if current_humidity > HUMIDITY_LOW:
                    humidifier.decrease_humidity()
                else:
                    humidifier.increase_humidity()

        # Maintain light intensity
        if light_sensor and light:
            current_light = light_sensor.get_reading()
            if current_light is not None:
                if current_light > LIGHT_INTENSITY_HIGH:
                    light.turn_off()
                else:
                    light.turn_on()  # Optional: you might want to set brightness levels instead

def main():
    home = home_plan()
    maintain_environment(home)

if __name__ == "__main__":
    main()