from home.home_plan import get_room, get_room_actuators, get_room_sensors
from home.actuator import AC
from home.config import TEMP_HIGH
from home.logger_config import logger

def open_window_to_cool_down(home, room_name):
    """Opens a window in the specified room to cool it down.

    Args:
        home: The home plan object.
        room_name: The name of the room to cool down.
    """
    room = get_room(home, room_name)
    if room is None:
        return

    # Find the AC in the room
    actuators = get_room_actuators(home, room_name)
    ac = next((a for a in actuators if isinstance(a, AC)), None)
    if ac is None:
        logger.warning(f"No AC found in {room_name}. Cannot cool down the room.")
        return

    # Get the current temperature sensor in the room
    sensors = get_room_sensors(home, room_name)
    temperature_sensor = next((s for s in sensors if s.sensor_type == "IndoorTemperature"), None)
    if temperature_sensor is None:
        logger.warning(f"No temperature sensor found in {room_name}. Cannot cool down the room.")
        return

    # Check if the temperature is high
    temperature = temperature_sensor.get_reading()
    if temperature is None:
        return

    if temperature > TEMP_HIGH:
        logger.info(f"Temperature in {room_name} is high. Opening a window to cool down.")
        for actuator in actuators:
            if actuator.actuator_type == "Window":
                actuator.turn_on()
                return

    else:
        logger.info(f"Temperature in {room_name} is not high enough to open the window.")


if __name__ == "__main__":
    # Example usage - Replace with your actual home plan
    home = get_room(None, "LivingRoom")
    open_window_to_cool_down(home, "LivingRoom")

# **Explanation:**

# 1. **Import necessary modules:**
#    - `get_room`, `get_room_actuators`, `get_room_sensors` from `home.home_plan`: Functions to access rooms, actuators, and sensors from your `home_plan.py` file.
#    - `AC` from `home.actuator`: Class representing an air conditioner.
#    - `TEMP_HIGH` from `home.config`: The temperature threshold for cooling.
#    - `logger` from `home.logger_config`: Your logging system.

# 2. **Define `open_window_to_cool_down` function:**
#    - **Arguments:**
#      - `home`: The home plan object.
#      - `room_name`: The name of the room to cool down.
#    - **Logic:**
#      1. **Get the room:** Use `get_room` to find the specified room in the home plan.
#      2. **Find the AC:** Use `get_room_actuators` to get the actuators in the room and iterate through them to find the `AC` instance.
#      3. **Get the temperature sensor:** Use `get_room_sensors` to find the `IndoorTemperature` sensor in the room.
#      4. **Check the temperature:** Get the current temperature using the sensor and compare it to `TEMP_HIGH`.
#      5. **Open the window:** If the temperature is higher than `TEMP_HIGH`, iterate through the room's actuators and find a `Window`. If found, turn it on.

# 3. **Example usage:**
#    - This section is just a placeholder for demonstrating how you would use the `open_window_to_cool_down` function with your existing `home_plan` object. Replace the comment with the actual instantiation and usage of your `home_plan` object.

# **Integration with your Project:**

# 1. **Place `function.py`:** Create a `functions` folder in your project directory and place this `function.py` file inside it.
# 2. **Import `function.py`:** In your main script or wherever you need to use this functionality, import the function:
#    ```python
#    from functions.function import open_window_to_cool_down
#    ```
# 3. **Call the function:** When you need to cool down a room, call `open_window_to_cool_down` with your home plan object and the desired room name:
#    ```python
#    open_window_to_cool_down(my_home_plan, "LivingRoom")
#    ```

# Remember to replace the placeholder code in the example usage section with your actual home plan initialization and how you'd use the `open_window_to_cool_down` function in your project.
