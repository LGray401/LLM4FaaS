from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger

def main():
    home = home_plan()
    # Example interaction:
    # Turn on the living room light and set it to medium brightness
    living_room = get_room(home, "LivingRoom")
    if living_room:
        living_room_lights = get_room_actuators(home, "LivingRoom")
        if living_room_lights:
            for light in living_room_lights:
                if light.actuator_type == "Light":
                    light.turn_on()
                    light.set_brightness_level("medium")

    # Get all the lights in the house and turn them off
    all_lights = get_all_actuators(home, "Light")
    if all_lights:
        for light in all_lights:
            light.turn_off()

    # Adjust the AC in the living room based on temperature
    living_room_ac = get_room_actuators(home, "LivingRoom")
    if living_room_ac:
        for ac in living_room_ac:
            if ac.actuator_type == "AC":
                living_room_temp_sensor = get_room_sensors(home, "LivingRoom")
                if living_room_temp_sensor:
                    for temp_sensor in living_room_temp_sensor:
                        if temp_sensor.sensor_type == "IndoorTemperature":
                            current_temp = temp_sensor.get_reading()
                            if current_temp is not None:
                                ac.adjust_temperature(current_temp)

    # Get all the temperature sensors and print their readings
    all_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    if all_temp_sensors:
        for temp_sensor in all_temp_sensors:
            temp_sensor.get_reading()

    # Check if any smoke sensors are triggered
    all_smoke_sensors = get_all_sensors(home, "Smoke")
    if all_smoke_sensors:
        for smoke_sensor in all_smoke_sensors:
            smoke_reading = smoke_sensor.get_reading()
            if smoke_reading is not None and smoke_reading > 50:
                logger.warning(f"Smoke detected in {smoke_sensor.room_name}!")
                notification_sender = get_room_actuators(home, smoke_sensor.room_name)
                if notification_sender:
                    for sender in notification_sender:
                        if sender.actuator_type == "NotificationSender":
                            sender.notification_sender("Smoke detected! Please check!")

if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Imports:**
#    - `home.home_plan`: Imports functions for managing the home plan, including getting rooms, sensors, and actuators.
#    - `home.config`: Imports configuration values for temperature, humidity, light intensity thresholds.
#    - `home.logger_config`: Imports the logger for logging events.

# 2. **`main()` function:**
#    - **Home Plan:** Creates the `home` object using `home_plan()` to represent the smart home's structure.
#    - **Living Room Light:**
#      - Gets the "LivingRoom" using `get_room()`.
#      - Retrieves lights in the "LivingRoom" using `get_room_actuators()`.
#      - Turns on each light and sets its brightness to "medium".
#    - **Turn Off All Lights:**
#      - Gets all lights in the house using `get_all_actuators()`.
#      - Turns off each light.
#    - **Living Room AC:**
#      - Gets the "LivingRoom" AC using `get_room_actuators()`.
#      - Gets the temperature sensor in the "LivingRoom" using `get_room_sensors()`.
#      - Reads the current temperature using `get_reading()`.
#      - Adjusts the AC based on the temperature and target temperature.
#    - **Temperature Sensor Readings:**
#      - Gets all temperature sensors using `get_all_sensors()`.
#      - Prints the readings of each temperature sensor.
#    - **Smoke Sensor Check:**
#      - Gets all smoke sensors using `get_all_sensors()`.
#      - Reads the smoke levels for each sensor.
#      - If smoke level is above 50, logs a warning, retrieves the notification sender in the room, and sends a smoke detection notification.

# 3. **Example Interactions:**
#    - The code provides examples of how to interact with the smart home: controlling lights, AC, and handling smoke detection.

# **To run this code:**

# 1. Make sure you have the other files (`sensor.py`, `actuator.py`, `home_plan.py`, `config.py`, `logger_config.py`) in the appropriate folders.
# 2. Run the `function.py` file.

# This code demonstrates how to create interactions with a smart home based on your provided descriptions. You can expand this code to include more functionality and add custom logic to your smart home system. 
