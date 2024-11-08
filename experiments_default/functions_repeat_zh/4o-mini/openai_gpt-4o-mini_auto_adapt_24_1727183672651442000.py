# Based on your functional description and the provided source code, I will create a `function.py` file that includes a main function to manage the smart home environment by maintaining the specified temperature, humidity, and light intensity levels.
# 
# Here’s the `function.py` file:

# functions/function.py

from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
import time

def maintain_environment(home):
    while True:
        for room in home:
            sensors = get_room_sensors(home, room.name)
            actuators = get_room_actuators(home, room.name)

            # Check temperature
            temp_sensor = next((sensor for sensor in sensors if sensor.sensor_type == "IndoorTemperature"), None)
            heater = next((actuator for actuator in actuators if actuator.actuator_type == "Heater"), None)
            ac = next((actuator for actuator in actuators if actuator.actuator_type == "AC"), None)

            if temp_sensor and heater and ac:
                current_temp = temp_sensor.get_reading()
                if current_temp is not None:
                    if current_temp < TEMP_LOW:
                        heater.set_target_temperature(TEMP_HIGH)
                        heater.adjust_temperature(current_temp)
                    elif current_temp > TEMP_HIGH:
                        ac.set_target_temperature(TEMP_LOW)
                        ac.adjust_temperature(current_temp)

            # Check humidity
            humidity_sensor = next((sensor for sensor in sensors if sensor.sensor_type == "Humidity"), None)
            humidifier = next((actuator for actuator in actuators if actuator.actuator_type == "Humidifier"), None)

            if humidity_sensor and humidifier:
                current_humidity = humidity_sensor.get_reading()
                if current_humidity is not None:
                    if current_humidity > HUMIDITY_LOW:
                        humidifier.decrease_humidity()

            # Check light intensity
            light_sensor = next((sensor for sensor in sensors if sensor.sensor_type == "LightIntensive"), None)
            light = next((actuator for actuator in actuators if actuator.actuator_type == "Light"), None)

            if light_sensor and light:
                current_light = light_sensor.get_reading()
                if current_light is not None:
                    if current_light < LIGHT_INTENSITY_LOW:
                        light.turn_on()
                    elif current_light > LIGHT_INTENSITY_HIGH:
                        light.turn_off()

        time.sleep(5)  # Check every 5 seconds

def main():
    home = home_plan()
    maintain_environment(home)

if __name__ == "__main__":
    main()