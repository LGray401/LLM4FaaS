# Sure, based on your functional description and the provided source code, here is the `function.py` file located in the `functions` folder. This script will implement the main function to handle the three plans: `MORNING PLAN`, `LEAVE HOME PLAN`, and `MOVIE PLAN`.

# functions/function.py

from home.home_plan import home_plan, get_all_actuators, get_all_sensors
from home.config import LIGHT_INTENSITY_LOW

def morning_plan(home):
    # Get necessary actuators
    curtains = get_all_actuators(home, "Curtain")
    coffee_machines = get_all_actuators(home, "CoffeeMachine")
    lights = get_all_actuators(home, "Light")
    
    # Get necessary sensors
    light_sensors = get_all_sensors(home, "LightIntensive")
    
    # Perform actions for the morning plan
    for curtain in curtains:
        curtain.turn_on()
    
    for coffee_machine in coffee_machines:
        coffee_machine.turn_on()
        coffee_machine.make_coffee("espresso")
    
    for light_sensor in light_sensors:
        light_reading = light_sensor.get_reading()
        if light_reading and light_reading < LIGHT_INTENSITY_LOW:
            for light in lights:
                light.turn_on()
                light.set_brightness_level("medium")

def leave_home_plan(home):
    # Get necessary actuators
    doors = get_all_actuators(home, "Door")
    lights = get_all_actuators(home, "Light")
    sockets = get_all_actuators(home, "SmartSocket")
    
    # Perform actions for leave home plan
    for door in doors:
        door.lock()
    
    for light in lights:
        light.turn_off()
    
    for socket in sockets:
        socket.turn_off()

def movie_plan(home):
    # Get necessary actuators
    curtains = get_all_actuators(home, "Curtain")
    lights = get_all_actuators(home, "Light")
    tvs = get_all_actuators(home, "SmartTV")
    
    # Perform actions for the movie plan
    for curtain in curtains:
        curtain.turn_off()
    
    for light in lights:
        light.turn_on()
        light.set_brightness_level("low")
    
    for tv in tvs:
        tv.turn_on()
        tv.play_channel("Movie")

def main():
    home = home_plan()
    
    print("Executing Morning Plan...")
    morning_plan(home)
    
    print("Executing Leave Home Plan...")
    leave_home_plan(home)
    
    print("Executing Movie Plan...")
    movie_plan(home)

if __name__ == "__main__":
    main()