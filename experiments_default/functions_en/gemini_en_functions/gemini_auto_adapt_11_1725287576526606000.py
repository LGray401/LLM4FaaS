from home.home_plan import home_plan, get_room, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, TEMP_LOW, HUMIDITY_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_HIGH, LIGHT_INTENSITY_LOW
from home.logger_config import logger

def main():
    home = home_plan()

    # Temperature Control
    temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    acs = get_all_actuators(home, "AC")
    heaters = get_all_actuators(home, "Heater")

    for temperature_sensor in temperature_sensors:
        temperature = temperature_sensor.get_reading()
        if temperature is not None:
            if temperature > TEMP_HIGH:
                for ac in acs:
                    ac.turn_on()
                    logger.info(f"Turning on AC in {ac.room_name} due to high temperature.")
            elif temperature < TEMP_LOW:
                for heater in heaters:
                    heater.turn_on()
                    logger.info(f"Turning on heater in {heater.room_name} due to low temperature.")

    # Humidity Control
    humidity_sensors = get_all_sensors(home, "Humidity")
    humidifiers = get_all_actuators(home, "Humidifier")
    
    for humidity_sensor in humidity_sensors:
        humidity = humidity_sensor.get_reading()
        if humidity is not None:
            if humidity > HUMIDITY_HIGH:
                for humidifier in humidifiers:
                    humidifier.decrease_humidity()
                    logger.info(f"Decreasing humidity in {humidifier.room_name} due to high humidity.")
            elif humidity < HUMIDITY_LOW:
                for humidifier in humidifiers:
                    humidifier.increase_humidity()
                    logger.info(f"Increasing humidity in {humidifier.room_name} due to low humidity.")

    # Light Intensity Control
    light_intensity_sensors = get_all_sensors(home, "LightIntensive")
    lights = get_all_actuators(home, "Light")
    
    for light_intensity_sensor in light_intensity_sensors:
        light_intensity = light_intensity_sensor.get_reading()
        if light_intensity is not None:
            if light_intensity > LIGHT_INTENSITY_HIGH:
                for light in lights:
                    light.turn_on()
                    logger.info(f"Turning on light in {light.room_name} due to high light intensity.")
            elif light_intensity < LIGHT_INTENSITY_LOW:
                for light in lights:
                    light.turn_off()
                    logger.info(f"Turning off light in {light.room_name} due to low light intensity.")
    
if __name__ == '__main__':
    main()

# **Explanation:**

# 1. **Imports:** The code imports necessary modules:
#     - `home.home_plan`: For managing the home structure and retrieving rooms, sensors, and actuators.
#     - `home.config`: For accessing configuration values like temperature thresholds.
#     - `home.logger_config`: For logging events and messages.

# 2. **`main` Function:**
#     - **Home Setup:** It starts by creating the `home` object using `home_plan()`, which defines the rooms and their components.
#     - **Temperature Control:**
#         - Gets all `IndoorTemperature` sensors.
#         - Gets all `AC` and `Heater` actuators.
#         - Iterates through each temperature sensor:
#             - Reads the current temperature.
#             - If temperature is above the `TEMP_HIGH` threshold, turns on all AC units in the home.
#             - If temperature is below the `TEMP_LOW` threshold, turns on all heaters in the home.
#     - **Humidity Control:**
#         - Gets all `Humidity` sensors.
#         - Gets all `Humidifier` actuators.
#         - Iterates through each humidity sensor:
#             - Reads the current humidity.
#             - If humidity is above the `HUMIDITY_HIGH` threshold, decreases humidity in all humidifiers.
#             - If humidity is below the `HUMIDITY_LOW` threshold, increases humidity in all humidifiers.
#     - **Light Intensity Control:**
#         - Gets all `LightIntensive` sensors.
#         - Gets all `Light` actuators.
#         - Iterates through each light intensity sensor:
#             - Reads the current light intensity.
#             - If light intensity is above the `LIGHT_INTENSITY_HIGH` threshold, turns on all lights.
#             - If light intensity is below the `LIGHT_INTENSITY_LOW` threshold, turns off all lights.

# 3. **Logging:** The code uses the `logger` object to log actions and events, providing information about what's happening in the smart home system.

# **How to Use:**

# 1. Place the `function.py` file in your `functions` folder.
# 2. Run the `function.py` file. 
# 3. The code will automatically monitor temperature, humidity, and light intensity and control the respective actuators (AC, heaters, humidifiers, lights) based on the set thresholds.

# **Improvements:**

# - **Specific Room Control:** You could modify the code to control actuators based on the room they belong to. For instance, only turn on the AC in the LivingRoom if the LivingRoom temperature is high.
# - **Actuator States:**  Consider keeping track of the current state of actuators (on/off) to avoid unnecessary actions.
# - **User Preferences:** Allow users to customize thresholds and preferences for different rooms.
# - **Error Handling:** Implement error handling to gracefully manage unexpected scenarios or sensor failures.
# - **Timers and Scheduling:** Add timers or a scheduling system to automate actions at specific times, such as turning on lights at dusk or running the cleaning robot daily. 
