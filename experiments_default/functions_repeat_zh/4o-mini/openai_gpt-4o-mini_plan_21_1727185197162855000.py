# Based on your functional description for the smart home project, I will create the `function.py` file. This file will implement the main function that incorporates the three plans: "MORNING PLAN", "LEAVE HOME PLAN", and "MOVIE PLAN", utilizing the classes defined in your provided source code.
# 
# Here is the content for the `function.py` file:

# functions/function.py

from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators
from home.actuator import Curtain, CoffeeMachine, Light, Door, SmartTV
from home.sensor import LightIntensiveSensor

def morning_plan(home):
    print("Executing MORNING PLAN...")
    
    # Get bedroom and kitchen which are assumed to have the required actuators and sensors
    bedroom = get_room(home, "Bedroom")
    kitchen = get_room(home, "Kitchen")

    # Set alarm (simulated)
    print("Alarm set for 7:00 AM.")

    # Open curtains in the bedroom
    curtain = next((actuator for actuator in get_room_actuators(home, "Bedroom") if isinstance(actuator, Curtain)), None)
    if curtain:
        curtain.turn_on()
    
    # Start coffee machine
    coffee_machine = next((actuator for actuator in get_room_actuators(home, "Kitchen") if isinstance(actuator, CoffeeMachine)), None)
    if coffee_machine:
        coffee_machine.turn_on()
        coffee_machine.make_coffee("espresso")  # Specify coffee type if needed

    # Check light intensity sensor and adjust lighting
    light_sensor = next((sensor for sensor in get_room_sensors(home, "Bedroom") if isinstance(sensor, LightIntensiveSensor)), None)
    light = next((actuator for actuator in get_room_actuators(home, "Bedroom") if isinstance(actuator, Light)), None)

    if light_sensor and light:
        light_sensor.turn_on()
        light_reading = light_sensor.get_reading()
        if light_reading and light_reading < 300:  # Assuming 300 lux is the threshold for light adjustment
            light.turn_on()
            light.set_brightness_level("medium")

def leave_home_plan(home):
    print("Executing LEAVE HOME PLAN...")

    # Lock the door
    door = next((actuator for actuator in get_room_actuators(home, "LivingRoom") if isinstance(actuator, Door)), None)
    if door:
        door.lock()

    # Turn off lights
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_off()

    # Turn off all smart sockets (assumed)
    smart_sockets = get_all_actuators(home, "SmartSocket")
    for socket in smart_sockets:
        socket.turn_off()

def movie_plan(home):
    print("Executing MOVIE PLAN...")

    # Close curtains
    living_room_curtain = next((actuator for actuator in get_room_actuators(home, "LivingRoom") if isinstance(actuator, Curtain)), None)
    if living_room_curtain:
        living_room_curtain.turn_off()

    # Dim lights
    living_room_light = next((actuator for actuator in get_room_actuators(home, "LivingRoom") if isinstance(actuator, Light)), None)
    if living_room_light:
        living_room_light.set_brightness_level("low")

    # Turn on SmartTV
    smart_tv = next((actuator for actuator in get_room_actuators(home, "LivingRoom") if isinstance(actuator, SmartTV)), None)
    if smart_tv:
        smart_tv.turn_on()
        smart_tv.play_channel("Movie Channel")  # Specify channel name if needed

def main():
    home = home_plan()  # Get the home plan with rooms and components

    # Execute the plans based on some conditions or triggers
    morning_plan(home)
    leave_home_plan(home)
    movie_plan(home)

if __name__ == "__main__":
    main()