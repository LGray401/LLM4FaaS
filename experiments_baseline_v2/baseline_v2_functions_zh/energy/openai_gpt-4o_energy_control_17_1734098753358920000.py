# To create a smart home application focused on energy conservation, we'll build a main application that leverages the provided sensor and actuator classes. The application will monitor environmental conditions using sensors and control actuators to maintain optimal settings for energy efficiency.
# 
# Based on the given functional description "节约能源" (which translates to "energy saving"), our application will perform the following tasks:
# 
# 1. Monitor temperature, humidity, and light levels.
# 2. Adjust heating, cooling, lighting, and other systems to maintain these parameters within efficient ranges, minimizing energy consumption.
# 3. Use the logger for important events and decisions.
# 
# Here's how you can create the application:
# 
# ### main.py
# ```python
import time
from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger

def manage_room_energy(room):
    sensors = get_room_sensors(home, room.name)
    actuators = get_room_actuators(home, room.name)

    temperature_sensor = next((s for s in sensors if s.sensor_type == "IndoorTemperature"), None)
    humidity_sensor = next((s for s in sensors if s.sensor_type == "Humidity"), None)
    light_sensor = next((s for s in sensors if s.sensor_type == "LightIntensive"), None)

    heater = next((a for a in actuators if a.actuator_type == "Heater"), None)
    ac = next((a for a in actuators if a.actuator_type == "AC"), None)
    light = next((a for a in actuators if a.actuator_type == "Light"), None)

    if temperature_sensor:
        temperature_sensor.turn_on()
        current_temp = temperature_sensor.get_reading()
        if current_temp < TEMP_LOW:
            if ac:
                ac.turn_off()
            if heater:
                heater.set_target_temperature(TEMP_LOW)
                heater.turn_on()
        elif current_temp > TEMP_HIGH:
            if heater:
                heater.turn_off()
            if ac:
                ac.set_target_temperature(TEMP_HIGH)
                ac.turn_on()
        else:
            if heater:
                heater.turn_off()
            if ac:
                ac.turn_off()

    if humidity_sensor:
        humidity_sensor.turn_on()
        current_humidity = humidity_sensor.get_reading()
        if current_humidity < HUMIDITY_LOW or current_humidity > HUMIDITY_HIGH:
            logger.info(f"Humidity out of range in {room.name}: {current_humidity}%")

    if light_sensor and light:
        light_sensor.turn_on()
        current_light_intensity = light_sensor.get_reading()
        if current_light_intensity < LIGHT_INTENSITY_LOW:
            light.turn_on()
            light.set_brightness_level("high")
        else:
            light.turn_off()

def main():
    global home
    home = home_plan()
    
    while True:
        for room in home:
            manage_room_energy(room)
        time.sleep(10)  # Wait for a bit before the next cycle

if __name__ == "__main__":
    main()
# ```
# 
# ### Command to Run the Application
# To run this application from a terminal, navigate to the directory containing the `main.py` file and use the following command:
# 
# ```bash
# python3 main.py
# ```
# 
# This script will continuously monitor the sensors and control the actuators in each room to maintain optimal conditions for energy saving. Make sure your Python environment has the necessary modules and logger configuration set up as expected by `logger_config.py`.