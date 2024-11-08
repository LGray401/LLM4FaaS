# Based on your functional description and the provided source code, I will create a `function.py` file that contains a main function to open windows in a specific room to cool down the temperature. This function will first check the current indoor temperature of the specified room, then open the windows if the temperature is above a certain threshold (e.g., `TEMP_HIGH` from `config.py`).
# 
# Here's the `function.py` file:

# functions/function.py

from home.sensor import IndoorTemperatureSensor
from home.actuator import Window
from home.home_plan import get_room_sensors, get_room_actuators, get_room
from home.config import TEMP_HIGH, TEMP_CHANGE_DURATION_WINDOW
import time

def open_windows_to_cool_down(room_name):
    """
    Open windows in the specified room to cool down the temperature.
    
    :param room_name: The name of the room where the windows should be opened.
    """
    # Get the room
    room = get_room(home_plan(), room_name)
    if not room:
        print(f"Room '{room_name}' not found.")
        return

    # Get all indoor temperature sensors in the room
    sensors = get_room_sensors(home_plan(), room_name)
    temp_sensors = [sensor for sensor in sensors if isinstance(sensor, IndoorTemperatureSensor)]

    if not temp_sensors:
        print(f"No indoor temperature sensor found in room '{room_name}'.")
        return

    # Get the current temperature reading from the first temperature sensor
    temp_sensor = temp_sensors[0]
    temp_sensor.turn_on()
    current_temp = temp_sensor.get_reading()
    temp_sensor.turn_off()

    if current_temp is None:
        print(f"Failed to get temperature reading from {temp_sensor.id}.")
        return

    # Check if the current temperature is above the high threshold
    if current_temp > TEMP_HIGH:
        print(f"Current temperature in {room_name} is {current_temp:.2f}°C, which is above the threshold of {TEMP_HIGH}°C. Opening windows to cool down...")

        # Get all windows in the room
        actuators = get_room_actuators(home_plan(), room_name)
        windows = [actuator for actuator in actuators if isinstance(actuator, Window)]

        if not windows:
            print(f"No windows found in room '{room_name}'.")
            return

        # Open all windows
        for window in windows:
            window.turn_on()
            print(f"Window {window.id} in {room_name} is now open.")

        # Wait for the temperature to change
        time.sleep(TEMP_CHANGE_DURATION_WINDOW)

        # Turn off all windows
        for window in windows:
            window.turn_off()
            print(f"Window {window.id} in {room_name} is now closed.")

        # Get the new temperature reading
        temp_sensor.turn_on()
        new_temp = temp_sensor.get_reading()
        temp_sensor.turn_off()

        if new_temp is None:
            print(f"Failed to get new temperature reading from {temp_sensor.id}.")
            return

        print(f"New temperature in {room_name} after opening windows: {new_temp:.2f}°C.")
    else:
        print(f"Current temperature in {room_name} is {current_temp:.2f}°C, which is below the threshold of {TEMP_HIGH}°C. No action needed.")

if __name__ == "__main__":
    from home.home_plan import home_plan

    # Example usage
    home = home_plan()
    open_windows_to_cool_down("LivingRoom")