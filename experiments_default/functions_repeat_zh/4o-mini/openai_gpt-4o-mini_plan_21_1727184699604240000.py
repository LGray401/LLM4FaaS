# Based on your functional description and the provided source code, I will create a `function.py` file that implements the three plans: Morning Plan, Leave Home Plan, and Movie Plan. This file will contain a main function that executes these plans using the classes defined in your project.
# 
# Here's the content for `function.py`:

# function.py
from home.home_plan import home_plan, get_room, get_room_actuators, get_room_sensors
from home.actuator import CoffeeMachine, Door, Light, Curtain, SmartTV
from home.sensor import LightIntensiveSensor

def morning_plan(home):
    print("Executing Morning Plan...")
    
    # Get the bedroom and kitchen
    bedroom = get_room(home, "Bedroom")
    kitchen = get_room(home, "Kitchen")

    # Set the alarm (simulating it)
    print("Setting alarm for 7:00 AM...")

    # Open curtains and start coffee machine
    curtain = get_room_actuators(bedroom, "Curtain")[0]  # Assuming there's at least one curtain in the bedroom
    coffee_machine = get_room_actuators(kitchen, "CoffeeMachine")[0]  # Assuming there's a coffee machine in the kitchen
    light_sensor = get_room_sensors(bedroom, "LightIntensiveSensor")[0]  # Assuming there's a light intensity sensor

    curtain.turn_on()
    coffee_machine.turn_on()
    coffee_machine.make_coffee("regular")

    # Check light intensity and adjust lighting
    light_intensity = light_sensor.get_reading()
    if light_intensity is not None and light_intensity < 500:  # Assuming 500 lux is the threshold for dim light
        light = get_room_actuators(bedroom, "Light")[0]  # Assuming there's at least one light in the bedroom
        light.turn_on()
        light.set_brightness_level("medium")

def leave_home_plan(home):
    print("Executing Leave Home Plan...")
    
    # Lock the door and turn off lights and sockets
    door = get_room_actuators(home, "Door")[0]  # Assuming there's at least one door
    door.lock()

    lights = get_room_actuators(home, "Light")
    for light in lights:
        light.turn_off()

    sockets = get_room_actuators(home, "SmartSocket")
    for socket in sockets:
        socket.turn_off()

def movie_plan(home):
    print("Executing Movie Plan...")
    
    # Close curtains and dim lights, then turn on the TV
    living_room = get_room(home, "LivingRoom")
    curtain = get_room_actuators(living_room, "Curtain")[0]  # Assuming there's at least one curtain in the living room
    light = get_room_actuators(living_room, "Light")[0]  # Assuming there's at least one light in the living room
    smart_tv = get_room_actuators(living_room, "SmartTV")[0]  # Assuming there's at least one TV in the living room

    curtain.turn_off()
    light.set_brightness_level("low")
    smart_tv.turn_on()
    smart_tv.play_channel("Movie Channel")

def main():
    home = home_plan()
    
    # Execute plans
    morning_plan(home)
    leave_home_plan(home)
    movie_plan(home)

if __name__ == "__main__":
    main()