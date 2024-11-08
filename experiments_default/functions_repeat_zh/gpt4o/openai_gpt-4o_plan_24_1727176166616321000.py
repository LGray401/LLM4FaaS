# Based on the provided functional description and source code, here is a `function.py` file that implements the main function for the smart home project. This file will be located in the `functions` folder and will contain functions to execute the different plans: MORNING PLAN, LEAVE HOME PLAN, and MOVIE PLAN.
# 
# ### `functions/function.py`

from home.home_plan import home_plan, get_room, get_all_actuators
from home.config import LIGHT_INTENSITY_HIGH
from home.sensor import LightIntensiveSensor
from home.actuator import CoffeeMachine, MusicPlayer, Light, Curtain, Door, SmartSocket, Window
import time

def morning_plan(home):
    print("Executing MORNING PLAN...")

    # 拉开窗帘
    curtains = get_all_actuators(home, "Curtain")
    for curtain in curtains:
        curtain.turn_on()

    # 阴天的话开灯
    light_sensors = get_all_sensors(home, "LightIntensive")
    is_cloudy = any(sensor.get_reading() < LIGHT_INTENSITY_HIGH for sensor in light_sensors)
    if is_cloudy:
        lights = get_all_actuators(home, "Light")
        for light in lights:
            light.turn_on()

    # 做咖啡
    coffee_machines = get_all_actuators(home, "CoffeeMachine")
    for machine in coffee_machines:
        machine.turn_on()
        machine.make_coffee("Espresso")
        time.sleep(2)  # Simulate time taken to make coffee

    # 咖啡做好了放音乐
    music_players = get_all_actuators(home, "MusicPlayer")
    for player in music_players:
        player.turn_on()
        player.play_music("Morning Playlist")

def leave_home_plan(home):
    print("Executing LEAVE HOME PLAN...")

    # 晴天的话拉开窗帘
    outdoor_temp_sensors = get_all_sensors(home, "OutdoorTemperature")
    is_sunny = any(sensor.get_reading() > 20 for sensor in outdoor_temp_sensors)  # assuming sunny if temp > 20°C
    if is_sunny:
        curtains = get_all_actuators(home, "Curtain")
        for curtain in curtains:
            curtain.turn_on()

    # 关闭灯，插座
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_off()

    sockets = get_all_actuators(home, "SmartSocket")
    for socket in sockets:
        socket.turn_off()

    # 锁门
    doors = get_all_actuators(home, "Door")
    for door in doors:
        door.lock()

def movie_plan(home):
    print("Executing MOVIE PLAN...")

    # 合上窗帘
    curtains = get_all_actuators(home, "Curtain")
    for curtain in curtains:
        curtain.turn_off()

    # 关灯
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_off()

def main():
    # Load the home plan
    home = home_plan()

    # Execute plans
    morning_plan(home)
    leave_home_plan(home)
    movie_plan(home)

if __name__ == "__main__":
    main()