# Here's the `function.py` file located in the 'functions' folder, with the main function to maintain the specified temperature, humidity, and light intensity:

import time
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, AC, Humidifier, Light
from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.config import TEMP_CHANGE_DURATION_WINDOW, TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def maintain_temperature(room):
    sensors = get_room_sensors(home, room)
    actuators = get_room_actuators(home, room)

    temp_sensor = None
    heater = None
    ac = None

    for sensor in sensors:
        if isinstance(sensor, IndoorTemperatureSensor):
            temp_sensor = sensor
            break

    for actuator in actuators:
        if isinstance(actuator, Heater):
            heater = actuator
        elif isinstance(actuator, AC):
            ac = actuator

    if temp_sensor and heater and ac:
        temp_sensor.turn_on()
        heater.set_target_temperature(26)
        ac.set_target_temperature(26)

        while True:
            current_temp = temp_sensor.get_reading()
            if current_temp is not None:
                heater.adjust_temperature(current_temp)
                ac.adjust_temperature(current_temp)
            time.sleep(TEMP_CHANGE_DURATION_WINDOW)
    else:
        print(f"Temperature control components missing in {room}")

def maintain_humidity(room):
    sensors = get_room_sensors(home, room)
    actuators = get_room_actuators(home, room)

    humidity_sensor = None
    humidifier = None

    for sensor in sensors:
        if isinstance(sensor, HumiditySensor):
            humidity_sensor = sensor
            break

    for actuator in actuators:
        if isinstance(actuator, Humidifier):
            humidifier = actuator
            break

    if humidity_sensor and humidifier:
        humidity_sensor.turn_on()

        while True:
            current_humidity = humidity_sensor.get_reading()
            if current_humidity is not None:
                if current_humidity < 60:
                    humidifier.turn_on()
                else:
                    humidifier.turn_off()
            time.sleep(TEMP_CHANGE_DURATION_WINDOW)
    else:
        print(f"Humidity control components missing in {room}")

def adjust_light(room, activity):
    sensors = get_room_sensors(home, room)
    actuators = get_room_actuators(home, room)

    light_sensor = None
    light = None

    for sensor in sensors:
        if isinstance(sensor, LightIntensiveSensor):
            light_sensor = sensor
            break

    for actuator in actuators:
        if isinstance(actuator, Light):
            light = actuator
            break

    if light_sensor and light:
        light_sensor.turn_on()
        light.turn_on()

        if activity == "work":
            light.set_brightness_level("high")
        elif activity == "relax":
            light.set_brightness_level("low")
        elif activity == "rest":
            light.turn_off()
        else:
            print("Invalid activity")
    else:
        print(f"Light control components missing in {room}")

def main():
    global home
    home = home_plan()

    room_name = "LivingRoom"  # Example room
    activities = ["work", "relax", "rest"]

    maintain_temperature(room_name)
    maintain_humidity(room_name)
    adjust_light(room_name, activities[0])  # Example activity

if __name__ == "__main__":
    main()