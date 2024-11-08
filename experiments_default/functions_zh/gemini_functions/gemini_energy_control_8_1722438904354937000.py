from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators
from home.sensor import IndoorTemperatureSensor
from home.actuator import AC, Window
from home.config import TEMP_CHANGE_DURATION_WINDOW
from home.logger_config import logger


def main():
    home = home_plan()

    # Get the living room
    living_room = get_room(home, "LivingRoom")

    # Get the AC in the living room
    ac = get_room_actuators(home, "LivingRoom")[0]

    # Get the windows in the living room
    windows = get_room_actuators(home, "LivingRoom")[1:3]  # Assuming the first two actuators are windows

    # Set the AC target temperature
    ac.set_target_temperature(17)

    # Turn off the windows
    for window in windows:
        window.turn_off()

    # Adjust the AC temperature based on current temperature
    while True:
        # Get the current temperature
        temperature_sensors = get_room_sensors(home, "LivingRoom")
        temperature_sensor = temperature_sensors[0]  # Assuming the first sensor is the temperature sensor

        # Get the temperature reading
        current_temperature = temperature_sensor.get_reading()

        # Adjust the AC temperature
        ac.adjust_temperature(current_temperature)

        # Sleep for a duration
        time.sleep(TEMP_CHANGE_DURATION_WINDOW)

if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Import necessary modules:**
#    - `home.home_plan`: For home plan functions, room access, and actuator/sensor retrieval.
#    - `home.sensor`: To access `IndoorTemperatureSensor`.
#    - `home.actuator`: To access `AC` and `Window`.
#    - `home.config`: For configuration values like `TEMP_CHANGE_DURATION_WINDOW`.
#    - `home.logger_config`: To use the logger.

# 2. **`main` function:**
#    - **Get the home plan:** `home = home_plan()`
#    - **Find the living room:** `living_room = get_room(home, "LivingRoom")`
#    - **Get the AC and windows:**
#      - `ac = get_room_actuators(home, "LivingRoom")[0]` (assuming the first actuator is the AC)
#      - `windows = get_room_actuators(home, "LivingRoom")[1:3]` (assuming the first two actuators are windows)
#    - **Set the AC target temperature:** `ac.set_target_temperature(17)`
#    - **Turn off the windows:** `window.turn_off()` for each window in `windows`
#    - **Continuously adjust AC temperature:**
#      - **Get the current temperature:**
#        - `temperature_sensors = get_room_sensors(home, "LivingRoom")`
#        - `temperature_sensor = temperature_sensors[0]`
#        - `current_temperature = temperature_sensor.get_reading()`
#      - **Adjust the AC based on current temperature:** `ac.adjust_temperature(current_temperature)`
#      - **Wait:** `time.sleep(TEMP_CHANGE_DURATION_WINDOW)`

# 3. **Running the code:**
#    - The `if __name__ == "__main__":` block ensures the `main` function is executed only when the file is run directly.

# **Key points:**

# - The code assumes specific orders for actuators and sensors in the `home_plan.py` file. Make sure your `home_plan.py` aligns with these assumptions.
# - The code uses `while True` to keep adjusting the AC temperature indefinitely. You might want to add logic to stop this loop under certain conditions.
# - The code uses `logger.info` and `logger.warning` for logging information. Ensure you have configured the logger as described in `logger_config.py`.
