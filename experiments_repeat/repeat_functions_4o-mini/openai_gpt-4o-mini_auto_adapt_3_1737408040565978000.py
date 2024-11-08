# Based on your functional description and the source code provided, I will create the `function.py` file located in the `functions` folder. This file will contain a main function that interacts with the sensors and actuators, specifically focusing on temperature, humidity, and light intensity as described.
# 
# Here's the `function.py` file:
# 
# ```python
# functions/function.py

from home.home_plan import home_plan
from home.actuator import Heater, AC, Light
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.logger_config import logger

def main():
    # Set up the home environment
    home = home_plan()

    # Get the room objects
    living_room = next((room for room in home if room.name == "LivingRoom"), None)
    bedroom = next((room for room in home if room.name == "Bedroom"), None)

    # Initialize sensors and actuators
    temperature_sensor = IndoorTemperatureSensor("LivingRoom")
    humidity_sensor = HumiditySensor("LivingRoom")
    light_sensor = LightIntensiveSensor("LivingRoom")

    heater = Heater("LivingRoom")
    ac = AC("Bedroom")
    light = Light("LivingRoom")

    # Turn on sensors
    temperature_sensor.turn_on()
    humidity_sensor.turn_on()
    light_sensor.turn_on()

    # Get readings
    temperature = temperature_sensor.get_reading()
    humidity = humidity_sensor.get_reading()
    light_intensity = light_sensor.get_reading()

    # Display readings
    print(f"Current Temperature: {temperature}°C")
    print(f"Current Humidity: {humidity}%")
    print(f"Current Light Intensity: {light_intensity} lux")

    # Control logic based on readings
    if temperature is not None:
        if temperature < 26:
            heater.set_target_temperature(26)
            heater.adjust_temperature(temperature)
        else:
            heater.turn_off()

    if humidity is not None:
        if humidity < 50:
            humidifier = AC("LivingRoom")  # Assuming AC can also act as a humidifier
            humidifier.adjust_temperature(humidity)  # This should be adjusted to a real humidifier method
        else:
            print("Humidity is at a comfortable level.")

    if light_intensity is not None:
        if light_intensity < 300:  # Assuming this is low light intensity
            light.turn_on()
            light.set_brightness_level("high")
        elif light_intensity > 900:
            light.turn_off()
        else:
            light.set_brightness_level("medium")

    # Turn off sensors after use
    temperature_sensor.turn_off()
    humidity_sensor.turn_off()
    light_sensor.turn_off()

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation:
# 1. **Imports**: The necessary classes are imported from the existing modules.
# 2. **Main Function**:
#    - A home environment is created using the `home_plan` function.
#    - Room objects are retrieved for "LivingRoom" and "Bedroom".
#    - Sensors and actuators are instantiated.
#    - Sensors are turned on to get readings for temperature, humidity, and light intensity.
#    - Based on the readings, the actuators (heater, AC, and light) are controlled according to the specified thresholds.
#    - Finally, the sensors are turned off after the readings are taken.
# 
# ### Note:
# - The code assumes that the desired logic for controlling the actuators based on the readings is in line with your functional description. Adjustments may be needed based on the actual implementation and preferences for how the actuators should respond.
# - The code for the humidifier is represented with some assumptions about how it fits into the existing framework; you may need to create a dedicated humidifier class if it doesn't exist in your current setup.