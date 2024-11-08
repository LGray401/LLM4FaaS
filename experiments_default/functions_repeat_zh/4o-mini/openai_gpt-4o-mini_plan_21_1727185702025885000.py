# Based on the provided functional description and the existing source code, we will create a `function.py` file that implements the three plans: the Morning Plan, Leave Home Plan, and Movie Plan. This file will use the classes defined in your existing code to perform the necessary actions for each plan.
# 
# Here is the `function.py` file:

# functions/function.py

from home.home_plan import home_plan
from home.actuator import CoffeeMachine, Door, Light, Curtain, SmartTV
from home.sensor import LightIntensiveSensor

def morning_plan(home):
    print("Executing Morning Plan...")
    
    # Get the required actuators and sensors
    coffee_machine = get_actuator(home, 'CoffeeMachine')
    curtain = get_actuator(home, 'Curtain')
    light = get_actuator(home, 'Light')
    light_sensor = get_sensor(home, 'LightIntensive')

    # Set alarm time (simulated)
    alarm_time = "07:00"
    print(f"Alarm set for {alarm_time}.")
    
    # Open curtains
    curtain.turn_on()

    # Start coffee machine
    coffee_machine.turn_on()
    coffee_machine.make_coffee("Espresso")

    # Check light intensity and adjust light if necessary
    if light_sensor:
        light_sensor.turn_on()  # Turn on the sensor
        light_intensity = light_sensor.get_reading()  # Get the reading
        if light_intensity < 300:  # Assuming 300 is the threshold for dark
            light.turn_on()
            light.set_brightness_level("medium")

def leave_home_plan(home):
    print("Executing Leave Home Plan...")
    
    # Get the required actuators
    door = get_actuator(home, 'Door')
    light = get_actuator(home, 'Light')
    smart_sockets = get_all_actuators(home, 'SmartSocket')

    # Lock the door
    door.lock()

    # Turn off lights
    light.turn_off()

    # Turn off all smart sockets
    for socket in smart_sockets:
        socket.turn_off()

def movie_plan(home):
    print("Executing Movie Plan...")
    
    # Get the required actuators
    curtain = get_actuator(home, 'Curtain')
    light = get_actuator(home, 'Light')
    tv = get_actuator(home, 'SmartTV')

    # Close curtains
    curtain.turn_off()

    # Dim lights
    light.turn_on()
    light.set_brightness_level("low")

    # Play movie on TV
    tv.turn_on()
    tv.play_channel("Favorite Movie Channel")

def get_actuator(home, actuator_type):
    for room in home:
        for actuator in room.actuators:
            if actuator.actuator_type == actuator_type:
                return actuator
    print(f"No actuator of type {actuator_type} found.")
    return None

def get_sensor(home, sensor_type):
    for room in home:
        for sensor in room.sensors:
            if sensor.sensor_type == sensor_type:
                return sensor
    print(f"No sensor of type {sensor_type} found.")
    return None

def get_all_actuators(home, actuator_type):
    all_actuators = []
    for room in home:
        for actuator in room.actuators:
            if actuator.actuator_type == actuator_type:
                all_actuators.append(actuator)
    return all_actuators

def main():
    home = home_plan()  # Create the home plan
    morning_plan(home)  # Execute Morning Plan
    leave_home_plan(home)  # Execute Leave Home Plan
    movie_plan(home)  # Execute Movie Plan

if __name__ == "__main__":
    main()