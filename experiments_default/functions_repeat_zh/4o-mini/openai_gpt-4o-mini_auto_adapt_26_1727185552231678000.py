# Based on the provided functional description and existing code, I'll create a `function.py` file that implements the main function to maintain the indoor temperature at 26°C, humidity at 60%, and manage light intensity based on the activities (working, relaxing, resting).
# 
# Here's how the `function.py` file might look:

# function.py
import time
from home.home_plan import home_plan
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH
from home.actuator import Heater, AC, Humidifier, Light
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor

def main():
    # Initialize the home plan
    home = home_plan()

    # Assume we are monitoring the Living Room for this example
    living_room = next(room for room in home if room.name == "LivingRoom")

    # Get relevant sensors and actuators
    temperature_sensor = next(sensor for sensor in living_room.sensors if isinstance(sensor, IndoorTemperatureSensor))
    humidity_sensor = next(sensor for sensor in living_room.sensors if isinstance(sensor, HumiditySensor))
    light_sensor = next(sensor for sensor in living_room.sensors if isinstance(sensor, LightIntensiveSensor))
    
    heater = next(actuator for actuator in living_room.actuators if isinstance(actuator, Heater))
    ac = next(actuator for actuator in living_room.actuators if isinstance(actuator, AC))
    humidifier = next(actuator for actuator in living_room.actuators if isinstance(actuator, Humidifier))
    light = next(actuator for actuator in living_room.actuators if isinstance(actuator, Light))

    # Set target values
    target_temperature = 26
    target_humidity = 60

    # Main control loop
    while True:
        # Get current readings
        current_temperature = temperature_sensor.get_reading()
        current_humidity = humidity_sensor.get_reading()
        current_light_intensity = light_sensor.get_reading()

        # Control temperature
        if current_temperature is not None:
            if current_temperature < target_temperature:
                heater.set_target_temperature(target_temperature)
                heater.adjust_temperature(current_temperature)
            elif current_temperature > target_temperature:
                ac.set_target_temperature(target_temperature)
                ac.adjust_temperature(current_temperature)

        # Control humidity
        if current_humidity is not None:
            if current_humidity < target_humidity:
                humidifier.increase_humidity()
            elif current_humidity > target_humidity:
                humidifier.decrease_humidity()

        # Control light intensity based on user activity
        # Here, I am setting a simple simulation of activities
        activity = input("Enter activity (work/relax/rest): ").strip().lower()
        if activity == "work":
            light.set_brightness_level("high")
        elif activity == "relax":
            light.set_brightness_level("medium")
        elif activity == "rest":
            light.turn_off()

        # Wait for a while before the next reading
        time.sleep(5)

if __name__ == "__main__":
    main()