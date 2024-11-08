# To create a smart home application based on your functional description, we will need to implement a main Python script that utilizes the provided sensor and actuator classes. The goal is to maintain the indoor temperature not higher than 26°C, keep humidity below 30%, and manage light intensity appropriately.
# 
# Let's create a new Python script called `smart_home.py` that will use the components from the `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py` files. This script will monitor the sensors and control the actuators to achieve the desired conditions.
# 
# Here's what the `smart_home.py` script might look like:
# 
# ```python
import time
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC, Humidifier, Curtain, Light
from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.config import TEMP_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_HIGH

def monitor_and_control():
    home = home_plan()
    
    while True:
        for room in home:
            sensors = get_room_sensors(home, room.name)
            actuators = get_room_actuators(home, room.name)

            # Initialize actuator states
            ac = next((actuator for actuator in actuators if isinstance(actuator, AC)), None)
            humidifier = next((actuator for actuator in actuators if isinstance(actuator, Humidifier)), None)
            curtain = next((actuator for actuator in actuators if isinstance(actuator, Curtain)), None)
            light = next((actuator for actuator in actuators if isinstance(actuator, Light)), None)

            # Turn on sensors
            for sensor in sensors:
                sensor.turn_on()
                time.sleep(1)  # Wait for sensors to stabilize (if needed)
            
            # Control temperature
            temp_sensor = next((sensor for sensor in sensors if isinstance(sensor, IndoorTemperatureSensor)), None)
            if temp_sensor:
                current_temp = temp_sensor.get_reading()
                if current_temp > TEMP_HIGH and ac:
                    ac.set_target_temperature(26)
                    ac.adjust_temperature(current_temp)

            # Control humidity
            humidity_sensor = next((sensor for sensor in sensors if isinstance(sensor, HumiditySensor)), None)
            if humidity_sensor:
                current_humidity = humidity_sensor.get_reading()
                if current_humidity > HUMIDITY_LOW and humidifier:
                    humidifier.decrease_humidity()

            # Control light intensity
            light_sensor = next((sensor for sensor in sensors if isinstance(sensor, LightIntensiveSensor)), None)
            if light_sensor:
                current_light = light_sensor.get_reading()
                if current_light > LIGHT_INTENSITY_HIGH and curtain:
                    curtain.turn_on()
                elif current_light < LIGHT_INTENSITY_HIGH and light:
                    light.turn_on()
                    light.set_brightness_level("medium")

            # Wait before next loop iteration
            time.sleep(5)  # Adjust this sleep time as needed

if __name__ == "__main__":
    try:
        monitor_and_control()
    except KeyboardInterrupt:
        print("Smart home control stopped by user.")
# ```
# 
# ### Instructions to Run the Application
# 
# 1. Ensure you have all the necessary Python files (`sensor.py`, `actuator.py`, `home_plan.py`, `config.py`) in the `home` directory.
# 
# 2. Save the above code as `smart_home.py` in the same directory where the `home` folder is located.
# 
# 3. Open a terminal and navigate to the directory containing the `smart_home.py` script.
# 
# 4. Run the script using the following command:
#    ```bash
#    python3 smart_home.py
#    ```
# 
# This script will continuously monitor the environmental sensors and control the actuators to maintain the specified conditions. You can stop the script by pressing `Ctrl+C`.
# 
# Please note that this script assumes that actuators like `AC`, `Humidifier`, `Curtain`, and `Light` are available in each room and that they have been properly initialized in the home plan. Adjust the script as necessary to fit your specific home setup.