# Based on the provided functional description and source code for your smart home project, I will create a `function.py` file for you. This file will include a main function that can interact with the sensors and actuators, demonstrating their functionality.
# 
# Here is a sample `function.py` file:

# function.py

from home.home_plan import home_plan, print_home_plan, get_room, get_room_sensors, get_room_actuators
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor, HumiditySensor
from home.actuator import Light, AC, Heater, NotificationSender, MusicPlayer

def main():
    # Initialize the home plan
    home = home_plan()

    # Print the home plan
    print_home_plan(home)

    # Example: Interact with a specific room
    room_name = "LivingRoom"
    living_room = get_room(home, room_name)

    if living_room:
        # Get sensors in the living room
        sensors = get_room_sensors(home, room_name)
        if sensors:
            for sensor in sensors:
                sensor.turn_on()  # Turn on each sensor
                sensor.get_reading()  # Get readings from the sensor
                sensor.turn_off()  # Turn off each sensor

        # Get actuators in the living room
        actuators = get_room_actuators(home, room_name)
        if actuators:
            for actuator in actuators:
                actuator.turn_on()  # Turn on each actuator
                if isinstance(actuator, Light):
                    actuator.set_brightness_level("medium")  # Set brightness for light
                elif isinstance(actuator, AC):
                    actuator.set_target_temperature(22)  # Set target temperature for AC
                elif isinstance(actuator, Heater):
                    actuator.set_target_temperature(24)  # Set target temperature for Heater
                elif isinstance(actuator, NotificationSender):
                    actuator.notification_sender("Welcome to the Living Room!")
                actuator.get_status()  # Get the status of each actuator
                actuator.turn_off()  # Turn off each actuator

if __name__ == "__main__":
    main()