# Based on the functional description you provided and the source code structure, I'll guide you on how to create a smart home application. This application will use the sensor and actuator classes to automatically control the air conditioning and curtains based on the conditions you described.
# 
# ### Functional Requirements Recap:
# 1. **Temperature Management**: Turn on the air conditioner to cool the room when the indoor temperature exceeds 26°C.
# 2. **Humidity Management**: Turn on the air conditioner to humidify the room when the indoor humidity drops below 36%.
# 3. **Light Management**: Close the curtains when the indoor light intensity exceeds 80.
# 
# ### Implementation Plan:
# 1. Use the `sensor.py` file to simulate sensor readings.
# 2. Use the `actuator.py` to control the actuators based on the sensor readings.
# 3. Use the `home_plan.py` to set up the home environment with rooms, sensors, and actuators.
# 4. Write a new `main.py` script to run the application and implement the logic for controlling the actuators based on the sensor readings.
# 
# ### Code Implementation:
# 
# Create a new file named `main.py` in the same directory as the other files.
# 
# ```python
import time
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC, Curtain
from home.home_plan import home_plan, get_room_sensors, get_room_actuators

# Thresholds based on your functional description
TEMP_THRESHOLD = 26.0  # Celsius
HUMIDITY_THRESHOLD = 36.0  # Percent
LIGHT_THRESHOLD = 80.0  # Lux

def control_room(room_name):
    # Get home plan
    home = home_plan()

    # Get sensors and actuators for the room
    sensors = get_room_sensors(home, room_name)
    actuators = get_room_actuators(home, room_name)

    # Find specific sensors
    temp_sensor = next((s for s in sensors if isinstance(s, IndoorTemperatureSensor)), None)
    humidity_sensor = next((s for s in sensors if isinstance(s, HumiditySensor)), None)
    light_sensor = next((s for s in sensors if isinstance(s, LightIntensiveSensor)), None)

    # Find specific actuators
    ac = next((a for a in actuators if isinstance(a, AC)), None)
    curtain = next((a for a in actuators if isinstance(a, Curtain)), None)

    # Turn on sensors
    for sensor in [temp_sensor, humidity_sensor, light_sensor]:
        if sensor:
            sensor.turn_on()

    # Check conditions and control actuators
    while True:
        if temp_sensor:
            temp_reading = temp_sensor.get_reading()
            if temp_reading and temp_reading > TEMP_THRESHOLD:
                if ac:
                    print(f"Temperature is {temp_reading}°C. Turning on AC for cooling.")
                    ac.turn_on()
                    ac.set_target_temperature(TEMP_THRESHOLD)
            else:
                if ac:
                    ac.turn_off()

        if humidity_sensor:
            humidity_reading = humidity_sensor.get_reading()
            if humidity_reading and humidity_reading < HUMIDITY_THRESHOLD:
                if ac:
                    print(f"Humidity is {humidity_reading}%. Turning on AC for humidification.")
                    ac.turn_on()
            else:
                if ac:
                    ac.turn_off()

        if light_sensor:
            light_reading = light_sensor.get_reading()
            if light_reading and light_reading > LIGHT_THRESHOLD:
                if curtain:
                    print(f"Light intensity is {light_reading}. Closing curtains.")
                    curtain.turn_on()
            else:
                if curtain:
                    curtain.turn_off()

        time.sleep(5)  # Wait for a bit before checking again

if __name__ == "__main__":
    control_room("LivingRoom")
# ```
# 
# ### Running the Application:
# 
# To run your smart home application in a Linux terminal, execute the following command:
# 
# ```bash
# python3 main.py
# ```
# 
# This script will continuously monitor the sensors and adjust the actuators accordingly based on the given conditions. Ensure that all necessary files are in the correct directory and that the `home` folder is accessible.