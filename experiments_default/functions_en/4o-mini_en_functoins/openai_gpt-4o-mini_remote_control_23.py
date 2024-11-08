# Based on your functional description and the provided source code, I will create a `function.py` file that establishes a network control system for your smart home project. The `function.py` file will contain a `main` function that initializes the home system, creates rooms with sensors and actuators, and allows for basic interaction with them.
# 
# Here's how the `function.py` file will look:

# functions/function.py
from home.home_plan import home_plan, print_home_plan, get_room, get_room_sensors, get_room_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, \
    OutdoorTemperatureSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, \
    SmartSocket, Door, CleaningRobot, SmartTV
import random

def main():
    # Initialize the home plan
    home = home_plan()
    
    # Print the home plan
    print_home_plan(home)

    # Example interaction: Get a specific room's details
    room_name = "LivingRoom"
    room = get_room(home, room_name)
    
    if room:
        # Show sensors and actuators in the room
        sensors = get_room_sensors(home, room_name)
        actuators = get_room_actuators(home, room_name)

        # Simulate reading from sensors
        for sensor in sensors:
            sensor.turn_on()
            sensor.get_reading()
            sensor.turn_off()

        # Simulate actuating devices
        for actuator in actuators:
            actuator.turn_on()
            print(f"Actuator ID: {actuator.id} is currently {actuator.get_status()}")
            actuator.turn_off()

    # Additional functionality can be added here as needed


if __name__ == "__main__":
    main()