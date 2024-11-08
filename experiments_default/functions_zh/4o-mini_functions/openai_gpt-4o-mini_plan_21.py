# Here's a `function.py` file that implements the required functionalities based on your descriptions for the different plans (Morning Plan, Leave Home Plan, Movie Plan). This file will serve as the main entry point for your smart home project.

# functions/function.py

from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators
from home.actuator import CoffeeMachine, Curtain, Door, Light, SmartTV
from home.sensor import LightIntensiveSensor
import time

def morning_plan(home):
    print("Executing Morning Plan...")
    
    # Get the necessary room and actuators
    bedroom = get_room(home, "Bedroom")
    if bedroom:
        # Set alarm to 7 AM (simulated with a print statement)
        print("Alarm set for 7 AM.")
        
        # Open curtains and start coffee machine
        curtain = next((actuator for actuator in bedroom.actuators if isinstance(actuator, Curtain)), None)
        coffee_machine = next((actuator for actuator in bedroom.actuators if isinstance(actuator, CoffeeMachine)), None)
        light_sensor = next((sensor for sensor in bedroom.sensors if isinstance(sensor, LightIntensiveSensor)), None)

        if curtain:
            curtain.turn_on()
        
        if coffee_machine:
            coffee_machine.turn_on()
            coffee_machine.make_coffee("Regular")

        # Check light intensity
        if light_sensor:
            light_sensor.turn_on()
            light_reading = light_sensor.get_reading()
            if light_reading and light_reading < 300:  # Assuming 300 lux is the threshold for dim light
                light = next((actuator for actuator in bedroom.actuators if isinstance(actuator, Light)), None)
                if light:
                    light.turn_on()
                    light.set_brightness_level("medium")  # Set to medium brightness


def leave_home_plan(home):
    print("Executing Leave Home Plan...")
    
    # Lock the door and turn off lights and smart sockets
    front_door = next((actuator for actuator in get_room_actuators(home, "LivingRoom") if isinstance(actuator, Door)), None)
    lights = get_all_actuators(home, "Light")
    
    if front_door:
        front_door.lock()

    for light in lights:
        light.turn_off()

    # Simulate turning off all smart sockets
    smart_sockets = get_all_actuators(home, "SmartSocket")
    for socket in smart_sockets:
        socket.turn_off()


def movie_plan(home):
    print("Executing Movie Plan...")
    
    # Close curtains, dim lights, and turn on the TV
    living_room = get_room(home, "LivingRoom")
    if living_room:
        curtain = next((actuator for actuator in living_room.actuators if isinstance(actuator, Curtain)), None)
        light = next((actuator for actuator in living_room.actuators if isinstance(actuator, Light)), None)
        smart_tv = next((actuator for actuator in living_room.actuators if isinstance(actuator, SmartTV)), None)

        if curtain:
            curtain.turn_on()
        
        if light:
            light.turn_on()
            light.set_brightness_level("low")  # Dim the lights
        
        if smart_tv:
            smart_tv.turn_on()
            smart_tv.play_channel("Favorite Movie Channel")


def main():
    home = home_plan()  # Create the home plan

    # Execute the plans
    morning_plan(home)
    time.sleep(1)  # Simulate time delay for each plan execution
    leave_home_plan(home)
    time.sleep(1)
    movie_plan(home)


if __name__ == "__main__":
    main()