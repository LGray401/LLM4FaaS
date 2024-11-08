# Certainly! Based on the functional description and source code provided, I'll create `function.py` which will include the main function to execute the described smart home actions.
# 
# ## function.py

import time
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, OutdoorTemperatureSensor
from home.actuator import Light, MusicPlayer, CoffeeMachine, AC, Curtain, CleaningRobot
from home.home_plan import home_plan, get_room, get_all_actuators

def main():
    home = home_plan()

    # Greeting
    print("ChatGPT: 下班了主人，您累一天了，有什么事情尽管吩咐我吧！")

    # Fetch each room
    living_room = get_room(home, "LivingRoom")
    kitchen = get_room(home, "Kitchen")
    bedroom = get_room(home, "Bedroom")

    # 1. 打开灯，调成中等光
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_on()
        light.set_brightness_level("medium")

    # 2. 播放一首可以缓解压力的歌曲
    music_players = get_all_actuators(home, "MusicPlayer")
    for music_player in music_players:
        music_player.turn_on()
        music_player.play_music("Relaxing Playlist")

    # 3. 煮一杯咖啡
    coffee_machines = get_all_actuators(home, "CoffeeMachine")
    for coffee_machine in coffee_machines:
        coffee_machine.turn_on()
        coffee_machine.make_coffee("Espresso")

    # 4. 打开空调调制22°
    ac_units = get_all_actuators(home, "AC")
    for ac in ac_units:
        ac.turn_on()
        ac.set_target_temperature(22)

    # 5. 关闭窗帘
    curtains = get_all_actuators(home, "Curtain")
    for curtain in curtains:
        curtain.turn_on()

    # 6. 让扫地机器人开始工作
    cleaning_robots = get_all_actuators(home, "CleaningRobot")
    for robot in cleaning_robots:
        robot.turn_on()
        robot.daily_routine()

if __name__ == "__main__":
    main()