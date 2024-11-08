# 基于你提供的功能描述和代码，我将为你创建一个`function.py`文件，该文件将包含一个主要的函数，用于调整（开、关、调亮、调暗）指定设备。这个函数将位于`functions`文件夹中，并能够与`home`文件夹中的其他文件交互。
# 
# 以下是`function.py`的代码：

# function.py

from home.home_plan import get_room, get_room_actuators
from home.actuator import Light

def adjust_device(home, room_name, device_type, action, *args):
    """
    调整指定房间中的设备。

    :param home: 家居计划对象，由home_plan()返回
    :param room_name: 要调整设备的房间名称
    :param device_type: 要调整的设备类型（如"Light"）
    :param action: 要执行的动作（如"on", "off", "brighten", "dim"）
    :param args: 动作所需的额外参数（如调亮或调暗时所需的亮度级别）
    """
    room = get_room(home, room_name)
    if not room:
        print(f"无法找到名为 {room_name} 的房间。")
        return

    actuators = get_room_actuators(home, room_name)
    if not actuators:
        print(f"在 {room_name} 中没有找到任何设备。")
        return

    device_found = False
    for actuator in actuators:
        if actuator.actuator_type == device_type:
            device_found = True
            if action == "on":
                actuator.turn_on()
            elif action == "off":
                actuator.turn_off()
            elif action == "brighten" and isinstance(actuator, Light) and len(args) == 1:
                actuator.set_brightness_level(args[0])
            elif action == "dim" and isinstance(actuator, Light) and len(args) == 1:
                actuator.set_brightness_level(args[0])
            else:
                print(f"设备 {device_type} 不支持动作 {action} 或参数不正确。")
            break

    if not device_found:
        print(f"在 {room_name} 中没有找到类型为 {device_type} 的设备。")

# 示例用法（这通常会在你的主程序或其他模块中调用）：
if __name__ == "__main__":
    from home.home_plan import home_plan
    home = home_plan()
    adjust_device(home, "LivingRoom", "Light", "on")
    adjust_device(home, "LivingRoom", "Light", "brighten", "high")