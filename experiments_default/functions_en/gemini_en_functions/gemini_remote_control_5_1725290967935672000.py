from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators, print_home_plan
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, \
    SmokeSensor
from home.actuator import Heater, AC, Light, CoffeeMachine, Door, Window, Curtain, MusicPlayer, CleaningRobot, \
    NotificationSender, SmartTV, SmartSocket, Humidifier
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, \
    LIGHT_INTENSITY_HIGH, TEMP_CHANGE_DURATION_WINDOW

from home.logger_config import logger


def main():
    # Create the home plan
    home = home_plan()

    # Print the home plan for debugging purposes
    print_home_plan(home)

    # Get the living room
    living_room = get_room(home, "LivingRoom")

    # Get the living room's sensors
    living_room_sensors = get_room_sensors(home, "LivingRoom")

    # Get the living room's actuators
    living_room_actuators = get_room_actuators(home, "LivingRoom")

    # Get all the indoor temperature sensors in the house
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")

    # Get all the lights in the house
    lights = get_all_actuators(home, "Light")

    # Example usage of sensors and actuators
    # ...

    # Adjust the temperature in the living room
    # for indoor_temp_sensor in indoor_temp_sensors:
    #     if indoor_temp_sensor.room_name == "LivingRoom":
    #         current_temperature = indoor_temp_sensor.get_reading()
    #         for actuator in living_room_actuators:
    #             if isinstance(actuator, Heater):
    #                 actuator.adjust_temperature(current_temperature)
    #             elif isinstance(actuator, AC):
    #                 actuator.adjust_temperature(current_temperature)
    #         break

    # Turn on the lights in the living room
    for light in lights:
        if light.room_name == "LivingRoom":
            light.turn_on()
            break

    # Make coffee in the kitchen
    kitchen = get_room(home, "Kitchen")
    kitchen_actuators = get_room_actuators(home, "Kitchen")
    for actuator in kitchen_actuators:
        if isinstance(actuator, CoffeeMachine):
            actuator.make_coffee("Espresso")
            break

    # Automate based on sensor readings
    while True:
        # Monitor indoor temperature
        for indoor_temp_sensor in indoor_temp_sensors:
            current_temp = indoor_temp_sensor.get_reading()
            room_name = indoor_temp_sensor.room_name
            room = get_room(home, room_name)
            room_actuators = get_room_actuators(home, room_name)
            if current_temp < TEMP_LOW:
                logger.info(f"Temperature in {room_name} is below threshold, turning on heater.")
                for actuator in room_actuators:
                    if isinstance(actuator, Heater):
                        actuator.turn_on()
                        break
            elif current_temp > TEMP_HIGH:
                logger.info(f"Temperature in {room_name} is above threshold, turning on AC.")
                for actuator in room_actuators:
                    if isinstance(actuator, AC):
                        actuator.turn_on()
                        break

        # Monitor humidity
        for humidity_sensor in get_all_sensors(home, "Humidity"):
            current_humidity = humidity_sensor.get_reading()
            room_name = humidity_sensor.room_name
            room = get_room(home, room_name)
            room_actuators = get_room_actuators(home, room_name)
            if current_humidity < HUMIDITY_LOW:
                logger.info(f"Humidity in {room_name} is below threshold, turning on humidifier.")
                for actuator in room_actuators:
                    if isinstance(actuator, Humidifier):
                        actuator.increase_humidity()
                        break
            elif current_humidity > HUMIDITY_HIGH:
                logger.info(f"Humidity in {room_name} is above threshold, decreasing humidity.")
                for actuator in room_actuators:
                    if isinstance(actuator, Humidifier):
                        actuator.decrease_humidity()
                        break

        # Monitor light intensity
        for light_intensive_sensor in get_all_sensors(home, "LightIntensive"):
            current_light_intensity = light_intensive_sensor.get_reading()
            room_name = light_intensive_sensor.room_name
            room = get_room(home, room_name)
            room_actuators = get_room_actuators(home, room_name)
            if current_light_intensity < LIGHT_INTENSITY_LOW:
                logger.info(f"Light intensity in {room_name} is below threshold, turning on lights.")
                for actuator in room_actuators:
                    if isinstance(actuator, Light):
                        actuator.turn_on()
                        break
            elif current_light_intensity > LIGHT_INTENSITY_HIGH:
                logger.info(f"Light intensity in {room_name} is above threshold, turning off lights.")
                for actuator in room_actuators:
                    if isinstance(actuator, Light):
                        actuator.turn_off()
                        break

        # Simulate sensor readings and actuator actions
        # ...

        # Wait for a short period of time
        time.sleep(TEMP_CHANGE_DURATION_WINDOW)  # Simulate waiting for temperature change


if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Import Necessary Modules:**
#    - Import relevant classes from `home.home_plan`, `home.sensor`, `home.actuator`, and `home.config`.
#    - Import `logger` for logging purposes.

# 2. **`main` Function:**
#    - **Create the Home Plan:**
#      - `home = home_plan()` creates a list of rooms with their sensors and actuators.
#      - `print_home_plan(home)` prints the home plan for debugging.
#    - **Get Specific Rooms and Components:**
#      - `living_room = get_room(home, "LivingRoom")` gets the living room object.
#      - Similar methods get sensors and actuators for the living room.
#    - **Get All Sensors and Actuators:**
#      - `indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")` finds all indoor temperature sensors.
#      - `lights = get_all_actuators(home, "Light")` finds all lights.
#    - **Example Usage:**
#      - Demonstrates basic sensor readings and actuator actions.
#    - **Automation Loop:**
#      - `while True:` creates a continuous loop for automation.
#      - **Temperature Monitoring:**
#        - Iterates through indoor temperature sensors.
#        - Checks if temperature is below or above thresholds.
#        - If necessary, turns on heaters or ACs in the respective rooms.
#      - **Humidity Monitoring:**
#        - Iterates through humidity sensors.
#        - Checks if humidity is below or above thresholds.
#        - If necessary, adjusts humidity using humidifiers.
#      - **Light Intensity Monitoring:**
#        - Iterates through light intensity sensors.
#        - Checks if light intensity is below or above thresholds.
#        - If necessary, turns lights on or off.
#      - **Sleep for a While:**
#        - `time.sleep(TEMP_CHANGE_DURATION_WINDOW)` pauses the loop to simulate changes in sensor readings.

# **Key Points:**

# - The code defines a simple automation framework using sensor readings and actuator actions.
# - It demonstrates monitoring of temperature, humidity, and light intensity.
# - It includes basic logic for adjusting temperature and humidity based on thresholds.
# - The `logger` is used for logging events and debugging.

# **To Run the Code:**

# 1. Make sure you have all the required Python modules installed (e.g., `time`, `random`, etc.).
# 2. Save the code as `function.py` in the `functions` folder.
# 3. Run the script from your terminal: `python functions/function.py`

# **Next Steps:**

# - **Add More Sensors and Actuators:** Expand the home plan with additional sensors and actuators based on your smart home project requirements.
# - **Implement More Automation Logic:** Implement more complex logic for controlling actuators based on sensor readings and user preferences.
# - **Connect to Real Sensors and Actuators:** Integrate the code with real-world sensors and actuators using communication protocols like MQTT, REST APIs, or other interfaces.
# - **User Interface:** Create a user interface (UI) to interact with the smart home system.
# - **AI Integration:** Explore the use of artificial intelligence (AI) to enhance automation and personalize the smart home experience.
