# Based on the given functional description and provided source code, here’s how the `function.py` file could be structured to fulfill the MORNING PLAN, LEAVE HOME PLAN, and MOVIE PLAN functionalities:
# 
# ### functions/function.py

import time
from home.sensor import LightIntensiveSensor
from home.actuator import Light, Curtain, CoffeeMachine, MusicPlayer, Door, SmartSocket
from home.home_plan import home_plan, get_room, get_all_sensors

def morning_plan(home):
    print("Executing Morning Plan...")
    living_room = get_room(home, "LivingRoom")
    kitchen = get_room(home, "Kitchen")
    
    # 拉开窗帘
    for actuator in living_room.actuators:
        if isinstance(actuator, Curtain):
            actuator.turn_on()

    # Check the outdoor light intensity to decide whether to turn on the light
    outdoor_light_sensor = get_all_sensors(home, "LightIntensive")
    if outdoor_light_sensor:
        outdoor_light_sensor[0].turn_on()
        light_reading = outdoor_light_sensor[0].get_reading()
        if light_reading < 900:  # 阴天的话开灯
            for actuator in living_room.actuators:
                if isinstance(actuator, Light):
                    actuator.turn_on()

    # 做咖啡
    for actuator in kitchen.actuators:
        if isinstance(actuator, CoffeeMachine):
            actuator.turn_on()
            actuator.make_coffee("Americano")

    # 放音乐
    time.sleep(2)  # Assuming coffee is made in 2 seconds for simplicity
    for actuator in living_room.actuators:
        if isinstance(actuator, MusicPlayer):
            actuator.turn_on()
            actuator.play_music("Morning Playlist")

def leave_home_plan(home):
    print("Executing Leave Home Plan...")
    # 晴天的话拉开窗帘，关闭灯，插座，锁门
    living_room = get_room(home, "LivingRoom")
    outdoor_light_sensor = get_all_sensors(home, "LightIntensive")
    if outdoor_light_sensor:
        outdoor_light_sensor[0].turn_on()
        light_reading = outdoor_light_sensor[0].get_reading()
        if light_reading >= 900:  # 晴天
            for actuator in living_room.actuators:
                if isinstance(actuator, Curtain):
                    actuator.turn_on()

    # 关闭灯，插座
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, Light) or isinstance(actuator, SmartSocket):
                actuator.turn_off()

    # 锁门
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, Door):
                actuator.lock()

def movie_plan(home):
    print("Executing Movie Plan...")
    living_room = get_room(home, "LivingRoom")
    
    # 合上窗帘，关灯
    for actuator in living_room.actuators:
        if isinstance(actuator, Curtain) or isinstance(actuator, Light):
            actuator.turn_off()

def main():
    home = home_plan()
    morning_plan(home)
    time.sleep(2)  # Wait for 2 seconds before executing the next plan
    leave_home_plan(home)
    time.sleep(2)  # Wait for 2 seconds before executing the next plan
    movie_plan(home)

if __name__ == "__main__":
    main()