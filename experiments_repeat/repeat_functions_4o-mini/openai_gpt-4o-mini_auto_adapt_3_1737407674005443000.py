# Based on your functional description and the source code provided, I will create a `function.py` file for your smart home project. This file will contain a `main` function that simulates the operation of the smart home system, including reading sensor values and adjusting actuators accordingly.
# 
# Here is the content for the `function.py` file:
# 
# ```python
# function.py

from home.home_plan import home_plan
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, AC, Light, NotificationSender
from home.logger_config import logger

def main():
    # Initialize the home plan
    home = home_plan()

    # Get the living room for demonstration
    living_room = next((room for room in home if room.name == "LivingRoom"), None)

    if living_room:
        # Get sensors from the living room
        temp_sensor = next((sensor for sensor in living_room.sensors if isinstance(sensor, IndoorTemperatureSensor)), None)
        humidity_sensor = next((sensor for sensor in living_room.sensors if isinstance(sensor, HumiditySensor)), None)
        light_sensor = next((sensor for sensor in living_room.sensors if isinstance(sensor, LightIntensiveSensor)), None)

        # Get actuators from the living room
        heater = next((actuator for actuator in living_room.actuators if isinstance(actuator, Heater)), None)
        ac = next((actuator for actuator in living_room.actuators if isinstance(actuator, AC)), None)
        light = next((actuator for actuator in living_room.actuators if isinstance(actuator, Light)), None)
        notification_sender = next((actuator for actuator in living_room.actuators if isinstance(actuator, NotificationSender)), None)

        # Turn on sensors
        if temp_sensor:
            temp_sensor.turn_on()
            current_temp = temp_sensor.get_reading()
        
        if humidity_sensor:
            humidity_sensor.turn_on()
            current_humidity = humidity_sensor.get_reading()

        if light_sensor:
            light_sensor.turn_on()
            current_light = light_sensor.get_reading()

        # Set target temperatures for heater and AC
        if heater:
            heater.set_target_temperature(26)  # Target temperature for heater
            heater.adjust_temperature(current_temp)  # Adjust heater based on current temperature

        if ac:
            ac.set_target_temperature(26)  # Target temperature for AC
            ac.adjust_temperature(current_temp)  # Adjust AC based on current temperature

        # Control light based on light intensity
        if light and current_light:
            if current_light < 300:  # Example threshold for low light
                light.turn_on()
                light.set_brightness_level("high")
            elif current_light > 900:  # Example threshold for high light
                light.turn_off()
            else:
                light.set_brightness_level("medium")

        # Send notification about current status
        if notification_sender:
            notification_sender.turn_on()
            message = f"Current Temperature: {current_temp}°C, Humidity: {current_humidity}%, Light Intensity: {current_light} lux"
            notification_sender.notification_sender(message)

    else:
        logger.warning("Living room not found in home plan.")

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation:
# 1. **Home Initialization**: The `main` function initializes the home plan and retrieves the living room.
# 2. **Sensor and Actuator Management**: It fetches the relevant sensors and actuators from the living room and turns on the sensors to get readings.
# 3. **Temperature Control**: It sets target temperatures for the heater and air conditioner based on the readings from the temperature sensor.
# 4. **Light Control**: It adjusts the light based on the light intensity reading.
# 5. **Notifications**: It sends a notification with the current temperature, humidity, and light intensity.
# 
# ### Note:
# Make sure you have the appropriate imports for your logger and any other dependencies as needed in your project. Adjust the thresholds for light intensity and temperature as per your requirements.