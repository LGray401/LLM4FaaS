# Based on the functional description you provided, I'll create the `function.py` file for your smart home project. This file will include a main function that maintains the indoor temperature at 26°C, the humidity at 60%, and adjusts the light intensity based on different activities (working, relaxing, resting).
# 
# Here is the `function.py` file:

# functions/function.py

from home.home_plan import home_plan
from home.config import TEMP_CHANGE_DURATION_WINDOW
from home.actuator import Heater, AC, Humidifier, Light
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
import time

def maintain_environment(home):
    for room in home:
        # Handle Temperature
        temperature_sensor = next((sensor for sensor in room.sensors if isinstance(sensor, IndoorTemperatureSensor)), None)
        heater = next((actuator for actuator in room.actuators if isinstance(actuator, Heater)), None)
        ac = next((actuator for actuator in room.actuators if isinstance(actuator, AC)), None)

        if temperature_sensor and heater and ac:
            current_temperature = temperature_sensor.get_reading()
            if current_temperature is not None:
                if current_temperature < 26:
                    heater.set_target_temperature(26)
                    heater.adjust_temperature(current_temperature)
                elif current_temperature > 26:
                    ac.set_target_temperature(26)
                    ac.adjust_temperature(current_temperature)

        # Handle Humidity
        humidity_sensor = next((sensor for sensor in room.sensors if isinstance(sensor, HumiditySensor)), None)
        humidifier = next((actuator for actuator in room.actuators if isinstance(actuator, Humidifier)), None)

        if humidity_sensor and humidifier:
            current_humidity = humidity_sensor.get_reading()
            if current_humidity is not None:
                if current_humidity < 60:
                    humidifier.increase_humidity()
                elif current_humidity > 60:
                    humidifier.decrease_humidity()

        # Handle Light Intensity
        light_sensor = next((sensor for sensor in room.sensors if isinstance(sensor, LightIntensiveSensor)), None)
        light = next((actuator for actuator in room.actuators if isinstance(actuator, Light)), None)

        if light_sensor and light:
            current_light_intensity = light_sensor.get_reading()
            if current_light_intensity is not None:
                # Example logic for adjusting light based on activity
                activity = "working"  # This should be determined dynamically in a real scenario
                if activity == "working":
                    light.set_brightness_level("high")
                elif activity == "relaxing":
                    light.set_brightness_level("medium")
                elif activity == "resting":
                    light.turn_off()

def main():
    home = home_plan()
    
    while True:
        maintain_environment(home)
        time.sleep(TEMP_CHANGE_DURATION_WINDOW)

if __name__ == "__main__":
    main()