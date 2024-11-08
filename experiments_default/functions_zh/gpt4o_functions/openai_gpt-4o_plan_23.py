# Sure, I can provide you with a `function.py` file that includes a main function to execute the described plans. Based on your functional description, here's the `function.py` file:

# function.py
import sys
sys.path.append('../home')

from home.sensor import LightIntensiveSensor
from home.actuator import Curtain, Light, MusicPlayer, Door
from home.home_plan import home_plan, get_room_actuators

def morning_plan(home):
    print("\nExecuting Morning Plan:")
    
    light_sensors = []
    for room in home:
        for sensor in room.sensors:
            if isinstance(sensor, LightIntensiveSensor):
                light_sensors.append(sensor)
    
    if not light_sensors:
        print("No LightIntensiveSensor found in the home plan.")
        return

    # Assuming we use the first LightIntensiveSensor found
    light_sensor = light_sensors[0]
    light_sensor.turn_on()
    light_intensity = light_sensor.get_reading()
    
    if light_intensity and light_intensity > 900:
        for room in home:
            for actuator in room.actuators:
                if isinstance(actuator, Curtain):
                    actuator.turn_on()
                if isinstance(actuator, MusicPlayer):
                    actuator.turn_on()
                    actuator.play_music("Morning Playlist")
    
    light_sensor.turn_off()


def leave_home_plan(home):
    print("\nExecuting Leave Home Plan:")
    
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, Door):
                actuator.turn_off()
            if isinstance(actuator, Curtain):
                actuator.turn_on()
            if isinstance(actuator, Light):
                actuator.turn_off()


def movie_plan(home):
    print("\nExecuting Movie Plan:")
    
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, Curtain):
                actuator.turn_off()
            if isinstance(actuator, Light):
                actuator.turn_on()
                actuator.set_brightness_level("low")


def main():
    home = home_plan()
    
    morning_plan(home)
    leave_home_plan(home)
    movie_plan(home)


if __name__ == "__main__":
    main()