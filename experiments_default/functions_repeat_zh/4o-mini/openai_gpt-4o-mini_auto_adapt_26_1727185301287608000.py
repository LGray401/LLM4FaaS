# Based on your functional description and the provided source code, I will create a `function.py` file that implements the main function to maintain the indoor temperature at 26°C, humidity at 60%, and control light intensity based on the user's activity (working, relaxing, resting).
# 
# Here's the `function.py` file:

# functions/function.py
from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH
import time

def maintain_environment(home):
    # Get the living room (or any other room where the sensors and actuators are)
    living_room = next((room for room in home if room.name == "LivingRoom"), None)
    
    if living_room is None:
        print("Living room not found in the home plan.")
        return

    # Get sensors and actuators
    temperature_sensor = next((s for s in get_room_sensors(home, "LivingRoom") if s.sensor_type == "IndoorTemperature"), None)
    humidity_sensor = next((s for s in get_room_sensors(home, "LivingRoom") if s.sensor_type == "Humidity"), None)
    light_sensor = next((s for s in get_room_sensors(home, "LivingRoom") if s.sensor_type == "LightIntensive"), None)

    heater = next((a for a in get_room_actuators(home, "LivingRoom") if a.actuator_type == "Heater"), None)
    ac = next((a for a in get_room_actuators(home, "LivingRoom") if a.actuator_type == "AC"), None)
    humidifier = next((a for a in get_room_actuators(home, "LivingRoom") if a.actuator_type == "Humidifier"), None)
    light = next((a for a in get_room_actuators(home, "LivingRoom") if a.actuator_type == "Light"), None)

    # Control loop to maintain temperature, humidity, and light
    while True:
        # Get current readings
        current_temp = temperature_sensor.get_reading() if temperature_sensor else None
        current_humidity = humidity_sensor.get_reading() if humidity_sensor else None
        current_light = light_sensor.get_reading() if light_sensor else None
        
        # Maintain temperature at 26°C
        if current_temp is not None:
            if current_temp < 26:
                if heater:
                    heater.set_target_temperature(26)
                    heater.adjust_temperature(current_temp)
            elif current_temp > 26:
                if ac:
                    ac.set_target_temperature(26)
                    ac.adjust_temperature(current_temp)

        # Maintain humidity at 60%
        if current_humidity is not None:
            if current_humidity < 60:
                if humidifier:
                    humidifier.increase_humidity()
            elif current_humidity > 60:
                if humidifier:
                    humidifier.decrease_humidity()

        # Control light intensity based on activity
        # For simplicity, let's assume we are using a basic mode. You can replace this with actual user input.
        current_activity = "working"  # Options: "working", "relaxing", "resting"
        
        if current_activity == "working":
            if light:
                light.set_brightness_level("high")
        elif current_activity == "relaxing":
            if light:
                light.set_brightness_level("low")
        elif current_activity == "resting":
            if light:
                light.turn_off()
        
        time.sleep(5)  # Check every 5 seconds

def main():
    home = home_plan()
    maintain_environment(home)

if __name__ == "__main__":
    main()