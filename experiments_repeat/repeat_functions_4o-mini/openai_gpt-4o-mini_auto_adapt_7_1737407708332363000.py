# Based on your functional description and the provided source codes, I will create a `function.py` file that integrates the functionalities of the smart home system. This file will include a `main` function that checks the readings from the sensors and controls the actuators accordingly.
# 
# Here’s the `function.py` code:
# 
# ```python
# function.py
from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.config import TEMP_HIGH, TEMP_LOW, HUMIDITY_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_HIGH, LIGHT_INTENSITY_LOW
import time

def monitor_home():
    home = home_plan()

    for room in home:
        sensors = get_room_sensors(home, room.name)
        actuators = get_room_actuators(home, room.name)

        # Check sensor readings
        temperature_sensor = next((s for s in sensors if s.sensor_type == "IndoorTemperature"), None)
        humidity_sensor = next((s for s in sensors if s.sensor_type == "Humidity"), None)
        light_sensor = next((s for s in sensors if s.sensor_type == "LightIntensive"), None)

        # Read temperature
        if temperature_sensor:
            temperature_reading = temperature_sensor.get_reading()
            if temperature_reading is not None:
                print(f"Temperature in {room.name}: {temperature_reading}°C")
                if temperature_reading > TEMP_HIGH:
                    heater = next((a for a in actuators if a.actuator_type == "Heater"), None)
                    if heater:
                        heater.turn_on()
                        heater.set_target_temperature(TEMP_LOW)
                elif temperature_reading < TEMP_LOW:
                    ac = next((a for a in actuators if a.actuator_type == "AC"), None)
                    if ac:
                        ac.turn_on()
                        ac.set_target_temperature(TEMP_HIGH)

        # Read humidity
        if humidity_sensor:
            humidity_reading = humidity_sensor.get_reading()
            if humidity_reading is not None:
                print(f"Humidity in {room.name}: {humidity_reading}%")
                if humidity_reading < HUMIDITY_LOW:
                    humidifier = next((a for a in actuators if a.actuator_type == "Humidifier"), None)
                    if humidifier:
                        humidifier.turn_on()
                        humidifier.increase_humidity()
                elif humidity_reading > HUMIDITY_HIGH:
                    humidifier = next((a for a in actuators if a.actuator_type == "Humidifier"), None)
                    if humidifier:
                        humidifier.turn_on()
                        humidifier.decrease_humidity()

        # Read light intensity
        if light_sensor:
            light_reading = light_sensor.get_reading()
            if light_reading is not None:
                print(f"Light Intensity in {room.name}: {light_reading} lux")
                if light_reading < LIGHT_INTENSITY_LOW:
                    light = next((a for a in actuators if a.actuator_type == "Light"), None)
                    if light:
                        light.turn_on()
                        light.set_brightness_level("high")
                elif light_reading > LIGHT_INTENSITY_HIGH:
                    light = next((a for a in actuators if a.actuator_type == "Light"), None)
                    if light:
                        light.turn_on()
                        light.set_brightness_level("low")

        # Introduce a small delay to simulate time passing
        time.sleep(2)

def main():
    monitor_home()

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation:
# 
# 1. **Room Monitoring**: The `monitor_home()` function iterates through each room, retrieves the sensors and actuators, and checks the readings from the temperature, humidity, and light intensity sensors.
# 
# 2. **Actuator Control**:
#    - **Temperature**: If the temperature exceeds the defined high threshold, the heater is turned on and set to a target low temperature. Conversely, if the temperature falls below the low threshold, the AC is turned on and set to a target high temperature.
#    - **Humidity**: If the humidity is below the low threshold, the humidifier is activated to increase humidity. If it exceeds the high threshold, the humidifier is activated to decrease humidity.
#    - **Light Intensity**: If the light intensity is below the low threshold, the light is turned on and set to high brightness. If it is above the high threshold, the light is set to low brightness.
# 
# 3. **Main Function**: The `main()` function calls `monitor_home()` to start the monitoring process.
# 
# This implementation will help automate the management of temperature, humidity, and light in your smart home environment based on the provided readings.