# Based on your functional description and the provided source code files, I will create a `function.py` file that contains a main function to monitor the temperature, humidity, and light intensity in your smart home. The main function will interact with the sensors and actuators to control the environment based on the given conditions, such as turning on the heater or humidifier, and adjusting the lights.
# 
# Here's the `function.py` code:
# 
# ```python
# functions/function.py
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, Humidifier, Light
from home.home_plan import home_plan
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    # Initialize home environment
    home = home_plan()

    # Assuming we are monitoring the living room
    living_room = next(room for room in home if room.name == "LivingRoom")

    # Get sensors and actuators
    temperature_sensor = next(sensor for sensor in living_room.sensors if sensor.sensor_type == "IndoorTemperature")
    humidity_sensor = next(sensor for sensor in living_room.sensors if sensor.sensor_type == "Humidity")
    light_sensor = next(sensor for sensor in living_room.sensors if sensor.sensor_type == "LightIntensive")

    heater = next(actuator for actuator in living_room.actuators if actuator.actuator_type == "Heater")
    humidifier = next(actuator for actuator in living_room.actuators if actuator.actuator_type == "Humidifier")
    light = next(actuator for actuator in living_room.actuators if actuator.actuator_type == "Light")

    # Turn on sensors
    temperature_sensor.turn_on()
    humidity_sensor.turn_on()
    light_sensor.turn_on()

    # Get readings
    current_temperature = temperature_sensor.get_reading()
    current_humidity = humidity_sensor.get_reading()
    current_light_intensity = light_sensor.get_reading()

    # Control logic based on readings
    if current_temperature is not None:
        if current_temperature < TEMP_LOW:
            heater.turn_on()
            heater.set_target_temperature(TEMP_HIGH)
        elif current_temperature > TEMP_HIGH:
            heater.turn_off()

    if current_humidity is not None:
        if current_humidity < HUMIDITY_LOW:
            humidifier.turn_on()
        elif current_humidity > HUMIDITY_HIGH:
            humidifier.turn_off()

    if current_light_intensity is not None:
        if current_light_intensity < LIGHT_INTENSITY_LOW:
            light.turn_on()
            light.set_brightness_level("high")
        elif current_light_intensity > LIGHT_INTENSITY_HIGH:
            light.turn_off()

    # Print final statuses
    print(f"Temperature: {current_temperature}°C, Humidity: {current_humidity}%, Light Intensity: {current_light_intensity} lux")
    print(f"Heater Status: {heater.get_status()}")
    print(f"Humidifier Status: {humidifier.get_status()}")
    print(f"Light Status: {light.get_status()}")

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation:
# 1. **Imports**: The necessary classes from your project are imported.
# 2. **Main Function**: The main function initializes the home environment and retrieves the specific sensors and actuators for the living room.
# 3. **Control Logic**:
#    - The temperature is checked against thresholds to turn the heater on or off.
#    - The humidity is monitored to activate or deactivate the humidifier.
#    - The light intensity is adjusted based on ambient light readings.
# 4. **Final Statuses**: The current readings and statuses of the actuators are printed at the end.
# 
# ### Next Steps:
# - Place this `function.py` file in the `functions` folder.
# - Make sure to run the script to see how it interacts with the smart home system.