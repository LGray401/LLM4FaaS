# Given your functional description in Chinese, "请帮我调整（开、关、调亮、调暗）某某设备。" which translates to "Please help me adjust (turn on, turn off, brighten, dim) a certain device.", I will create the `function.py` file to handle these operations.
# 
# Here's the `function.py` file:
# 
# ### `functions/function.py`

from home.home_plan import home_plan, get_room_actuators
from home.actuator import Light

def main():
    home = home_plan()
    room_name = input("请输入房间名称: ")
    device_type = input("请输入设备类型（例如，Light）: ")
    operation = input("请输入操作类型（开, 关, 调亮, 调暗）: ")

    actuators = get_room_actuators(home, room_name)
    if actuators is None:
        print(f"房间 {room_name} 没有找到设备。")
        return

    target_actuator = None
    for actuator in actuators:
        if actuator.actuator_type == device_type:
            target_actuator = actuator
            break

    if target_actuator is None:
        print(f"房间 {room_name} 没有找到类型为 {device_type} 的设备。")
        return

    if operation == "开":
        target_actuator.turn_on()
    elif operation == "关":
        target_actuator.turn_off()
    elif operation == "调亮":
        if isinstance(target_actuator, Light):
            target_actuator.turn_on()
            target_actuator.set_brightness_level("high")
        else:
            print(f"{device_type} 不支持调亮操作。")
    elif operation == "调暗":
        if isinstance(target_actuator, Light):
            target_actuator.turn_on()
            target_actuator.set_brightness_level("low")
        else:
            print(f"{device_type} 不支持调暗操作。")
    else:
        print("无效的操作类型。")

if __name__ == "__main__":
    main()