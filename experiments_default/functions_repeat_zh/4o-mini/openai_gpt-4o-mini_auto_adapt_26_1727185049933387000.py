# Based on your functional description and the provided source code for your smart home project, I'll create a `function.py` file that will coordinate the sensors and actuators to maintain the desired indoor temperature and humidity, as well as manage the light intensity based on different states (working, relaxing, resting).
# 
# Here's the `function.py` code:

# functions/function.py

from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH
from home.logger_config import logger
import time

def maintain_environment(home):
    # Define target values
    TARGET_TEMPERATURE = 26  # Target temperature in Celsius
    TARGET_HUMIDITY = 60      # Target humidity in percentage

    for room in home:
        # Get the temperature and humidity sensors
        temperature_sensors = get_all_sensors(room.sensors, "IndoorTemperature")
        humidity_sensors = get_all_sensors(room.sensors, "Humidity")
        light_sensors = get_all_sensors(room.sensors, "LightIntensive")

        # Get actuators for heating/cooling and humidifying
        heater = next((act for act in room.actuators if isinstance(act, Heater)), None)
        ac = next((act for act in room.actuators if isinstance(act, AC)), None)
        humidifier = next((act for act in room.actuators if isinstance(act, Humidifier)), None)

        # Maintain temperature
        if temperature_sensors:
            current_temperature = temperature_sensors[0].get_reading()
            if current_temperature is not None:
                if current_temperature < TARGET_TEMPERATURE:
                    if heater:
                        heater.set_target_temperature(TARGET_TEMPERATURE)
                        heater.adjust_temperature(current_temperature)
                elif current_temperature > TARGET_TEMPERATURE:
                    if ac:
                        ac.set_target_temperature(TARGET_TEMPERATURE)
                        ac.adjust_temperature(current_temperature)

        # Maintain humidity
        if humidity_sensors:
            current_humidity = humidity_sensors[0].get_reading()
            if current_humidity is not None:
                if current_humidity < TARGET_HUMIDITY:
                    if humidifier:
                        humidifier.increase_humidity()
                elif current_humidity > TARGET_HUMIDITY:
                    if humidifier:
                        humidifier.decrease_humidity()

        # Control light based on activity
        light_actuator = next((act for act in room.actuators if isinstance(act, Light)), None)
        activity_state = determine_activity_state()  # You need to implement this logic
        
        if light_actuator:
            if activity_state == "working":
                light_actuator.set_brightness_level("high")
            elif activity_state == "relaxing":
                light_actuator.set_brightness_level("low")
            elif activity_state == "resting":
                light_actuator.turn_off()

def determine_activity_state():
    # Placeholder for activity state determination logic
    # This function should return "working", "relaxing", or "resting"
    # For now, we return "working" for demonstration purposes
    return "working"

def main():
    home = home_plan()
    while True:
        maintain_environment(home)
        time.sleep(5)  # Wait for a while before checking again

if __name__ == "__main__":
    main()