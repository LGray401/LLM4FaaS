# Based on your functional description and the provided source code, I will create a `function.py` file that implements the main function to regulate temperature, humidity, and light intensity in your smart home project. This file will utilize the classes defined in your `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py` files.
# 
# Here’s the proposed `function.py`:

# functions/function.py

from home.home_plan import home_plan, get_room_sensors, get_room_actuators, get_room
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH
from home.actuator import Heater, AC, Humidifier, Light
import time

def regulate_environment(home):
    # Get the room you want to regulate
    living_room = get_room(home, "LivingRoom")
    
    if living_room:
        # Get sensors
        temperature_sensors = get_room_sensors(home, "LivingRoom")
        humidity_sensors = get_room_sensors(home, "LivingRoom")
        light_sensors = get_room_sensors(home, "LivingRoom")

        # Get actuators
        heater = next((act for act in get_room_actuators(home, "LivingRoom") if isinstance(act, Heater)), None)
        ac = next((act for act in get_room_actuators(home, "LivingRoom") if isinstance(act, AC)), None)
        humidifier = next((act for act in get_room_actuators(home, "LivingRoom") if isinstance(act, Humidifier)), None)
        light = next((act for act in get_room_actuators(home, "LivingRoom") if isinstance(act, Light)), None)

        while True:
            # Get the current temperature reading
            current_temp = None
            for sensor in temperature_sensors:
                if sensor.get_status() == "on":
                    current_temp = sensor.get_reading()
                    break
            
            if current_temp is not None:
                # Adjust temperature
                if current_temp < 26:
                    heater.set_target_temperature(26)
                    heater.adjust_temperature(current_temp)
                elif current_temp > 26:
                    ac.set_target_temperature(26)
                    ac.adjust_temperature(current_temp)

            # Get the current humidity reading
            current_humidity = None
            for sensor in humidity_sensors:
                if sensor.get_status() == "on":
                    current_humidity = sensor.get_reading()
                    break
            
            if current_humidity is not None:
                # Adjust humidity
                if current_humidity < 60:
                    humidifier.turn_on()
                elif current_humidity > 60:
                    humidifier.turn_off()

            # Get light intensity reading
            current_light = None
            for sensor in light_sensors:
                if sensor.get_status() == "on":
                    current_light = sensor.get_reading()
                    break

            # Adjust light based on activity
            if current_light is not None:
                # Assuming we can determine activity mode (working, relaxing, resting)
                activity_mode = "working"  # This would be dynamically set in a real application
                if activity_mode == "working":
                    light.set_brightness_level("high")
                elif activity_mode == "relaxing":
                    light.set_brightness_level("medium")
                elif activity_mode == "resting":
                    light.turn_off()

            time.sleep(5)  # Wait before next regulation check

def main():
    home = home_plan()  # Create the home plan
    regulate_environment(home)  # Start regulating the environment

if __name__ == "__main__":
    main()