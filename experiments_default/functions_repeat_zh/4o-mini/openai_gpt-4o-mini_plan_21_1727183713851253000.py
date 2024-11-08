# Based on your functional description and the provided source code, here is a `function.py` file that implements the morning plan, leave home plan, and movie plan functionalities. This module will utilize the existing sensors and actuators to perform the specified actions.

# functions/function.py

from home.home_plan import home_plan, get_room, get_room_actuators, get_all_sensors
from home.actuator import Door, CoffeeMachine, Curtain, Light, SmartTV
from home.sensor import LightIntensiveSensor

def morning_plan(home):
    print("Executing Morning Plan...")
    living_room = get_room(home, "LivingRoom")
    bedroom = get_room(home, "Bedroom")

    # Set alarm time (for simulation purposes)
    alarm_time = "07:00"
    print(f"Alarm set for {alarm_time}.")

    # Open curtains, start coffee machine, adjust lights
    curtain = next((act for act in living_room.actuators if isinstance(act, Curtain)), None)
    coffee_machine = next((act for act in kitchen.actuators if isinstance(act, CoffeeMachine)), None)
    light = next((act for act in living_room.actuators if isinstance(act, Light)), None)
    
    # Simulate checking light intensity
    light_sensor = next((sensor for sensor in bedroom.sensors if isinstance(sensor, LightIntensiveSensor)), None)
    if light_sensor:
        light_sensor.turn_on()  # Turn on the light sensor to get readings
        light_intensity = light_sensor.get_reading()
        light_sensor.turn_off()
        
        if light_intensity is not None and light_intensity < 500:  # Check if it's dark
            if light:
                light.turn_on()
                light.set_brightness_level("medium")  # Set brightness to medium
    
    if curtain:
        curtain.turn_on()  # Open curtains
    if coffee_machine:
        coffee_machine.turn_on()  # Start coffee machine

def leave_home_plan(home):
    print("Executing Leave Home Plan...")
    living_room = get_room(home, "LivingRoom")
    
    door = next((act for act in living_room.actuators if isinstance(act, Door)), None)
    lights = get_all_sensors(home, "Light")  # Get all lights to turn off
    sockets = get_all_sensors(home, "SmartSocket")  # Get all smart sockets to turn off
    
    if door:
        door.lock()  # Lock the door
    for light in lights:
        light.turn_off()  # Turn off lights
    for socket in sockets:
        socket.turn_off()  # Turn off all smart sockets

def movie_plan(home):
    print("Executing Movie Plan...")
    living_room = get_room(home, "LivingRoom")
    
    curtain = next((act for act in living_room.actuators if isinstance(act, Curtain)), None)
    light = next((act for act in living_room.actuators if isinstance(act, Light)), None)
    smart_tv = next((act for act in living_room.actuators if isinstance(act, SmartTV)), None)

    if curtain:
        curtain.turn_off()  # Close curtains
    if light:
        light.turn_on()
        light.set_brightness_level("low")  # Set brightness to low
    if smart_tv:
        smart_tv.turn_on()
        smart_tv.play_channel("Movie Channel")  # Play the movie channel

def main():
    home = home_plan()  # Create home plan
    morning_plan(home)  # Execute morning plan
    leave_home_plan(home)  # Execute leave home plan
    movie_plan(home)  # Execute movie plan

if __name__ == "__main__":
    main()