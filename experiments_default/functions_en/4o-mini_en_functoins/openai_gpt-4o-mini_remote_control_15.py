# Based on the provided functional description, I will create a `function.py` file that serves as the main entry point of your smart home project. This file will initialize the home plan, and allow interaction with the sensors and actuators within the rooms of the home.
# 
# Here is the content for `function.py`:

# function.py
from home.home_plan import home_plan, print_home_plan, get_room, get_room_sensors, get_room_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH

def main():
    # Initialize the home plan
    home = home_plan()
    
    # Print the home plan
    print_home_plan(home)

    # Example: Get a specific room and its sensors and actuators
    room_name = "LivingRoom"  # You can change this to any room you want to query
    room = get_room(home, room_name)
    
    if room:
        # Get and print sensors in the room
        sensors = get_room_sensors(home, room_name)
        if sensors:
            for sensor in sensors:
                sensor.turn_on()  # Turn on each sensor to get readings
                sensor.get_reading()  # Get the reading from the sensor
                sensor.turn_off()  # Turn off the sensor

        # Get and print actuators in the room
        actuators = get_room_actuators(home, room_name)
        if actuators:
            for actuator in actuators:
                actuator.turn_on()  # Turn on each actuator
                actuator.get_status()  # Get the status of the actuator
                actuator.turn_off()  # Turn off the actuator

    # Example: You can implement conditional checks based on sensor readings
    # to control actuators, e.g., controlling temperature based on readings
    # This is just a template for how you might expand functionality.

if __name__ == "__main__":
    main()