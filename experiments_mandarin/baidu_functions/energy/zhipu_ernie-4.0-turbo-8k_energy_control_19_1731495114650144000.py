# 基于你的功能描述和提供的代码，我将为你的智能家居项目编写一个`function.py`文件，该文件将包含主要的控制逻辑，特别是关于节能模式的自动化决策和外部环境检测。以下是`function.py`的代码：

import random
from home.sensor import Sensor, IndoorTemperatureSensor, OutdoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Actuator, Window, AC, Heater, NotificationSender
from home.home_plan import home_plan, get_room, get_room_sensors, get_all_sensors
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger


def check_outdoor_weather(rooms):
    outdoor_sensors = get_all_sensors(rooms, "OutdoorTemperature")
    if outdoor_sensors:
        outdoor_temp = outdoor_sensors[0].get_reading()  # 假设只有一个室外温度传感器
        if outdoor_temp is not None:
            return outdoor_temp
    return None


def automate_based_on_weather(rooms):
    outdoor_temp = check_outdoor_weather(rooms)
    if outdoor_temp is not None:
        for room in rooms:
            indoor_temp_sensors = [s for s in room.sensors if s.sensor_type == "IndoorTemperature"]
            windows = [a for a in room.actuators if a.actuator_type == "Window"]
            acs = [a for a in room.actuators if a.actuator_type == "AC"]
            heaters = [a for a in room.actuators if a.actuator_type == "Heater"]

            if indoor_temp_sensors and windows:
                indoor_temp = indoor_temp_sensors[0].get_reading()  # 假设每个房间只有一个室内温度传感器
                if indoor_temp is not None:
                    # 根据室外温度自动调节窗户
                    if outdoor_temp < TEMP_LOW and any(w.status == "off" for w in windows):
                        ask_user_and_act(room, "It's cold outside. Would you like to close the windows?", windows, "close")
                    elif outdoor_temp > TEMP_HIGH and any(w.status == "on" for w in windows):
                        ask_user_and_act(room, "It's hot outside. Would you like to open the windows?", windows, "open")

                    # 自动调节空调或暖气
                    if acs and outdoor_temp > TEMP_HIGH and indoor_temp > TEMP_HIGH:
                        turn_on_ac_if_needed(acs, indoor_temp)
                    elif heaters and outdoor_temp < TEMP_LOW and indoor_temp < TEMP_LOW:
                        turn_on_heater_if_needed(heaters, indoor_temp)


def turn_on_ac_if_needed(acs, indoor_temp):
    for ac in acs:
        if ac.status == "off":
            ac.turn_on()
            ac.set_target_temperature(TEMP_HIGH - 2)  # 设定为稍低于高温阈值的温度
            logger.info(f"Turned on AC in {ac.room_name} due to high indoor temperature ({indoor_temp}°C).")


def turn_on_heater_if_needed(heaters, indoor_temp):
    for heater in heaters:
        if heater.status == "off":
            heater.turn_on()
            heater.set_target_temperature(TEMP_LOW + 2)  # 设定为稍高于低温阈值的温度
            logger.info(f"Turned on heater in {heater.room_name} due to low indoor temperature ({indoor_temp}°C).")


def ask_user_and_act(room, message, devices, action):
    user_response = input(message + " (yes/no): ").strip().lower()
    if user_response == "yes":
        for device in devices:
            if action == "close" and device.actuator_type == "Window" and device.status == "on":
                device.turn_off()
            elif action == "open" and device.actuator_type == "Window" and device.status == "off":
                device.turn_on()
            # 可以根据需要添加更多设备类型和动作
        logger.info(f"User agreed to {action} the {devices[0].actuator_type} in {room.name}.")
    else:
        logger.info(f"User declined to {action} the {devices[0].actuator_type} in {room.name}.")


def energy_saving_mode(rooms):
    # 检查是否有窗户和空调同时开启的情况
    for room in rooms:
        windows = [a for a in room.actuators if a.actuator_type == "Window" and a.status == "on"]
        acs = [a for a in room.actuators if a.actuator_type == "AC" and a.status == "on"]
        heaters = [a for a in room.actuators if a.actuator_type == "Heater" and a.status == "on"]

        if windows and (acs or heaters):
            ask_user_and_act(room, "Windows are open while AC/Heater is on. Would you like to turn off the AC/Heater?", acs + heaters, "turn_off")


def main():
    rooms = home_plan()
    automate_based_on_weather(rooms)
    energy_saving_mode(rooms)


if __name__ == "__main__":
    main()