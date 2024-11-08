# Based on your functional description and the provided source code, I'll create a `function.py` file that will reside in the `functions` folder. This file will contain the main function to handle the specified functionalities:
# 
# 1. Automatically close doors and windows when the air conditioner (AC) is turned on.
# 2. Prompt the user to open the window for cooling when the indoor temperature is higher than the outdoor temperature.
# 
# Here's the `function.py` file:

# function.py
import time
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor
from home.actuator import AC, Window, Door, NotificationSender
from home.home_plan import home_plan, get_room_actuators, get_all_sensors, get_room

def main():
    home = home_plan()

    # Example room to demonstrate functionality
    room_name = "LivingRoom"
    room = get_room(home, room_name)

    if room:
        # Get actuators and sensors for the room
        ac = next((actuator for actuator in room.actuators if isinstance(actuator, AC)), None)
        windows = [actuator for actuator in room.actuators if isinstance(actuator, Window)]
        doors = [actuator for actuator in room.actuators if isinstance(actuator, Door)]
        indoor_temp_sensor = next((sensor for sensor in room.sensors if isinstance(sensor, IndoorTemperatureSensor)), None)
        outdoor_temp_sensor = next((sensor for sensor in room.sensors if isinstance(sensor, OutdoorTemperatureSensor)), None)
        notification_sender = next((actuator for actuator in room.actuators if isinstance(actuator, NotificationSender)), None)

        # Ensure all components are available
        if not all([ac, windows, doors, indoor_temp_sensor, outdoor_temp_sensor, notification_sender]):
            print("Missing components in the room to perform the required operations.")
            return

        # Turn on sensors
        indoor_temp_sensor.turn_on()
        outdoor_temp_sensor.turn_on()

        # Simulate AC turning on
        ac.turn_on()

        # Close all doors and windows when AC is on
        for window in windows:
            window.turn_off()
        for door in doors:
            door.lock()

        # Get temperature readings
        indoor_temp = indoor_temp_sensor.get_reading()
        outdoor_temp = outdoor_temp_sensor.get_reading()

        # Check if indoor temperature is higher than outdoor temperature
        if indoor_temp and outdoor_temp and indoor_temp > outdoor_temp:
            notification_sender.turn_on()
            notification_sender.notification_sender("Indoor temperature is higher than outdoor temperature. Open windows to cool down?")
            response = input("Do you want to open the windows to cool down? (yes/no): ").strip().lower()
            if response == "yes":
                for window in windows:
                    window.turn_on()

if __name__ == "__main__":
    main()