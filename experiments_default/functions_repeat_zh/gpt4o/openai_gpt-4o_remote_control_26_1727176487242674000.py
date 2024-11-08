# Great! Based on your functional description and the source code provided, here is a `function.py` file for your smart home project. This file will be placed in the `functions` folder and contains a main function that adjusts various devices (turn on, turn off, brighten, dim) based on the provided commands.

# functions/function.py

from home.home_plan import home_plan, get_room_actuators
from home.actuator import Light, Heater, AC, Humidifier

def adjust_device(room_name, device_type, action, level=None):
    home = home_plan()
    actuators = get_room_actuators(home, room_name)
    
    if not actuators:
        print(f"No actuators found in room: {room_name}")
        return
    
    for actuator in actuators:
        if actuator.actuator_type.lower() == device_type.lower():
            if action == "开":
                actuator.turn_on()
            elif action == "关":
                actuator.turn_off()
            elif action == "调亮" and isinstance(actuator, Light):
                if level:
                    actuator.set_brightness_level(level)
                else:
                    print(f"Brightness level not provided for {device_type} in {room_name}")
            elif action == "调暗" and isinstance(actuator, Light):
                if level:
                    actuator.set_brightness_level(level)
                else:
                    print(f"Brightness level not provided for {device_type} in {room_name}")
            elif action == "调亮" and isinstance(actuator, Heater):
                if level:
                    actuator.set_target_temperature(level)
                else:
                    print(f"Target temperature not provided for {device_type} in {room_name}")
            elif action == "调暗" and isinstance(actuator, AC):
                if level:
                    actuator.set_target_temperature(level)
                else:
                    print(f"Target temperature not provided for {device_type} in {room_name}")
            elif action == "调亮" and isinstance(actuator, Humidifier):
                actuator.increase_humidity()
            elif action == "调暗" and isinstance(actuator, Humidifier):
                actuator.decrease_humidity()
            else:
                print(f"Action '{action}' not supported for {device_type} in {room_name}")
            break
    else:
        print(f"No matching device found for {device_type} in {room_name}")

if __name__ == "__main__":
    # Example usage
    adjust_device("LivingRoom", "Light", "开")
    adjust_device("LivingRoom", "Light", "调亮", "high")
    adjust_device("LivingRoom", "Heater", "调亮", 22)
    adjust_device("LivingRoom", "AC", "调暗", 18)
    adjust_device("LivingRoom", "Humidifier", "调亮")
    adjust_device("LivingRoom", "Humidifier", "调暗")