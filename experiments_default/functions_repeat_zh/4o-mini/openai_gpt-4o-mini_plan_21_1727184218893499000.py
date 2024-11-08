# Based on the provided functional description and the source code of your smart home project, here is a `function.py` file that implements the three plans: Morning Plan, Leave Home Plan, and Movie Plan. This file will also contain a main function that sets up the home environment and executes the plans as needed.

# functions/function.py

from home.home_plan import home_plan, get_room, get_room_actuators, get_all_sensors
from home.actuator import CoffeeMachine, Curtain, Light, Door, SmartTV
from home.sensor import LightIntensiveSensor
import time

def morning_plan(home):
    print("Executing Morning Plan...")
    living_room = get_room(home, "LivingRoom")
    bedroom = get_room(home, "Bedroom")

    # Turn on the curtains and coffee machine
    curtain = next(actuator for actuator in living_room.actuators if isinstance(actuator, Curtain))
    coffee_machine = next(actuator for actuator in kitchen.actuators if isinstance(actuator, CoffeeMachine))
    light_sensor = next(sensor for sensor in bedroom.sensors if isinstance(sensor, LightIntensiveSensor))

    curtain.turn_on()
    coffee_machine.turn_on()
    
    # Check light intensity and adjust light if necessary
    light_intensity = light_sensor.get_reading()
    if light_intensity is not None and light_intensity < 300:  # Example threshold
        light = next(actuator for actuator in living_room.actuators if isinstance(actuator, Light))
        light.turn_on()
        light.set_brightness_level("medium")

    time.sleep(1)  # Simulate some delay
    print("Morning Plan executed successfully.")

def leave_home_plan(home):
    print("Executing Leave Home Plan...")
    living_room = get_room(home, "LivingRoom")

    # Lock the door, turn off lights, and disable sockets
    door = next(actuator for actuator in living_room.actuators if isinstance(actuator, Door))
    light = next(actuator for actuator in living_room.actuators if isinstance(actuator, Light))
    smart_sockets = [actuator for actuator in living_room.actuators if isinstance(actuator, SmartSocket)]

    door.lock()
    light.turn_off()
    for socket in smart_sockets:
        socket.turn_off()

    time.sleep(1)  # Simulate some delay
    print("Leave Home Plan executed successfully.")

def movie_plan(home):
    print("Executing Movie Plan...")
    living_room = get_room(home, "LivingRoom")

    # Close the curtains, dim the lights, and turn on the TV
    curtain = next(actuator for actuator in living_room.actuators if isinstance(actuator, Curtain))
    light = next(actuator for actuator in living_room.actuators if isinstance(actuator, Light))
    tv = next(actuator for actuator in living_room.actuators if isinstance(actuator, SmartTV))

    curtain.turn_off()
    light.turn_on()
    light.set_brightness_level("low")
    tv.turn_on()
    tv.play_channel("Favorite Movie Channel")  # You can replace this with an actual channel name

    time.sleep(1)  # Simulate some delay
    print("Movie Plan executed successfully.")

def main():
    home = home_plan()
    
    # Execute the plans
    morning_plan(home)
    leave_home_plan(home)
    movie_plan(home)

if __name__ == "__main__":
    main()