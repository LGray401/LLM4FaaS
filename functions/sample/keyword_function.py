import concurrent.futures

from home.actuator import AC, Light, SmartTV, SmartSocket, CoffeeMachine, Curtain, MusicPlayer
from home.home_plan import home_plan, get_room_actuators, print_home_plan, get_room_sensors, get_all_actuators
from datetime import datetime
from home.sensor import LightIntensiveSensor

import time

# todo:
#   1. get the whloe room plan
#   2. keyword is related to (one) specific rooms.
#       morning & night -> mainly bedroom
#       back & home & movie -> mainly living room
#   3. use the sensor readings in that room to trigger actuators in that room.

MORNING = "07:00"
NIGHT = "23:00"


def scheduler(keyword):  # use time or keyword
    if keyword == MORNING or keyword.lower() == "morning":
        morning_plan()
    elif keyword == NIGHT or keyword.lower() == "night":
        night_plan()
    elif keyword.lower() == "leave":
        leave_home_plan()
    elif keyword.lower() == "back":
        back_home_plan()
    elif keyword.lower() == "movie":
        movie_plan()
    else:
        print("Invalid keyword. No Plan is Found.")


def morning_plan():
    print("---------------------------Morning Plan---------------------------")
    # bedroom: turn on lights, open curtain
    # current_light_intensive = 1000 # a fake reading that do not need light

    bedroom_actuators = get_room_actuators(rooms_at_home, "Bedroom")
    bedroom_sensors = get_room_sensors(rooms_at_home, "Bedroom")
    kitchen_actuators = get_room_actuators(rooms_at_home, "Kitchen")

    for sensor in bedroom_sensors:
        if isinstance(sensor, LightIntensiveSensor):
            sensor.turn_on()
            current_light_intensive = sensor.get_reading()
            # print(f"Bedroom's Light Intensive is {current_light_intensive} lux")

    # Bedroom Actuators: lights, curtain, music_player
    for actor in bedroom_actuators:
        if isinstance(actor, Curtain):
            actor.turn_on()
        elif isinstance(actor, Light) and current_light_intensive < 100:
            print("To dark in the Bedroom")
            actor.turn_on()
        elif isinstance(actor, MusicPlayer):
            actor.music_player('Daily News')

    # Kitchen Actuator: coffee machine
    for actor in kitchen_actuators:
        if isinstance(actor, CoffeeMachine):
            print("----Morning Coffee Time----")
            actor.turn_on()


def night_plan():
    print("---------------------------Night Plan---------------------------")
    bedroom_actuators = get_room_actuators(rooms_at_home, "Bedroom")

    # Bedroom Actuators: lights, curtain, music_player
    for actor in bedroom_actuators:
        if isinstance(actor, Curtain):
            actor.turn_off()
        elif isinstance(actor, Light):
            print("Set Bedroom Light to Sleep Mode")
            bedroom_light = actor
            bedroom_light.turn_on()
            bedroom_light.set_brightness_level("low")
        elif isinstance(actor, MusicPlayer):
            bedroom_player = actor
            bedroom_player.music_player('Bed Time Music')

    time.sleep(3)
    print(f"\n----------After 3 seconds----------")
    bedroom_light.turn_off()
    bedroom_player.turn_off()


def back_home_plan():
    print("---------------------------Back Home Plan---------------------------")
    living_room_actuators = get_room_actuators(rooms_at_home, "LivingRoom")

    for actuator in living_room_actuators:
        if isinstance(actuator, Light):
            actuator.turn_on()
        elif isinstance(actuator, Curtain):
            actuator.turn_off()

    get_all_actuators(rooms_at_home, "SmartSocket")


# todo: start 'comfort home' 5-min before arrival,
#  i.e., start the function when back-plan is triggered,
#        trigger actuators after 5-min


def leave_home_plan():
    print("---------------------------Leave Home Plan---------------------------")
    all_lights = get_all_actuators(rooms_at_home, "Light")
    all_sockets = get_all_actuators(rooms_at_home, "SmartSocket")
    all_windows = get_all_actuators(rooms_at_home, "Window")
    all_doors = get_all_actuators(rooms_at_home, "Door")
    all_robots = get_all_actuators(rooms_at_home, "CleaningRobot")

    if all_lights is not None:
        for light in all_lights:
            light.turn_off()

    if all_sockets is not None:
        for socket in all_sockets:
            if not socket.room_name == "Kitchen":
                # print(socket.id)
                socket.turn_off()

    if all_windows is not None:
        for window in all_windows:
            window.turn_off()

    if all_doors is not None:
        for door in all_doors:
            if door.room_name == "Outdoor":
                door.turn_off()

    if all_robots is not None:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(run_daily_routine, all_robots)
    # print(f"Cleaning Robots: {all_robots}")
    # if all_robots is not None:# first robot will block for loop
    #     for robot in all_robots:
    #         robot.daily_routine()


def movie_plan():
    print("---------------------------Movie Plan---------------------------")
    living_room_actuators = get_room_actuators(rooms_at_home, "LivingRoom")
    # todo: turn off all lights except the one(s) in living room?
    for actuator in living_room_actuators:
        if actuator.actuator_type == "Light":
            actuator.turn_on()
            actuator.set_brightness_level("medium")
        elif actuator.actuator_type == "SmartTV":
            actuator.turn_on()
        elif actuator.actuator_type == "Curtain":
            actuator.turn_off()


def run_daily_routine(robot):
    robot.daily_routine()


# test scheduler
if __name__ == "__main__":
    # current home plan
    rooms_at_home = home_plan()  # return rooms
    # Time
    current_time = datetime.now().strftime("%H:%M")
    print(f"current time is {current_time}")

    scheduler("movie")
