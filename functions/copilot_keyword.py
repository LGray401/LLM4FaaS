from home.home_plan import home_plan, get_room, get_room_actuators
from home.actuator import Light, Curtain, MusicPlayer, CoffeeMachine, Window, Door, CleaningRobot, SmartSocket, SmartTV
from home.sensor import LightIntensiveSensor
import time

def morning_routine():
    home = home_plan()
    bedroom = get_room(home, "Bedroom")
    bedroom_actuators = get_room_actuators(home, "Bedroom")
    for actuator in bedroom_actuators:
        if isinstance(actuator, Curtain):
            actuator.turn_on()
        if isinstance(actuator, Light):
            # light_intensity = LightIntensiveSensor("Bedroom").get_reading()
            # if light_intensity < 500:
            actuator.turn_on()
        if isinstance(actuator, MusicPlayer):
            actuator.play_music("daily news")
        if isinstance(actuator, CoffeeMachine):
            actuator.turn_on()

def evening_routine():
    home = home_plan()
    bedroom = get_room(home, "Bedroom")
    bedroom_actuators = get_room_actuators(home, "Bedroom")
    for actuator in bedroom_actuators:
        if isinstance(actuator, Curtain):
            actuator.turn_off()
        if isinstance(actuator, MusicPlayer):
            actuator.play_music("bedtime music")
        if isinstance(actuator, Light):
            actuator.set_brightness_level("medium")
            time.sleep(30*60)
            actuator.turn_off()

def home_plan_routine():
    home = home_plan()
    living_room_actuators = get_room_actuators(home, "LivingRoom")
    for actuator in living_room_actuators:
        if isinstance(actuator, Light):
            actuator.turn_on()
        if isinstance(actuator, Curtain):
            actuator.turn_off()
    for room in home:
        room_actuators = get_room_actuators(home, room.name)
        for actuator in room_actuators:
            if isinstance(actuator, SmartSocket):
                actuator.turn_on()

def away_plan_routine():
    home = home_plan()
    for room in home:
        room_actuators = get_room_actuators(home, room.name)
        for actuator in room_actuators:
            if isinstance(actuator, Light) or isinstance(actuator, Window):
                actuator.turn_off()
            if isinstance(actuator, Door):
                actuator.turn_on()
            if isinstance(actuator, CleaningRobot):
                actuator.daily_routine()
            if isinstance(actuator, SmartSocket) and room.name != "Kitchen":
                actuator.turn_off()

def movie_plan_routine():
    home = home_plan()
    for room in home:
        room_actuators = get_room_actuators(home, room.name)
        for actuator in room_actuators:
            if isinstance(actuator, Light):
                if room.name == "LivingRoom":
                    actuator.set_brightness_level("medium")
                else:
                    actuator.turn_off()
            if isinstance(actuator, Curtain) and room.name == "LivingRoom":
                actuator.turn_off()
            if isinstance(actuator, SmartTV) and room.name == "LivingRoom":
                actuator.turn_on()


if __name__ == '__main__':
    morning_routine()
