# Based on your functional description and the provided source code, I'll create a `function.py` file that utilizes your sensors and actuators to address the conditions of temperature, humidity, and light intensity in the home. The main function will check each room's sensor readings and activate the appropriate actuators when the conditions are met.
# 
# Here's the `function.py`:
# 
# ```python
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC, Heater, Humidifier, Light, NotificationSender
from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
import time

def control_temperature(room_sensors, room_actuators):
    for sensor in room_sensors:
        if isinstance(sensor, IndoorTemperatureSensor):
            temperature = sensor.get_reading()
            if temperature is not None:
                for actuator in room_actuators:
                    if isinstance(actuator, AC):
                        if temperature > TEMP_HIGH:
                            print("屋里太热了")
                            actuator.turn_on()
                        else:
                            actuator.turn_off()
                    elif isinstance(actuator, Heater):
                        if temperature < TEMP_LOW:
                            actuator.turn_on()
                        else:
                            actuator.turn_off()

def control_humidity(room_sensors, room_actuators):
    for sensor in room_sensors:
        if isinstance(sensor, HumiditySensor):
            humidity = sensor.get_reading()
            if humidity is not None:
                for actuator in room_actuators:
                    if isinstance(actuator, Humidifier):
                        if humidity < HUMIDITY_LOW:
                            print("屋里有点干")
                            actuator.turn_on()
                        else:
                            actuator.turn_off()

def control_light_intensity(room_sensors, room_actuators):
    for sensor in room_sensors:
        if isinstance(sensor, LightIntensiveSensor):
            light_intensity = sensor.get_reading()
            if light_intensity is not None:
                for actuator in room_actuators:
                    if isinstance(actuator, Light):
                        if light_intensity < LIGHT_INTENSITY_LOW:
                            print("屋里太暗了")
                            actuator.turn_on()
                        else:
                            actuator.turn_off()

def main():
    home = home_plan()  # Assuming home_plan initializes and returns the setup
    for room in home:
        room_sensors = get_room_sensors(home, room.name)
        room_actuators = get_room_actuators(home, room.name)
        if room_sensors and room_actuators:
            control_temperature(room_sensors, room_actuators)
            control_humidity(room_sensors, room_actuators)
            control_light_intensity(room_sensors, room_actuators)
        time.sleep(1)  # Wait a bit before next room check to simulate real-time processing

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation:
# - The `main` function loops through each room in the home, retrieves the sensors and actuators, and calls functions to check and adjust temperature, humidity, and light intensity.
# - Each control function (`control_temperature`, `control_humidity`, `control_light_intensity`) checks the respective sensor readings and triggers the corresponding actuators if they are not within the desired ranges.
# - The `print` statements are used in accordance with your functional description to output the conditions in Chinese.
# - The `time.sleep(1)` is used to simulate a delay between processing each room, which might be useful in a real-time scenario.
# 
# This setup should help you manage the smart home environment based on the conditions specified. Adjust thresholds and durations as needed in your `config.py`.