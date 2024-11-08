# Based on the functional description and the provided source code, it seems like you want to create a `function.py` file that will handle the temperature, humidity, and light intensity in your smart home project.
#
# Here's a basic outline of what the `function.py` file could look like:
#
# ```python
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, AC, Light, NotificationSender
from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    home = home_plan()

    # Iterate over each room
    for room in home:
        # Get all sensors and actuators in the room
        sensors = get_room_sensors(home, room.name)
        actuators = get_room_actuators(home, room.name)

        # Iterate over each sensor in the room
        for sensor in sensors:
            # Handle temperature
            if isinstance(sensor, IndoorTemperatureSensor):
                handle_temperature(sensor, actuators)
            # Handle humidity
            elif isinstance(sensor, HumiditySensor):
                handle_humidity(sensor, actuators)
            # Handle light intensity
            elif isinstance(sensor, LightIntensiveSensor):
                handle_light_intensity(sensor, actuators)

def handle_temperature(sensor, actuators):
    temperature = sensor.get_reading()
    if temperature is not None:
        if temperature < TEMP_LOW:
            # Too cold, turn on heater
            for actuator in actuators:
                if isinstance(actuator, Heater):
                    actuator.turn_on()
        elif temperature > TEMP_HIGH:
            # Too hot, turn on AC
            for actuator in actuators:
                if isinstance(actuator, AC):
                    actuator.turn_on()

def handle_humidity(sensor, actuators):
    humidity = sensor.get_reading()
    if humidity is not None:
        if humidity < HUMIDITY_LOW:
            # Too dry, send notification
            for actuator in actuators:
                if isinstance(actuator, NotificationSender):
                    actuator.notification_sender("小g 太干了")
        elif humidity > HUMIDITY_HIGH:
            # Too humid, send notification
            for actuator in actuators:
                if isinstance(actuator, NotificationSender):
                    actuator.notification_sender("小g 太湿了")

def handle_light_intensity(sensor, actuators):
    light_intensity = sensor.get_reading()
    if light_intensity is not None:
        if light_intensity < LIGHT_INTENSITY_LOW:
            # Too dark, turn on light
            for actuator in actuators:
                if isinstance(actuator, Light):
                    actuator.turn_on()
        elif light_intensity > LIGHT_INTENSITY_HIGH:
            # Too bright, send notification
            for actuator in actuators:
                if isinstance(actuator, NotificationSender):
                    actuator.notification_sender("小g 太亮了")

if __name__ == "__main__":
    main()
# ```
#
# This script will iterate over each room in your home, get all the sensors and actuators in that room, and then handle the temperature, humidity, and light intensity based on the readings from the sensors. If the temperature is too low, it will turn on the heater. If the temperature is too high, it will turn on the AC. If the humidity is too low or too high, it will send a notification. If the light intensity is too low, it will turn on the light. If the light intensity is too high, it will send a notification.
#
# Please note that this is a basic implementation and might need to be adjusted based on your specific needs.