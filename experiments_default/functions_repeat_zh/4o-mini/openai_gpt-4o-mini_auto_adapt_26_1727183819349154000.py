# Based on your functional description and the provided source code, I've created a `function.py` file that will handle the following functionalities:
# 
# 1. Maintain the indoor temperature at 26°C using a heater or an AC.
# 2. Maintain the indoor humidity at 60% using a humidifier.
# 3. Adjust the light intensity based on the user's activity (bright for work, dim for relaxation, off for rest).
# 
# Here's the `function.py` file:

# functions/function.py
from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH
import time

def maintain_conditions(home):
    while True:
        for room in home:
            # Manage temperature
            temp_sensors = get_room_sensors(home, room.name)
            temp_actuators = get_room_actuators(home, room.name)
            if temp_sensors and temp_actuators:
                indoor_temp_sensor = next((s for s in temp_sensors if s.sensor_type == "IndoorTemperature"), None)
                heater = next((a for a in temp_actuators if a.actuator_type == "Heater"), None)
                ac = next((a for a in temp_actuators if a.actuator_type == "AC"), None)

                if indoor_temp_sensor:
                    current_temp = indoor_temp_sensor.get_reading()
                    if current_temp is not None:
                        if current_temp < 26:
                            if heater:
                                heater.set_target_temperature(26)
                                heater.adjust_temperature(current_temp)
                        elif current_temp > 26:
                            if ac:
                                ac.set_target_temperature(26)
                                ac.adjust_temperature(current_temp)

            # Manage humidity
            humidity_sensors = get_room_sensors(home, room.name)
            humidifier = next((a for a in temp_actuators if a.actuator_type == "Humidifier"), None)

            if humidity_sensors and humidifier:
                humidity_sensor = next((s for s in humidity_sensors if s.sensor_type == "Humidity"), None)
                if humidity_sensor:
                    current_humidity = humidity_sensor.get_reading()
                    if current_humidity is not None:
                        if current_humidity < 60:
                            humidifier.increase_humidity()
                        elif current_humidity > 60:
                            humidifier.decrease_humidity()

            # Manage light intensity
            light_sensors = get_room_sensors(home, room.name)
            light_actuator = next((a for a in temp_actuators if a.actuator_type == "Light"), None)

            if light_sensors and light_actuator:
                light_sensor = next((s for s in light_sensors if s.sensor_type == "LightIntensive"), None)
                if light_sensor:
                    current_light = light_sensor.get_reading()
                    if current_light is not None:
                        # Assuming some method to determine user activity
                        user_activity = determine_user_activity()  # Placeholder for user activity detection
                        if user_activity == "work":
                            light_actuator.set_brightness_level("high")
                        elif user_activity == "relax":
                            light_actuator.set_brightness_level("medium")
                        elif user_activity == "rest":
                            light_actuator.turn_off()

        time.sleep(10)  # wait for a while before the next check

def determine_user_activity():
    # Placeholder function to determine user activity
    # In a real scenario, this could involve more complex logic or sensors
    return "work"  # Just a placeholder; you can modify this as needed

def main():
    home = home_plan()
    maintain_conditions(home)

if __name__ == "__main__":
    main()