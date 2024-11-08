# Based on your functional description and the provided source code for your smart home project, I will create a `function.py` file that implements the main function to maintain the indoor temperature at 26°C, humidity at 60%, and adjust the light intensity based on user activities (working, relaxing, resting).
# 
# Here's the `function.py` file:

# functions/function.py

from home.home_plan import home_plan
from home.config import TEMP_CHANGE_DURATION_WINDOW
import time


def maintain_environment(home):
    while True:
        for room in home:
            # Maintain temperature
            temp_sensor = next((s for s in room.sensors if s.sensor_type == "IndoorTemperature"), None)
            heater = next((a for a in room.actuators if a.actuator_type == "Heater"), None)
            ac = next((a for a in room.actuators if a.actuator_type == "AC"), None)

            if temp_sensor and heater and ac:
                current_temp = temp_sensor.get_reading()
                if current_temp is not None:
                    # Adjust temperature to 26°C
                    if current_temp < 26:
                        heater.set_target_temperature(26)
                        heater.adjust_temperature(current_temp)
                    elif current_temp > 26:
                        ac.set_target_temperature(26)
                        ac.adjust_temperature(current_temp)

            # Maintain humidity
            humidity_sensor = next((s for s in room.sensors if s.sensor_type == "Humidity"), None)
            humidifier = next((a for a in room.actuators if a.actuator_type == "Humidifier"), None)

            if humidity_sensor and humidifier:
                current_humidity = humidity_sensor.get_reading()
                if current_humidity is not None:
                    # Adjust humidity to 60%
                    if current_humidity < 60:
                        humidifier.increase_humidity()
                    elif current_humidity > 60:
                        humidifier.decrease_humidity()

            # Adjust light intensity based on activity
            light_sensor = next((s for s in room.sensors if s.sensor_type == "LightIntensive"), None)
            light = next((a for a in room.actuators if a.actuator_type == "Light"), None)

            if light_sensor and light:
                current_light_intensity = light_sensor.get_reading()
                if current_light_intensity is not None:
                    # Here you will need to define a way to determine activity
                    # For the purpose of this example, let's assume the following:
                    activity = "working"  # This should be dynamically received from user input or sensors

                    if activity == "working":
                        light.set_brightness_level("high")
                    elif activity == "relaxing":
                        light.set_brightness_level("medium")
                    elif activity == "resting":
                        light.turn_off()

        time.sleep(TEMP_CHANGE_DURATION_WINDOW)  # Wait before the next check


def main():
    home = home_plan()
    maintain_environment(home)


if __name__ == "__main__":
    main()