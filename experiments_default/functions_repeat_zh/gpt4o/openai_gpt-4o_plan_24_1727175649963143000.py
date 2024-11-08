# Certainly! Given your functional description and the provided source code, I will create a `function.py` file to implement the morning, leave home, and movie plans. Here it is:
# 
# ## function.py

from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import LIGHT_INTENSITY_HIGH
from home.sensor import LightIntensiveSensor
from home.actuator import Light, Curtain, CoffeeMachine, MusicPlayer, Door, SmartSocket, Window

def morning_plan(home):
    print("Executing Morning Plan...")

    # 拉开窗帘
    curtains = get_all_actuators(home, "Curtain")
    for curtain in curtains:
        curtain.turn_on()

    # 阴天的话开灯
    outdoor_light_sensors = get_all_sensors(home, "LightIntensive")
    for sensor in outdoor_light_sensors:
        sensor.turn_on()
        light_intensity = sensor.get_reading()
        if light_intensity < LIGHT_INTENSITY_HIGH:
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
    print("Executing Leave Home Plan...")

    # 晴天的话拉开窗帘
    outdoor_light_sensors = get_all_sensors(home, "LightIntensive")
    for sensor in outdoor_light_sensors:
        sensor.turn_on()
        light_intensity = sensor.get_reading()
        if light_intensity >= LIGHT_INTENSITY_HIGH:
            curtains = get_all_actuators(home, "Curtain")
            for curtain in curtains:
                curtain.turn_on()

    # 关闭灯，插座，锁门
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_off()

    sockets = get_all_actuators(home, "SmartSocket")
    for socket in sockets:
        socket.turn_off()

    doors = get_all_actuators(home, "Door")
    for door in doors:
        door.lock()


def movie_plan(home):
    print("Executing Movie Plan...")

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
    
    # Execute plans
    morning_plan(home)
    leave_home_plan(home)
    movie_plan(home)


if __name__ == "__main__":
    main()