# Based on the provided functional description and source code, here's the `function.py` file that includes a `main` function which can be used to interact with the smart home system. It will allow you to turn on sensors and actuators, get sensor readings, and perform other actions.

# function.py
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, OutdoorTemperatureSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, SmartSocket, Door, \
    CleaningRobot, SmartTV, Humidifier
from home.logger_config import logger
from home_plan import home_plan

def main():
    # Create the home plan
    home = home_plan()
    
    # Example usage:
    # Get a room
    living_room = get_room(home, "LivingRoom")
    
    # Get sensors and actuators in a room
    sensors = get_room_sensors(living_room, "LivingRoom")
    actuators = get_room_actuators(living_room, "LivingRoom")
    
    # Turn on a sensor
    if sensors:
        temp_sensor = sensors[0]  # Assuming the first sensor is the indoor temperature sensor
        temp_sensor.turn_on()
    
    # Get a reading from the sensor
    reading = temp_sensor.get_reading()
    print(f"Temperature reading: {reading}°C")
    
    # Turn on an actuator
    if actuators:
        light = actuators[0]  # Assuming the first actuator is a light
        light.turn_on()
    
    # Turn off the actuator
    light.turn_off()
    
    # Perform other actions...
    # ...

# Helper functions used in main
def get_room(home, room_name):
    for room in home:
        if room.name == room_name:
            return room
    return None

def get_room_sensors(room, room_name):
    return room.sensors

def get_room_actuators(room, room_name):
    return room.actuators

# Run the main function
if __name__ == "__main__":
    main()