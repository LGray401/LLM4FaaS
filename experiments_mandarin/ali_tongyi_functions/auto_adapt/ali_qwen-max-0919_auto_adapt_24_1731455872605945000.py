# Based on your functional description and the provided source code, I will create a `function.py` file that contains the main function to control the smart home system. The main function will ensure that:
# 
# - The indoor temperature does not exceed 26 degrees Celsius.
# - The humidity is kept below 30%.
# - The light intensity is maintained between the levels for opening curtains and turning on lights.
# 
# Here is the `function.py` file:

# functions/function.py

from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC, Heater, Humidifier, Curtain, Light
from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.config import TEMP_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
import time

def control_temperature(room_name):
    room_sensors = get_room_sensors(home, room_name)
    room_actuators = get_room_actuators(home, room_name)

    temp_sensor = next((s for s in room_sensors if isinstance(s, IndoorTemperatureSensor)), None)
    ac = next((a for a in room_actuators if isinstance(a, AC)), None)
    heater = next((a for a in room_actuators if isinstance(a, Heater)), None)

    if temp_sensor:
        current_temp = temp_sensor.get_reading()
        if current_temp is not None:
            if current_temp > TEMP_HIGH:
                if ac:
                    ac.set_target_temperature(TEMP_HIGH)
                    ac.adjust_temperature(current_temp)
            elif current_temp < TEMP_HIGH:
                if ac and ac.status == "on":
                    ac.turn_off()
                if heater:
                    heater.set_target_temperature(TEMP_HIGH)
                    heater.adjust_temperature(current_temp)
            else:
                if ac and ac.status == "on":
                    ac.turn_off()
                if heater and heater.status == "on":
                    heater.turn_off()

def control_humidity(room_name):
    room_sensors = get_room_sensors(home, room_name)
    room_actuators = get_room_actuators(home, room_name)

    humidity_sensor = next((s for s in room_sensors if isinstance(s, HumiditySensor)), None)
    humidifier = next((a for a in room_actuators if isinstance(a, Humidifier)), None)

    if humidity_sensor:
        current_humidity = humidity_sensor.get_reading()
        if current_humidity is not None:
            if current_humidity > HUMIDITY_LOW:
                if humidifier and humidifier.status == "on":
                    humidifier.turn_off()
            elif current_humidity < HUMIDITY_LOW:
                if humidifier:
                    humidifier.increase_humidity()
            else:
                if humidifier and humidifier.status == "on":
                    humidifier.turn_off()

def control_light_intensity(room_name):
    room_sensors = get_room_sensors(home, room_name)
    room_actuators = get_room_actuators(home, room_name)

    light_sensor = next((s for s in room_sensors if isinstance(s, LightIntensiveSensor)), None)
    curtain = next((a for a in room_actuators if isinstance(a, Curtain)), None)
    light = next((a for a in room_actuators if isinstance(a, Light)), None)

    if light_sensor:
        current_light_intensity = light_sensor.get_reading()
        if current_light_intensity is not None:
            if current_light_intensity < LIGHT_INTENSITY_LOW:
                if light:
                    light.turn_on()
                    light.set_brightness_level("high")
                if curtain and curtain.status == "on":
                    curtain.turn_off()
            elif current_light_intensity > LIGHT_INTENSITY_HIGH:
                if light and light.status == "on":
                    light.turn_off()
                if curtain:
                    curtain.turn_on()
            else:
                if light and light.status == "on":
                    light.turn_off()
                if curtain and curtain.status == "on":
                    curtain.turn_off()

def main():
    global home
    home = home_plan()
    rooms = [room.name for room in home]

    while True:
        for room_name in rooms:
            control_temperature(room_name)
            control_humidity(room_name)
            control_light_intensity(room_name)
        time.sleep(10)  # Adjust the sleep time as needed

if __name__ == "__main__":
    main()