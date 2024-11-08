# To create a smart home application based on your functional description and the provided code files, we'll organize the system into branches for sensors and actuators in each room, and use the existing classes to simulate the behavior of those branches.
# 
# Here is the main application code that orchestrates the smart home functionality:
# 
# ## `smart_home.py`
# 
# ```python
import time
from home.home_plan import home_plan, print_home_plan, get_room_sensors, get_room_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def control_temperature(sensors, actuators):
    indoor_temp_sensors = [sensor for sensor in sensors if sensor.sensor_type == "IndoorTemperature"]
    heaters = [actuator for actuator in actuators if actuator.actuator_type == "Heater"]
    acs = [actuator for actuator in actuators if actuator.actuator_type == "AC"]

    for sensor in indoor_temp_sensors:
        sensor.turn_on()
        current_temp = sensor.get_reading()
        for heater in heaters:
            heater.set_target_temperature(TEMP_LOW)
            heater.adjust_temperature(current_temp)
        for ac in acs:
            ac.set_target_temperature(TEMP_HIGH)
            ac.adjust_temperature(current_temp)

def control_humidity(sensors, actuators):
    humidity_sensors = [sensor for sensor in sensors if sensor.sensor_type == "Humidity"]
    humidifiers = [actuator for actuator in actuators if actuator.actuator_type == "Humidifier"]

    for sensor in humidity_sensors:
        sensor.turn_on()
        current_humidity = sensor.get_reading()
        for humidifier in humidifiers:
            if current_humidity < HUMIDITY_LOW:
                humidifier.increase_humidity()
            elif current_humidity > HUMIDITY_HIGH:
                humidifier.decrease_humidity()

def control_light(sensors, actuators):
    light_sensors = [sensor for sensor in sensors if sensor.sensor_type == "LightIntensive"]
    lights = [actuator for actuator in actuators if actuator.actuator_type == "Light"]

    for sensor in light_sensors:
        sensor.turn_on()
        current_light_intensity = sensor.get_reading()
        for light in lights:
            if current_light_intensity < LIGHT_INTENSITY_LOW:
                light.set_brightness_level("high")
            elif current_light_intensity > LIGHT_INTENSITY_HIGH:
                light.set_brightness_level("low")
            else:
                light.set_brightness_level("medium")

def main():
    home = home_plan()
    print_home_plan(home)

    for room in home:
        sensors = get_room_sensors(home, room.name)
        actuators = get_room_actuators(home, room.name)
        control_temperature(sensors, actuators)
        control_humidity(sensors, actuators)
        control_light(sensors, actuators)
        time.sleep(1)

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation
# 
# 1. **Main Functionality**: The script starts by printing the home plan, which includes all rooms, sensors, and actuators. Then, it iterates over each room to control temperature, humidity, and lighting based on sensor readings.
# 
# 2. **Temperature Control**: It reads from the temperature sensors and adjusts the AC or Heater actuators accordingly.
# 
# 3. **Humidity Control**: It reads from the humidity sensors and adjusts the humidifiers to increase or decrease humidity.
# 
# 4. **Light Control**: It reads from the light intensity sensors and adjusts the brightness of the lights.
# 
# ### Running the Application
# 
# To run this application in a Linux terminal, you should navigate to the directory containing the `smart_home.py` file and run:
# 
# ```bash
# python3 smart_home.py
# ```
# 
# Ensure that your Python environment is set up correctly and that the `home` directory containing the referenced Python files (`sensor.py`, `actuator.py`, `home_plan.py`, `config.py`) is in the same directory or accessible in your Python path.