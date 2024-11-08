from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, TEMP_LOW, HUMIDITY_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_HIGH, LIGHT_INTENSITY_LOW, TEMP_CHANGE_DURATION_WINDOW
from home.logger_config import logger


def main():
    home = home_plan()

    # Kitchen smoke detection
    kitchen = get_room(home, "Kitchen")
    smoke_sensors = get_room_sensors(kitchen, "Kitchen")
    smoke_alarm = get_room_actuators(kitchen, "Kitchen")[0]  # Assuming only one smoke alarm in the kitchen
    for smoke_sensor in smoke_sensors:
        smoke_sensor.turn_on()
        if smoke_sensor.get_reading() > 50:  # Assuming a threshold of 50 for smoke detection
            smoke_alarm.turn_on()
            print(f"Smoke detected in the Kitchen! Smoke alarm turned on.")
            logger.warning(f"Smoke detected in the Kitchen! Smoke alarm turned on.")

    # Summer AC control
    living_room = get_room(home, "LivingRoom")
    indoor_temp_sensor = get_room_sensors(living_room, "LivingRoom")[0]  # Assuming only one indoor temp sensor
    ac = get_room_actuators(living_room, "LivingRoom")[0]  # Assuming only one AC in the living room
    indoor_temp_sensor.turn_on()
    current_temp = indoor_temp_sensor.get_reading()
    if current_temp < TEMP_LOW:
        ac.turn_off()
        print(f"Indoor temperature is below {TEMP_LOW} degrees. AC turned off.")
        logger.info(f"Indoor temperature is below {TEMP_LOW} degrees. AC turned off.")
    elif current_temp > TEMP_HIGH:
        ac.turn_on()
        print(f"Indoor temperature is above {TEMP_HIGH} degrees. AC turned on.")
        logger.info(f"Indoor temperature is above {TEMP_HIGH} degrees. AC turned on.")

    # Sensor light control
    living_room = get_room(home, "LivingRoom")
    light_intensity_sensor = get_room_sensors(living_room, "LivingRoom")[0]
    light = get_room_actuators(living_room, "LivingRoom")[1]
    light_intensity_sensor.turn_on()
    current_light_intensity = light_intensity_sensor.get_reading()
    if current_light_intensity < LIGHT_INTENSITY_LOW:
        light.turn_off()
        print(f"Light intensity is below {LIGHT_INTENSITY_LOW} lux. Light turned off.")
        logger.info(f"Light intensity is below {LIGHT_INTENSITY_LOW} lux. Light turned off.")
    elif current_light_intensity > LIGHT_INTENSITY_HIGH:
        light.turn_on()
        print(f"Light intensity is above {LIGHT_INTENSITY_HIGH} lux. Light turned on.")
        logger.info(f"Light intensity is above {LIGHT_INTENSITY_HIGH} lux. Light turned on.")


if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Imports:**
#    - Import necessary functions and classes from `home_plan.py` and `config.py`.
#    - Import `logger` from `logger_config.py` for logging.

# 2. **`main()` function:**
#    - Creates a home plan using `home_plan()`.
#    - **Kitchen Smoke Detection:**
#      - Gets the "Kitchen" room using `get_room()`.
#      - Retrieves all smoke sensors in the kitchen using `get_room_sensors()`.
#      - Gets the first smoke alarm in the kitchen (assuming only one) using `get_room_actuators()`.
#      - Iterates through smoke sensors, turns them on, and checks if the reading exceeds the threshold (50 in this case).
#      - If smoke is detected, turns on the smoke alarm and logs the event.
#    - **Summer AC Control:**
#      - Gets the "LivingRoom" room.
#      - Retrieves the indoor temperature sensor and AC.
#      - Turns on the indoor temperature sensor.
#      - Gets the current temperature.
#      - If temperature is below `TEMP_LOW`, turns off the AC and logs the event.
#      - If temperature is above `TEMP_HIGH`, turns on the AC and logs the event.
#    - **Sensor Light Control:**
#      - Gets the "LivingRoom" room.
#      - Retrieves the light intensity sensor and the light.
#      - Turns on the light intensity sensor.
#      - Gets the current light intensity.
#      - If light intensity is below `LIGHT_INTENSITY_LOW`, turns off the light and logs the event.
#      - If light intensity is above `LIGHT_INTENSITY_HIGH`, turns on the light and logs the event.

# 3. **`if __name__ == "__main__":` block:**
#    - Calls the `main()` function when the script is run directly.

# **Key points:**

# - This script demonstrates how to interact with sensors and actuators in a smart home system based on your provided code.
# - It sets thresholds and triggers actions based on sensor readings, providing basic automation for the scenarios you described.
# - The `logger` is used to record events and warnings, which is helpful for debugging and monitoring.
# - You can further customize this script to incorporate more complex logic, additional features, and interactions with other components of your smart home system.
