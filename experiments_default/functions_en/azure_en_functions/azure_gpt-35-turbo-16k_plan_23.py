# Sure! Here is the 'function.py' file based on your functional description:

from home.sensor import LightIntensiveSensor
from home.actuator import Curtain, Light, MusicPlayer, Door

def morning_plan(rooms):
    for room in rooms:
        if room.name == "LivingRoom":
            for sensor in room.sensors:
                if isinstance(sensor, LightIntensiveSensor):
                    sensor.turn_on()
            for actuator in room.actuators:
                if isinstance(actuator, Curtain):
                    actuator.open()
                elif isinstance(actuator, Light):
                    actuator.turn_on()
                elif isinstance(actuator, MusicPlayer):
                    actuator.play_music("morning_playlist")

def leave_home_plan(rooms):
    for room in rooms:
        if room.name == "LivingRoom":
            for actuator in room.actuators:
                if isinstance(actuator, Door):
                    actuator.close()
                elif isinstance(actuator, Curtain):
                    actuator.open()
                elif isinstance(actuator, Light):
                    actuator.turn_off()

def movie_plan(rooms):
    for room in rooms:
        if room.name == "LivingRoom":
            for actuator in room.actuators:
                if isinstance(actuator, Curtain):
                    actuator.close()
                elif isinstance(actuator, Light):
                    actuator.dim()

if __name__ == "__main__":
    rooms = home_plan()
    # Execute the morning plan
    morning_plan(rooms)
    # Execute the leave home plan
    leave_home_plan(rooms)
    # Execute the movie plan
    movie_plan(rooms)