# 基于你的功能描述和提供的源代码，我将为你编写一个`function.py`文件，该文件包含一个主函数来执行打开灯、空调、暖气以及电视的操作。以下是`function.py`的实现：

from home.home_plan import home_plan, get_room, get_room_actuators
from home.actuator import Light, AC, Heater, SmartTV

def main():
    # 创建家庭计划并获取所有房间
    home = home_plan()

    # 打开客厅、卧室、浴室的灯
    rooms_to_turn_on_lights = ["LivingRoom", "Bedroom", "Bathroom"]
    for room_name in rooms_to_turn_on_lights:
        room = get_room(home, room_name)
        if room:
            actuators = get_room_actuators(home, room_name)
            for actuator in actuators:
                if isinstance(actuator, Light):
                    actuator.turn_on()

    # 打开客厅、卧室的空调
    rooms_to_turn_on_ac = ["LivingRoom", "Bedroom"]
    for room_name in rooms_to_turn_on_ac:
        room = get_room(home, room_name)
        if room:
            actuators = get_room_actuators(home, room_name)
            for actuator in actuators:
                if isinstance(actuator, AC):
                    actuator.turn_on()  # 可以根据需要设置目标温度，例如：actuator.set_target_temperature(24)

    # 打开浴室的暖气
    bathroom = get_room(home, "Bathroom")
    if bathroom:
        actuators = get_room_actuators(home, "Bathroom")
        for actuator in actuators:
            if isinstance(actuator, Heater):
                actuator.turn_on()  # 可以根据需要设置目标温度，例如：actuator.set_target_temperature(28)

    # 开启客厅电视
    living_room = get_room(home, "LivingRoom")
    if living_room:
        actuators = get_room_actuators(home, "LivingRoom")
        for actuator in actuators:
            if isinstance(actuator, SmartTV):
                actuator.turn_on()  # 可以根据需要播放特定频道，例如：actuator.play_channel("News")

if __name__ == "__main__":
    main()