# To implement the functional description in your `function.py` file, we'll need to create logic that automatically closes doors and windows when the air conditioner (AC) is turned on. Additionally, it will prompt the user if they want to open a window when the indoor temperature is higher than the outdoor temperature.
# 
# Here's the `function.py` file that implements this functionality:
# 
# ```python
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor
from home.actuator import AC, Window, Door, NotificationSender
from home.home_plan import home_plan, get_room_actuators, get_room_sensors
from home.config import TEMP_CHANGE_DURATION_WINDOW


def check_and_control_temperature(room_name, home):
    # Get the room actuators and sensors
    actuators = get_room_actuators(home, room_name)
    sensors = get_room_sensors(home, room_name)

    # Find AC, windows, and doors in the room
    ac = next((a for a in actuators if isinstance(a, AC)), None)
    windows = [a for a in actuators if isinstance(a, Window)]
    doors = [a for a in actuators if isinstance(a, Door)]
    notification_sender = next((a for a in actuators if isinstance(a, NotificationSender)), None)

    # Find indoor and outdoor temperature sensors
    indoor_temp_sensor = next((s for s in sensors if isinstance(s, IndoorTemperatureSensor)), None)
    outdoor_temp_sensor = next((s for s in sensors if isinstance(s, OutdoorTemperatureSensor)), None)

    # Ensure sensors are turned on to get readings
    if indoor_temp_sensor:
        indoor_temp_sensor.turn_on()
    if outdoor_temp_sensor:
        outdoor_temp_sensor.turn_on()

    # Get temperature readings
    indoor_temp = indoor_temp_sensor.get_reading() if indoor_temp_sensor else None
    outdoor_temp = outdoor_temp_sensor.get_reading() if outdoor_temp_sensor else None

    # If AC is turned on, close windows and doors
    if ac and ac.get_status() == 'on':
        for window in windows:
            window.turn_off()  # Assuming turning off means closing the window
        for door in doors:
            door.turn_off()  # Assuming turning off means closing the door

    # If indoor temperature is higher than outdoor temperature, notify the user
    if indoor_temp and outdoor_temp and indoor_temp > outdoor_temp:
        if notification_sender:
            notification_sender.turn_on()
            message = f"Indoor temperature ({indoor_temp}°C) is higher than outdoor temperature ({outdoor_temp}°C). Would you like to open a window to cool down?"
            notification_sender.notification_sender(message)


def main():
    # Create home plan
    home = home_plan()

    # Check and control temperature for each room
    for room in home:
        check_and_control_temperature(room.name, home)


if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation
# 
# 1. **Import Statements**: We import the necessary classes from other modules (`sensor.py`, `actuator.py`, `home_plan.py`, `config.py`).
# 
# 2. **check_and_control_temperature**: This function takes a room name and the home plan as parameters. It retrieves the sensors and actuators for the specified room.
# 
# 3. **AC Control**: If the AC is turned on, it automatically closes all windows and doors in the room.
# 
# 4. **Temperature Comparison**: It compares the indoor and outdoor temperatures. If the indoor temperature is higher than the outdoor temperature, it sends a notification to the user asking if they want to open a window.
# 
# 5. **main Function**: This function initializes the home plan and iterates through each room to perform temperature checks and controls.
# 
# This implementation assumes that turning off a window or door actuator means closing them. If the logic is different, adjust the `turn_off` method calls accordingly.