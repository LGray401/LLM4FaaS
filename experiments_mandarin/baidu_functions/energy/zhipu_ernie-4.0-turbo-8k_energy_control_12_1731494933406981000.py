# 基于您提供的功能描述和源代码，我将为您的智能家居项目创建一个`function.py`文件，该文件将包含启动节能模式的主函数。节能模式将根据室外温湿度自主决定是否启用空调。
# 
# ### function.py

from home.home_plan import home_plan, get_room_sensors, get_all_actuators
from home.sensor import OutdoorTemperatureSensor, HumiditySensor
from home.actuator import AC
from home.config import TEMP_HIGH, TEMP_LOW, HUMIDITY_HIGH, HUMIDITY_LOW

def energy_saving_mode(home):
    # 获取室外温湿度传感器
    outdoor_temp_sensors = get_all_sensors(home, "OutdoorTemperature")
    outdoor_humidity_sensors = get_all_sensors(home, "Humidity")  # 假设室外也有湿度传感器
    
    # 如果没有找到室外温湿度传感器，则退出函数
    if not outdoor_temp_sensors or not outdoor_humidity_sensors:
        print("未能找到室外温湿度传感器，节能模式无法启动。")
        return
    
    # 获取所有空调设备
    acs = get_all_actuators(home, "AC")
    
    # 如果没有找到空调设备，则退出函数
    if not acs:
        print("未能找到空调设备，节能模式无法控制空调。")
        return
    
    # 遍历室外温湿度传感器，获取读数
    for temp_sensor in outdoor_temp_sensors:
        temp_sensor.turn_on()  # 打开传感器以获取读数
        temp_reading = temp_sensor.get_reading()
        temp_sensor.turn_off()  # 获取读数后关闭传感器以节省能源
        
        for humidity_sensor in outdoor_humidity_sensors:
            humidity_sensor.turn_on()  # 打开传感器以获取读数
            humidity_reading = humidity_sensor.get_reading()
            humidity_sensor.turn_off()  # 获取读数后关闭传感器以节省能源
            
            # 根据温湿度决定是否启用空调
            if temp_reading > TEMP_HIGH or humidity_reading > HUMIDITY_HIGH:
                # 如果温度过高或湿度过高，则打开空调
                for ac in acs:
                    if ac.status == "off":
                        ac.turn_on()
                        ac.set_target_temperature(TEMP_HIGH)  # 设置目标温度为较高值以节能
                    ac.adjust_temperature(temp_reading)  # 根据当前温度调整空调状态
            else:
                # 如果温度过低或湿度过低，则关闭空调
                for ac in acs:
                    if ac.status == "on":
                        ac.turn_off()
            
            # 假设只需要一个室外温湿度传感器的读数即可决定所有空调的状态
            break  # 跳出内层循环
        
        # 假设只需要一组温湿度读数即可决定空调状态，因此外层循环也可以跳出
        break  # 跳出外层循环

# 主函数
def main():
    # 创建家居计划
    home = home_plan()
    
    # 启动节能模式
    energy_saving_mode(home)

if __name__ == "__main__":
    main()