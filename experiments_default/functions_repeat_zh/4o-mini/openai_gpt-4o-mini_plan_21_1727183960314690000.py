# Based on the functional description you provided, I will create a `function.py` file that includes implementations for the "Morning Plan", "Leave Home Plan", and "Movie Plan". This file will utilize the classes from your existing code in `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py`.
# 
# Here's how the `function.py` file is structured:
# 
# 1. **Morning Plan**: Sets the alarm, opens curtains, starts the coffee machine, and adjusts lighting based on sunlight intensity.
# 2. **Leave Home Plan**: Locks the door, turns off the lights, and cuts power to all smart sockets.
# 3. **Movie Plan**: Closes the curtains, dims the lights, and plays a movie on the smart TV.
# 
# The file will also include a main function to test these plans.
# 
# Here’s the content for `function.py`:

# functions/function.py

from home.home_plan import home_plan
from home.actuator import Curtain, CoffeeMachine, Light, Door, SmartTV
from home.sensor import LightIntensiveSensor
from home.logger_config import logger

def morning_plan(home):
    logger.info("Executing Morning Plan.")
    print("Executing Morning Plan.")

    # Assume we have a designated room for the morning plan
    living_room = home[0]  # Assuming LivingRoom is at index 0
    kitchen = home[2]  # Assuming Kitchen is at index 2

    # Open curtains
    curtains = [actuator for actuator in living_room.actuators if isinstance(actuator, Curtain)]
    for curtain in curtains:
        curtain.turn_on()
    
    # Start coffee machine
    coffee_machine = next((actuator for actuator in kitchen.actuators if isinstance(actuator, CoffeeMachine)), None)
    if coffee_machine:
        coffee_machine.turn_on()
        coffee_machine.make_coffee("Espresso")

    # Check light intensity and adjust lights
    light_sensor = next((sensor for sensor in living_room.sensors if isinstance(sensor, LightIntensiveSensor)), None)
    light = next((actuator for actuator in living_room.actuators if isinstance(actuator, Light)), None)

    if light_sensor and light:
        light_sensor.turn_on()  # Ensure sensor is on
        light_intensity = light_sensor.get_reading()
        if light_intensity is not None and light_intensity < 300:  # Assuming 300 is the threshold for dim light
            light.turn_on()
            light.set_brightness_level("medium")
        else:
            light.turn_off()

def leave_home_plan(home):
    logger.info("Executing Leave Home Plan.")
    print("Executing Leave Home Plan.")

    # Lock the door
    living_room = home[0]  # Assuming LivingRoom is at index 0
    door = next((actuator for actuator in living_room.actuators if isinstance(actuator, Door)), None)
    if door:
        door.lock()

    # Turn off lights
    lights = [actuator for actuator in living_room.actuators if isinstance(actuator, Light)]
    for light in lights:
        light.turn_off()

    # Turn off smart sockets
    smart_sockets = [actuator for actuator in living_room.actuators if isinstance(actuator, SmartSocket)]
    for socket in smart_sockets:
        socket.turn_off()

def movie_plan(home):
    logger.info("Executing Movie Plan.")
    print("Executing Movie Plan.")

    # Close curtains
    living_room = home[0]  # Assuming LivingRoom is at index 0
    curtains = [actuator for actuator in living_room.actuators if isinstance(actuator, Curtain)]
    for curtain in curtains:
        curtain.turn_off()

    # Dim lights
    light = next((actuator for actuator in living_room.actuators if isinstance(actuator, Light)), None)
    if light:
        light.turn_on()
        light.set_brightness_level("low")

    # Play movie on Smart TV
    smart_tv = next((actuator for actuator in living_room.actuators if isinstance(actuator, SmartTV)), None)
    if smart_tv:
        smart_tv.turn_on()
        smart_tv.play_channel("Movie Channel")

def main():
    home = home_plan()
    
    # Execute the plans
    morning_plan(home)
    leave_home_plan(home)
    movie_plan(home)

if __name__ == "__main__":
    main()