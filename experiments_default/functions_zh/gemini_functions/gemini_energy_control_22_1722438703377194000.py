from home.home_plan import home_plan, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger

def main():
    # Create the home plan
    home = home_plan()

    # Kitchen smoke sensor logic
    smoke_sensors = get_all_sensors(home, "Smoke")
    for smoke_sensor in smoke_sensors:
        smoke_reading = smoke_sensor.get_reading()
        if smoke_reading is not None and smoke_reading > 50:  # Assuming smoke reading above 50 indicates an issue
            notification_senders = get_all_actuators(home, "NotificationSender")
            for notification_sender in notification_senders:
                notification_sender.notification_sender("Smoke detected in the Kitchen! Please check.")

    # Living room temperature control logic
    living_room = get_room_sensors(home, "LivingRoom")
    for sensor in living_room:
        if sensor.sensor_type == "IndoorTemperature":
            temperature = sensor.get_reading()
            if temperature is not None:
                living_room_ac = get_room_actuators(home, "LivingRoom")[0]
                if temperature < TEMP_LOW:
                    living_room_ac.turn_off()
                    logger.info("Living room temperature is below 20 degrees, turning off the AC")
                elif temperature > TEMP_HIGH:
                    living_room_ac.turn_on()
                    logger.info("Living room temperature is above 25 degrees, turning on the AC")

    # Automatic light control logic
    for room in home:
        light_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "LightIntensive"]
        lights = [actuator for actuator in room.actuators if actuator.actuator_type == "Light"]
        for light_sensor in light_sensors:
            light_intensity = light_sensor.get_reading()
            if light_intensity is not None:
                for light in lights:
                    if light_intensity < LIGHT_INTENSITY_LOW:
                        light.turn_on()
                        logger.info(f"Light intensity in {room.name} is low, turning on the light")
                    elif light_intensity > LIGHT_INTENSITY_HIGH:
                        light.turn_off()
                        logger.info(f"Light intensity in {room.name} is high, turning off the light")

    # Cleaning robot daily routine
    cleaning_robots = get_all_actuators(home, "CleaningRobot")
    for cleaning_robot in cleaning_robots:
        cleaning_robot.daily_routine()

if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Import necessary modules:**
#    - `home.home_plan`: Provides functions for interacting with the home plan, such as retrieving sensors and actuators.
#    - `home.config`: Contains configuration values like temperature thresholds.
#    - `home.logger_config`:  Handles logging for debugging.

# 2. **`main` function:**
#    - **Smoke Detection:**
#      - Gets all "Smoke" sensors from the home.
#      - Reads smoke sensor values.
#      - If a smoke reading exceeds a threshold (50 in this example), it triggers a notification to all "NotificationSender" actuators.
#    - **Living Room Temperature Control:**
#      - Gets the sensors in the "LivingRoom".
#      - Checks for "IndoorTemperature" sensors.
#      - Reads temperature values.
#      - Turns the "AC" actuator in the "LivingRoom" on/off based on the temperature being above or below the thresholds (25 and 20 degrees).
#    - **Automatic Light Control:**
#      - Iterates through each room.
#      - Gets "LightIntensive" sensors and "Light" actuators in the room.
#      - Reads light intensity values.
#      - Turns the lights on/off based on the light intensity being below or above the thresholds (300 and 900 lux).
#    - **Cleaning Robot Routine:**
#      - Gets all "CleaningRobot" actuators.
#      - Initiates the daily routine for each cleaning robot.

# **Key Points:**

# - This code demonstrates a simple smart home automation logic using the provided sensor and actuator classes.
# - The thresholds for smoke, temperature, and light intensity are defined in `home.config`.
# - You can extend this code by adding more logic based on your specific requirements and the available sensors and actuators.

# **How to Use:**

# 1. Make sure you have the `home` folder with `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py` files in the same directory as this `function.py` file.
# 2. Run the `function.py` file. The code will simulate sensor readings and actuator actions based on the logic implemented.
