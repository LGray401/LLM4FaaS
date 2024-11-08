# Based on the functional description and the provided source code, I will create the `function.py` file to control the temperature, humidity, and light intensity in the home. Here is the implementation of `function.py`.
# 
# ### function.py

from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, AC, Humidifier, Light
import time

def control_temperature(room):
    sensors = get_room_sensors(home, room)
    actuators = get_room_actuators(home, room)
    
    temp_sensor = next((sensor for sensor in sensors if isinstance(sensor, IndoorTemperatureSensor)), None)
    heater = next((actuator for actuator in actuators if isinstance(actuator, Heater)), None)
    ac = next((actuator for actuator in actuators if isinstance(actuator, AC)), None)

    if temp_sensor and heater and ac:
        temp_sensor.turn_on()
        current_temp = temp_sensor.get_reading()
        
        heater.set_target_temperature(26)
        ac.set_target_temperature(26)
        
        heater.adjust_temperature(current_temp)
        ac.adjust_temperature(current_temp)

def control_humidity(room):
    sensors = get_room_sensors(home, room)
    actuators = get_room_actuators(home, room)
    
    humidity_sensor = next((sensor for sensor in sensors if isinstance(sensor, HumiditySensor)), None)
    humidifier = next((actuator for actuator in actuators if isinstance(actuator, Humidifier)), None)

    if humidity_sensor and humidifier:
        humidity_sensor.turn_on()
        current_humidity = humidity_sensor.get_reading()
        
        if current_humidity < 60:
            humidifier.turn_on()
        else:
            humidifier.turn_off()

def control_light(room, mode):
    sensors = get_room_sensors(home, room)
    actuators = get_room_actuators(home, room)
    
    light_sensor = next((sensor for sensor in sensors if isinstance(sensor, LightIntensiveSensor)), None)
    lights = [actuator for actuator in actuators if isinstance(actuator, Light)]

    if light_sensor and lights:
        light_sensor.turn_on()
        current_light_intensity = light_sensor.get_reading()
        
        for light in lights:
            light.turn_on()
            if mode == "work":
                light.set_brightness_level("high")
            elif mode == "relax":
                light.set_brightness_level("medium")
            elif mode == "rest":
                light.turn_off()

def main():
    global home
    home = home_plan()

    rooms = ["LivingRoom", "Bedroom", "Kitchen", "Bathroom", "Balcony"]
    
    for room in rooms:
        control_temperature(room)
        control_humidity(room)
        control_light(room, "work")  # Change mode to "relax" or "rest" as needed

if __name__ == "__main__":
    main()