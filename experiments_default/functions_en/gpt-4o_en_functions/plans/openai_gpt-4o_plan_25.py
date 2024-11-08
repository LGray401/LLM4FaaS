# I'll create a `function.py` file that contains the main function to implement the three plans (Morning, Leave Home, and Movie). This main function will use the classes and methods defined in your existing source code files.
# 
# Here's the `function.py` file:

from home.sensor import LightIntensiveSensor
from home.actuator import Curtain, Light, MusicPlayer, CoffeeMachine, Door, SmartTV
from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators
from home.config import LIGHT_INTENSITY_HIGH

def morning_plan(home):
    print("Executing Morning Plan...")
    bedroom = get_room(home, "Bedroom")
    light_sensor = next((s for s in bedroom.sensors if isinstance(s, LightIntensiveSensor)), None)
    if light_sensor:
        light_sensor.turn_on()
        light_intensity = light_sensor.get_reading()
        if light_intensity and light_intensity >= LIGHT_INTENSITY_HIGH:
            print("Light intensity is high enough, executing morning actions...")
            for actuator in bedroom.actuators:
                if isinstance(actuator, Curtain):
                    actuator.turn_on()
                elif isinstance(actuator, Light):
                    actuator.turn_off()
                elif isinstance(actuator, MusicPlayer):
                    actuator.turn_on()
                    actuator.play_music("Morning Playlist")
                elif isinstance(actuator, CoffeeMachine):
                    actuator.turn_on()
                    actuator.make_coffee("Espresso")
    else:
        print("No light sensor found in the bedroom.")

def leave_home_plan(home):
    print("Executing Leave Home Plan...")
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, Door):
                actuator.lock()
            elif isinstance(actuator, Curtain):
                actuator.turn_off()
            elif isinstance(actuator, Light):
                actuator.turn_off()
            elif isinstance(actuator, SmartSocket):
                actuator.turn_off()

def movie_plan(home):
    print("Executing Movie Plan...")
    living_room = get_room(home, "LivingRoom")
    tv = next((a for a in living_room.actuators if isinstance(a, SmartTV)), None)
    if tv:
        tv.turn_on()
        tv.play_channel("Movie Channel")
        for actuator in living_room.actuators:
            if isinstance(actuator, Curtain):
                actuator.turn_on()
            elif isinstance(actuator, Light):
                actuator.turn_on()
                actuator.set_brightness_level("low")
    else:
        print("No SmartTV found in the living room.")

def main():
    home = home_plan()
    morning_plan(home)
    leave_home_plan(home)
    movie_plan(home)

if __name__ == "__main__":
    main()