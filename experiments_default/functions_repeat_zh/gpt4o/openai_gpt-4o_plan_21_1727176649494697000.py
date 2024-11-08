# Here is the `function.py` file based on the provided functional description and the given source code files:

import time
from home.home_plan import home_plan, get_room, get_all_sensors
from home.actuator import SmartTV, CoffeeMachine, Curtain, Light, Door, SmartSocket

def morning_plan(home):
    print("Starting Morning Plan...")

    # Find the curtain in the Bedroom
    bedroom = get_room(home, "Bedroom")
    curtain = next((actuator for actuator in bedroom.actuators if isinstance(actuator, Curtain)), None)
    coffee_maker = next((actuator for actuator in bedroom.actuators if isinstance(actuator, CoffeeMachine)), None)
    light = next((actuator for actuator in bedroom.actuators if isinstance(actuator, Light)), None)

    if curtain:
        curtain.turn_on()
        print("Curtain is opened in the Bedroom.")
    if coffee_maker:
        coffee_maker.turn_on()
        coffee_maker.make_coffee("Espresso")
        print("Coffee Maker is turned on in the Bedroom.")
    if light:
        light.turn_on()
        light.set_brightness_level("medium")

    # Check light intensity
    light_sensors = get_all_sensors(home, "LightIntensive")
    for sensor in light_sensors:
        sensor.turn_on()
        reading = sensor.get_reading()
        if reading and reading < 300:
            light.turn_on()
            light.set_brightness_level("medium")

def leave_home_plan(home):
    print("Starting Leave Home Plan...")

    door = next((actuator for actuator in home.actuators if isinstance(actuator, Door)), None)
    lights = get_all_actuators(home, "Light")
    sockets = get_all_actuators(home, "SmartSocket")
    
    if door:
        door.lock()
        print("Door is locked.")
        
    for light in lights:
        light.turn_off()
        print(f"Light {light.id} is turned off.")
        
    for socket in sockets:
        socket.turn_off()
        print(f"SmartSocket {socket.id} is turned off.")

def movie_plan(home):
    print("Starting Movie Plan...")

    living_room = get_room(home, "LivingRoom")
    curtain = next((actuator for actuator in living_room.actuators if isinstance(actuator, Curtain)), None)
    light = next((actuator for actuator in living_room.actuators if isinstance(actuator, Light)), None)
    tv = next((actuator for actuator in living_room.actuators if isinstance(actuator, SmartTV)), None)

    if curtain:
        curtain.turn_off()
        print("Curtain is closed in the LivingRoom.")
    if light:
        light.turn_on()
        light.set_brightness_level("low")
        print("Light is set to low brightness in the LivingRoom.")
    if tv:
        tv.turn_on()
        tv.play_channel("Movie Channel")
        print("TV is turned on and movie is playing in the LivingRoom.")

def main():
    home = home_plan()
    
    # Execute the plans
    morning_plan(home)
    time.sleep(1)
    leave_home_plan(home)
    time.sleep(1)
    movie_plan(home)
    
if __name__ == "__main__":
    main()