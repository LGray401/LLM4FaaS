# Based on your functional description and the provided source code for your smart home project, I'll create the `function.py` file located in the `functions` folder. This file will contain the main function to implement the three plans: MORNING PLAN, LEAVE HOME PLAN, and MOVIE PLAN.
# 
# Here is the `function.py` file:

# function.py
from home.home_plan import home_plan, get_room, get_all_actuators
from home.config import LIGHT_INTENSITY_LOW
from home.sensor import LightIntensiveSensor
from home.actuator import Light, CoffeeMachine, Curtain, Door, SmartSocket, SmartTV

def morning_plan(home):
    living_room = get_room(home, "LivingRoom")
    kitchen = get_room(home, "Kitchen")
    
    curtain_living = next(actuator for actuator in living_room.actuators if isinstance(actuator, Curtain))
    curtain_living.turn_on()
    
    coffee_machine = next(actuator for actuator in kitchen.actuators if isinstance(actuator, CoffeeMachine))
    coffee_machine.turn_on()
    coffee_machine.make_coffee("Espresso")
    
    light_sensors = get_all_actuators(home, "Light")
    for sensor in light_sensors:
        if isinstance(sensor, LightIntensiveSensor):
            light_intensity = sensor.get_reading()
            if light_intensity and light_intensity < LIGHT_INTENSITY_LOW:
                light_actuators = get_all_actuators(home, "Light")
                for light in light_actuators:
                    light.turn_on()
                    light.set_brightness_level("medium")

def leave_home_plan(home):
    all_doors = get_all_actuators(home, "Door")
    for door in all_doors:
        door.lock()
        
    all_lights = get_all_actuators(home, "Light")
    for light in all_lights:
        light.turn_off()

    all_sockets = get_all_actuators(home, "SmartSocket")
    for socket in all_sockets:
        socket.turn_off()

def movie_plan(home):
    living_room = get_room(home, "LivingRoom")
    
    curtain_living = next(actuator for actuator in living_room.actuators if isinstance(actuator, Curtain))
    curtain_living.turn_off()
    
    light_actuators = get_all_actuators(home, "Light")
    for light in light_actuators:
        light.turn_on()
        light.set_brightness_level("low")
    
    smart_tv = next(actuator for actuator in living_room.actuators if isinstance(actuator, SmartTV))
    smart_tv.turn_on()
    smart_tv.play_channel("movie")

def main():
    home = home_plan()
    
    print("Executing MORNING PLAN...")
    morning_plan(home)
    
    print("\nExecuting LEAVE HOME PLAN...")
    leave_home_plan(home)
    
    print("\nExecuting MOVIE PLAN...")
    movie_plan(home)

if __name__ == "__main__":
    main()