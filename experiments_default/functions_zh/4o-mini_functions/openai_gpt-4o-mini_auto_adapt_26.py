# Based on your functional description and the provided source code, I'll create the `function.py` file. The purpose of this file will be to manage the smart home functionality related to temperature, humidity, and light intensity as described.
# 
# Here's the structure of the `function.py` file that you can place in the `functions` folder:

from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, AC, Light, Humidifier

def maintain_temperature(home):
    room = get_room(home, "LivingRoom")
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

def maintain_humidity(home):
    room = get_room(home, "LivingRoom")
    humidity_sensor = next((sensor for sensor in room.sensors if isinstance(sensor, HumiditySensor)), None)
    humidifier = next((actuator for actuator in room.actuators if isinstance(actuator, Humidifier)), None)

    if humidity_sensor and humidifier:
        current_humidity = humidity_sensor.get_reading()

        if current_humidity is not None:
            if current_humidity < 60:
                humidifier.increase_humidity()
            elif current_humidity > 60:
                humidifier.decrease_humidity()

def manage_light_intensity(home, activity_type):
    room = get_room(home, "LivingRoom")
    light_sensor = next((sensor for sensor in room.sensors if isinstance(sensor, LightIntensiveSensor)), None)
    light = next((actuator for actuator in room.actuators if isinstance(actuator, Light)), None)

    if light_sensor and light:
        light_sensor.get_reading()  # Get current light intensity reading

        if activity_type == 'work':
            light.turn_on()
            light.set_brightness_level('high')
        elif activity_type == 'relax':
            light.turn_on()
            light.set_brightness_level('low')
        elif activity_type == 'rest':
            light.turn_off()

def main():
    home = home_plan()
    
    # Maintain Temperature
    maintain_temperature(home)
    
    # Maintain Humidity
    maintain_humidity(home)
    
    # Example of managing light intensity based on activity
    current_activity = 'work'  # This could be dynamic based on user input or automation
    manage_light_intensity(home, current_activity)

if __name__ == "__main__":
    main()