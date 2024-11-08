# Here's the `function.py` file that you requested. It implements the three plans described: MORNING PLAN, LEAVE HOME PLAN, and MOVIE PLAN.

# function.py

from home.sensor import LightIntensiveSensor
from home.actuator import Curtain, Light, MusicPlayer, CoffeeMachine, Door, SmartSocket, SmartTV
from home.home_plan import home_plan, get_room, get_all_sensors, get_all_actuators
from home.config import LIGHT_INTENSITY_HIGH

def morning_plan(home):
    light_sensors = get_all_sensors(home, "LightIntensive")
    for sensor in light_sensors:
        sensor.turn_on()
        if sensor.get_reading() >= LIGHT_INTENSITY_HIGH:
            bedroom = get_room(home, "Bedroom")
            for actuator in bedroom.actuators:
                if isinstance(actuator, Curtain):
                    actuator.turn_on()
                elif isinstance(actuator, Light):
                    actuator.turn_off()
                elif isinstance(actuator, CoffeeMachine):
                    actuator.turn_on()
                    actuator.make_coffee("Espresso")
                elif isinstance(actuator, MusicPlayer):
                    actuator.turn_on()
                    actuator.play_music("Morning Playlist")

def leave_home_plan(home):
    door = get_all_actuators(home, "Door")[0]
    door.lock()
    
    curtains = get_all_actuators(home, "Curtain")
    for curtain in curtains:
        curtain.turn_off()
        
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_off()
        
    sockets = get_all_actuators(home, "SmartSocket")
    for socket in sockets:
        socket.turn_off()

def movie_plan(home):
    smart_tv = get_all_actuators(home, "SmartTV")[0]
    smart_tv.turn_on()
    
    curtains = get_all_actuators(home, "Curtain")
    for curtain in curtains:
        curtain.turn_off()
        
    lights = get_all_actuators(home, "Light")
    for light in lights:
        if light.status == "on":
            light.set_brightness_level("low")

if __name__ == "__main__":
    home = home_plan()
    
    # Execute the plans as needed
    morning_plan(home)
    leave_home_plan(home)
    movie_plan(home)