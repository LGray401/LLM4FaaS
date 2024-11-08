# Based on the functional description you provided for the smart home project, I will create a `function.py` file that includes a main function to handle the described plans: the morning plan, the leave home plan, and the movie plan. 
# 
# This file will integrate the functionalities of `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py` to execute the required actions. Here is how the `function.py` may look:

# functions/function.py

from home.home_plan import home_plan, get_room, get_all_sensors, get_all_actuators
from home.actuator import CoffeeMachine, Door, Light, Curtain, SmartTV
from home.sensor import LightIntensiveSensor

def morning_plan(home):
    print("Executing Morning Plan...")
    
    bedroom = get_room(home, "Bedroom")
    living_room = get_room(home, "LivingRoom")
    
    # Set alarm at 7 AM (simulated by executing this plan)
    curtain = next((act for act in bedroom.actuators if isinstance(act, Curtain)), None)
    coffee_machine = next((act for act in kitchen.actuators if isinstance(act, CoffeeMachine)), None)
    light = next((act for act in living_room.actuators if isinstance(act, Light)), None)
    light_sensor = next((sensor for sensor in bedroom.sensors if isinstance(sensor, LightIntensiveSensor)), None)

    if curtain:
        curtain.turn_on()  # Open curtains
        
    if coffee_machine:
        coffee_machine.turn_on()  # Start coffee machine
        coffee_machine.make_coffee("Espresso")  # Make a coffee

    if light_sensor and light:
        light_sensor_value = light_sensor.get_reading()
        if light_sensor_value < 300:  # Assuming 300 is a significant threshold for dim light
            light.turn_on()
            light.set_brightness_level("medium")  # Set to medium brightness

def leave_home_plan(home):
    print("Executing Leave Home Plan...")
    
    living_room = get_room(home, "LivingRoom")
    
    door = next((act for act in living_room.actuators if isinstance(act, Door)), None)
    light = next((act for act in living_room.actuators if isinstance(act, Light)), None)
    smart_sockets = get_all_actuators(home, "SmartSocket")
    
    if door:
        door.lock()  # Lock the door
        
    if light:
        light.turn_off()  # Turn off the lights
    
    for socket in smart_sockets:
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
        light.turn_on()  # Turn on lights
        light.set_brightness_level("dark")  # Set to dark brightness

    if smart_tv:
        smart_tv.turn_on()  # Turn on TV
        smart_tv.play_channel("Movie Channel")  # Play the movie channel

def main():
    home = home_plan()
    
    # Execute plans
    morning_plan(home)
    leave_home_plan(home)
    movie_plan(home)

if __name__ == "__main__":
    main()