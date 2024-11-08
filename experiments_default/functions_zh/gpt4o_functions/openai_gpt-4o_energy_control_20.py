# Based on your project setup and functional description, I'll create the `function.py` file that will reside in the `functions` folder. This file will contain the main function which will utilize the provided components to adjust indoor temperature, humidity, and light intensity.
# 
# Here is the `function.py`:

from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, AC, Humidifier, Light
from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def adjust_environment(room_name):
    home = home_plan()
    room = get_room(home, room_name)
    
    if not room:
        return

    sensors = get_room_sensors(home, room_name)
    actuators = get_room_actuators(home, room_name)

    temp_sensor = None
    humidity_sensor = None
    light_sensor = None

    heater = None
    ac = None
    humidifier = None
    light = None

    for sensor in sensors:
        if isinstance(sensor, IndoorTemperatureSensor):
            temp_sensor = sensor
        elif isinstance(sensor, HumiditySensor):
            humidity_sensor = sensor
        elif isinstance(sensor, LightIntensiveSensor):
            light_sensor = sensor

    for actuator in actuators:
        if isinstance(actuator, Heater):
            heater = actuator
        elif isinstance(actuator, AC):
            ac = actuator
        elif isinstance(actuator, Humidifier):
            humidifier = actuator
        elif isinstance(actuator, Light):
            light = actuator

    if temp_sensor and heater and ac:
        temp_sensor.turn_on()
        current_temp = temp_sensor.get_reading()
        heater.set_target_temperature(TEMP_HIGH)
        ac.set_target_temperature(TEMP_LOW)
        heater.adjust_temperature(current_temp)
        ac.adjust_temperature(current_temp)

    if humidity_sensor and humidifier:
        humidity_sensor.turn_on()
        current_humidity = humidity_sensor.get_reading()
        if current_humidity < HUMIDITY_LOW:
            humidifier.turn_on()
            humidifier.increase_humidity()
        elif current_humidity > HUMIDITY_HIGH:
            humidifier.turn_on()
            humidifier.decrease_humidity()
        else:
            humidifier.turn_off()

    if light_sensor and light:
        light_sensor.turn_on()
        current_light_intensity = light_sensor.get_reading()
        light.turn_on()
        if current_light_intensity < LIGHT_INTENSITY_LOW:
            light.set_brightness_level("high")
        elif current_light_intensity > LIGHT_INTENSITY_HIGH:
            light.set_brightness_level("low")
        else:
            light.set_brightness_level("medium")

if __name__ == "__main__":
    room_name = "LivingRoom"  # Example room name
    adjust_environment(room_name)