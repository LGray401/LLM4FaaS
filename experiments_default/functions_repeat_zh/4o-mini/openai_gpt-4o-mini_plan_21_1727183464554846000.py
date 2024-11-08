# Based on the provided functional description and source code, I will create the `function.py` file that implements the three plans: "MORNING PLAN", "LEAVE HOME PLAN", and "MOVIE PLAN". This file will utilize the classes and methods defined in your existing files (`sensor.py`, `actuator.py`, `home_plan.py`, and `config.py`).
# 
# Here is the `function.py` file:

# functions/function.py

from home.home_plan import home_plan
from home.actuator import CoffeeMachine, Curtain, Light, Door, SmartTV
from home.sensor import LightIntensiveSensor

def morning_plan(home):
    print("\n--- Morning Plan Activated ---")
    
    # Get relevant components
    living_room = home[0]  # Assuming living room is the first room
    bedroom = home[1]      # Assuming bedroom is the second room

    # Set the alarm (not implemented, just a placeholder)
    print("Setting alarm to 7 AM...")

    # Open curtains and start coffee machine
    curtain = next(actor for actor in living_room.actuators if isinstance(actor, Curtain))
    coffee_machine = next(actor for actor in kitchen.actuators if isinstance(actor, CoffeeMachine))
    light_sensor = next(sensor for sensor in living_room.sensors if isinstance(sensor, LightIntensiveSensor))

    curtain.turn_on()
    coffee_machine.turn_on()
    coffee_machine.make_coffee("Espresso")  # You can specify the type of coffee

    # Check light intensity and adjust lights
    light_sensor.turn_on()
    light_intensity = light_sensor.get_reading()
    if light_intensity is not None and light_intensity < 300:  # Example threshold
        light = next(actor for actor in living_room.actuators if isinstance(actor, Light))
        light.turn_on()
        light.set_brightness_level("medium")

def leave_home_plan(home):
    print("\n--- Leave Home Plan Activated ---")
    
    living_room = home[0]  # Assuming living room is the first room
    door = next(actor for actor in living_room.actuators if isinstance(actor, Door))
    light = next(actor for actor in living_room.actuators if isinstance(actor, Light))
    smart_sockets = [actor for actor in living_room.actuators if isinstance(actor, SmartSocket)]

    # Lock the door
    door.lock()
    
    # Turn off lights
    light.turn_off()
    
    # Turn off all smart sockets
    for socket in smart_sockets:
        socket.turn_off()

def movie_plan(home):
    print("\n--- Movie Plan Activated ---")
    
    living_room = home[0]  # Assuming living room is the first room
    curtain = next(actor for actor in living_room.actuators if isinstance(actor, Curtain))
    light = next(actor for actor in living_room.actuators if isinstance(actor, Light))
    smart_tv = next(actor for actor in living_room.actuators if isinstance(actor, SmartTV))

    # Close curtains
    curtain.turn_off()
    
    # Dim lights
    light.turn_on()
    light.set_brightness_level("low")

    # Play movie on TV
    smart_tv.turn_on()
    smart_tv.play_channel("Favorite Movie Channel")  # You can specify the channel

def main():
    home = home_plan()

    # Example calls to the plans
    morning_plan(home)
    leave_home_plan(home)
    movie_plan(home)

if __name__ == "__main__":
    main()