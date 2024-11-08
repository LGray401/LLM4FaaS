# Here is the 'function.py' file based on the given functional description:

from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators
from home.sensor import LightIntensiveSensor
from home.actuator import Window, Curtain, MusicPlayer, CoffeeMachine, Door, SmartTV, Light

def morning_plan():
    home = home_plan()
    living_room = get_room(home, "LivingRoom")
    bedroom = get_room(home, "Bedroom")

    light_sensor = get_room_sensors(home, "LivingRoom")[0]  # assumes the light sensor is the first sensor in the room
    light_reading = light_sensor.get_reading()

    curtain = get_room_actuators(home, "LivingRoom")[2]  # assumes the curtain is the third actuator in the room
    curtain_status = curtain.get_status()

    bedroom_light = get_room_actuators(home, "Bedroom")[0]  # assumes the bedroom light is the first actuator in the room

    music_player = get_room_actuators(home, "LivingRoom")[5]  # assumes the music player is the fifth actuator in the room
    coffee_machine = get_room_actuators(home, "Kitchen")[4]  # assumes the coffee machine is the fifth actuator in the room

    if light_reading >= LightIntensiveSensor.LIGHT_INTENSITY_HIGH:
        curtain.turn_on()
        bedroom_light.turn_off()
        music_player.turn_on()
        music_player.play_music("morning playlist")
        coffee_machine.turn_on()
        coffee_machine.make_coffee("black")

    return None


def leave_home_plan():
    home = home_plan()
    outdoor_light_sensor = get_all_sensors(home, "LightIntensive")[0]  # assumes there is only one outdoor light sensor
    outdoor_light_reading = outdoor_light_sensor.get_reading()

    door = get_room_actuators(home, "LivingRoom")[8]  # assumes the door is the ninth actuator in the room
    curtain = get_room_actuators(home, "LivingRoom")[2]  # assumes the curtain is the third actuator in the room
    living_room_lights = get_room_actuators(home, "LivingRoom")[1::]  # assumes the lights are the second, third, ..., actuators in the room
    living_room_sockets = get_room_actuators(home, "LivingRoom")[6::]  # assumes the sockets are the seventh, eighth, ..., actuators in the room

    if outdoor_light_reading >= LightIntensiveSensor.LIGHT_INTENSITY_HIGH:
        curtain.turn_on()
        for light in living_room_lights:
            light.turn_off()
        for socket in living_room_sockets:
            socket.turn_off()

    door.lock()

    return None


def movie_plan():
    home = home_plan()
    tv = get_room_actuators(home, "LivingRoom")[-2]  # assumes the TV is the second to last actuator in the room
    curtain = get_room_actuators(home, "LivingRoom")[2]  # assumes the curtain is the third actuator in the room
    living_room_lights = get_room_actuators(home, "LivingRoom")[1::]  # assumes the lights are the second, third, ..., actuators in the room

    tv.turn_on()
    curtain.turn_on()
    for light in living_room_lights:
        light.set_brightness_level("low")

    return None