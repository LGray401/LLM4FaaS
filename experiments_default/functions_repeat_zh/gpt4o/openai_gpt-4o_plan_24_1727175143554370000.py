# Based on your functional description and the provided source code files, here is the `function.py` file located in the `functions` folder. This file defines the main functions for the smart home project, which includes the `morning_plan`, `leave_home_plan`, and `movie_plan`.
# 
# ### functions/function.py

from home.sensor import LightIntensiveSensor, OutdoorTemperatureSensor
from home.actuator import Curtain, Light, CoffeeMachine, MusicPlayer, Door, SmartSocket, Window
from home.home_plan import home_plan, get_all_actuators, get_all_sensors

def morning_plan(home):
    # 拉开窗帘
    curtains = get_all_actuators(home, "Curtain")
    for curtain in curtains:
        curtain.turn_on()

    # 阴天的话开灯
    outdoor_light_sensors = get_all_sensors(home, "LightIntensive")
    is_cloudy = all(sensor.get_reading() < 900 for sensor in outdoor_light_sensors)
    if is_cloudy:
        lights = get_all_actuators(home, "Light")
        for light in lights:
            light.turn_on()

    # 做咖啡
    coffee_machines = get_all_actuators(home, "CoffeeMachine")
    for coffee_machine in coffee_machines:
        coffee_machine.turn_on()
        coffee_machine.make_coffee("Espresso")

    # 咖啡做好了放音乐
    music_players = get_all_actuators(home, "MusicPlayer")
    for music_player in music_players:
        music_player.turn_on()
        music_player.play_music("Morning Playlist")


def leave_home_plan(home):
    # 晴天的话拉开窗帘
    outdoor_temp_sensors = get_all_sensors(home, "OutdoorTemperature")
    is_sunny = all(sensor.get_reading() > 10 for sensor in outdoor_temp_sensors)
    if is_sunny:
        curtains = get_all_actuators(home, "Curtain")
        for curtain in curtains:
            curtain.turn_on()

    # 关闭灯
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_off()

    # 关闭插座
    sockets = get_all_actuators(home, "SmartSocket")
    for socket in sockets:
        socket.turn_off()

    # 锁门
    doors = get_all_actuators(home, "Door")
    for door in doors:
        door.lock()


def movie_plan(home):
    # 合上窗帘
    curtains = get_all_actuators(home, "Curtain")
    for curtain in curtains:
        curtain.turn_off()

    # 关灯
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_off()


def main():
    home = home_plan()
    
    # Call the required plans
    print("Executing Morning Plan:")
    morning_plan(home)
    
    print("\nExecuting Leave Home Plan:")
    leave_home_plan(home)
    
    print("\nExecuting Movie Plan:")
    movie_plan(home)


if __name__ == "__main__":
    main()