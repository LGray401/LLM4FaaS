# Based on your functional description and the provided source code, I will create the `function.py` file that will control the temperature, humidity, and light intensity in your smart home project. 
# 
# Here’s the implementation of `function.py`:

# functions/function.py

from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH
from home.actuator import Heater, AC, Humidifier, Light
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor

def maintain_environment(home):
    # Define target values
    target_temperature = 26  # Celsius
    target_humidity = 60  # Percentage

    for room in home:
        # Get sensors and actuators in the room
        temperature_sensors = get_room_sensors(home, room.name)
        humidity_sensors = get_room_sensors(home, room.name)
        lights = get_room_actuators(home, room.name)

        # Handle temperature
        for temp_sensor in temperature_sensors:
            if isinstance(temp_sensor, IndoorTemperatureSensor):
                current_temperature = temp_sensor.get_reading()
                if current_temperature is not None:
                    # Control heater and AC based on current temperature
                    heater = next((act for act in get_room_actuators(home, room.name) if isinstance(act, Heater)), None)
                    ac = next((act for act in get_room_actuators(home, room.name) if isinstance(act, AC)), None)

                    if heater and ac:
                        heater.set_target_temperature(target_temperature)
                        ac.set_target_temperature(target_temperature)
                        
                        # Adjust heater
                        heater.adjust_temperature(current_temperature)
                        # Adjust AC
                        ac.adjust_temperature(current_temperature)
        
        # Handle humidity
        for humidity_sensor in humidity_sensors:
            if isinstance(humidity_sensor, HumiditySensor):
                current_humidity = humidity_sensor.get_reading()
                if current_humidity is not None:
                    humidifier = next((act for act in get_room_actuators(home, room.name) if isinstance(act, Humidifier)), None)

                    if humidifier:
                        if current_humidity < target_humidity:
                            humidifier.increase_humidity()
                        else:
                            humidifier.decrease_humidity()

        # Handle light intensity based on activities
        light_sensor = next((sensor for sensor in temperature_sensors if isinstance(sensor, LightIntensiveSensor)), None)
        if light_sensor:
            current_light_intensity = light_sensor.get_reading()
            if current_light_intensity is not None:
                for light in lights:
                    if isinstance(light, Light):
                        # Assume we can determine activity type; this could be refined based on actual activity detection
                        activity_type = determine_activity()  # Placeholder function

                        if activity_type == "work":
                            light.set_brightness_level("high")
                        elif activity_type == "relax":
                            light.set_brightness_level("medium")
                        elif activity_type == "rest":
                            light.turn_off()

def determine_activity():
    # Placeholder for actual activity detection logic
    # This can be replaced with a real logic to determine if the user is working, relaxing, or resting
    return "work"  # Example output

def main():
    home = home_plan()
    maintain_environment(home)

if __name__ == "__main__":
    main()