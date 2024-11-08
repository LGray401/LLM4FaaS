# Based on the functional description and the provided source code, you need to create a `function.py` file that contains a main function. This function should control the smart home system to automatically close doors and windows when the air conditioner is on, and ask whether to open windows to cool down when the temperature inside the house is high and outside is low.
#
# Here is a high-level pseudocode of what the main function in `function.py` should do:
#
# 1. Import necessary modules and classes from `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py`.
# 2. Create an instance of the home plan.
# 3. For each room in the home:
# - Get the indoor and outdoor temperature readings.
# - If the air conditioner is on, close all doors and windows.
# - If the indoor temperature is high and the outdoor temperature is low, send a notification to ask whether to open the windows to cool down.
#
# Now, let's translate this pseudocode into Python code:
#
# ```python
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor
from home.actuator import AC, Window, Door, NotificationSender
from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.config import TEMP_HIGH

def main():
    home = home_plan()

    for room in home:
        # Get sensors and actuators in the room
        sensors = get_room_sensors(home, room.name)
        actuators = get_room_actuators(home, room.name)

        # Get indoor and outdoor temperature sensors
        indoor_temp_sensor = next((s for s in sensors if isinstance(s, IndoorTemperatureSensor)), None)
        outdoor_temp_sensor = next((s for s in sensors if isinstance(s, OutdoorTemperatureSensor)), None)

        # Get AC, windows, doors, and notification sender
        ac = next((a for a in actuators if isinstance(a, AC)), None)
        windows = [a for a in actuators if isinstance(a, Window)]
        doors = [a for a in actuators if isinstance(a, Door)]
        notification_sender = next((a for a in actuators if isinstance(a, NotificationSender)), None)

        # If AC is on, close all windows and doors
        if ac and ac.get_status() == "on":
            for window in windows:
                window.turn_off()
            for door in doors:
                door.turn_off()

        # If indoor temperature is high and outdoor temperature is low, send a notification
        if indoor_temp_sensor and outdoor_temp_sensor and notification_sender:
            indoor_temp = indoor_temp_sensor.get_reading()
            outdoor_temp = outdoor_temp_sensor.get_reading()

            if indoor_temp > TEMP_HIGH and outdoor_temp < indoor_temp:
                notification_sender.turn_on()
                notification_sender.notification_sender("The indoor temperature is high and the outdoor temperature is low. Do you want to open the windows to cool down?")

if __name__ == "__main__":
    main()
# ```
#
# This `function.py` file should be placed in the 'functions' folder as per your project structure. The main function will be executed when you run this file. It uses the classes and functions defined in `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py` to control the smart home system according to the functional description.