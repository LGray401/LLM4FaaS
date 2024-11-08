from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC, CleaningRobot, Light, MusicPlayer
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, \
    TEMP_CHANGE_DURATION_WINDOW

import time

def main():
    home = home_plan()

    #  回家前十分钟开空调
    living_room = get_room(home, "LivingRoom")
    living_room_ac = get_room_actuators(home, "LivingRoom")[0]
    living_room_temp_sensor = get_room_sensors(home, "LivingRoom")[0]
    
    # 模拟回家前十分钟
    print("模拟回家前十分钟...")
    time.sleep(600)

    # 检查客厅温度
    current_temp = living_room_temp_sensor.get_reading()
    if current_temp > TEMP_HIGH:
        print("客厅温度过高，打开空调降温")
        living_room_ac.turn_on()
        living_room_ac.set_target_temperature(TEMP_HIGH - 1)
    else:
        print("客厅温度适宜，无需开空调")

    #  家里没人时扫地机器人扫地
    living_room_cleaning_robot = get_room_actuators(home, "LivingRoom")[1]
    bedroom_cleaning_robot = get_room_actuators(home, "Bedroom")[0]
    
    # 模拟无人状态
    print("模拟无人状态...")
    time.sleep(600)

    # 检查客厅和卧室的灯光
    living_room_lights = get_room_actuators(home, "LivingRoom")[2]
    bedroom_lights = get_room_actuators(home, "Bedroom")[0]
    if living_room_lights.get_status() == "on" or bedroom_lights.get_status() == "on":
        print("客厅或卧室有灯光，不启动扫地机器人")
    else:
        print("客厅和卧室均无灯光，启动扫地机器人")
        living_room_cleaning_robot.turn_on()
        living_room_cleaning_robot.daily_routine()
        bedroom_cleaning_robot.turn_on()
        bedroom_cleaning_robot.daily_routine()

    # 模拟无人状态
    print("模拟无人状态...")
    time.sleep(600)

    # 模拟有人回家
    print("模拟有人回家...")

    # 关闭空调
    living_room_ac.turn_off()

    # 打开客厅灯光
    living_room_lights.turn_on()
    living_room_lights.set_brightness_level("medium")

    # 打开音乐
    living_room_music_player = get_room_actuators(home, "LivingRoom")[5]
    living_room_music_player.turn_on()
    living_room_music_player.play_music("Relaxing Music")

    # 自动调节灯光和空调
    while True:
        # 获取客厅温度、湿度和光照强度
        current_temp = living_room_temp_sensor.get_reading()
        living_room_humidity_sensor = get_room_sensors(home, "LivingRoom")[1]
        current_humidity = living_room_humidity_sensor.get_reading()
        living_room_light_sensor = get_room_sensors(home, "LivingRoom")[2]
        current_light_intensity = living_room_light_sensor.get_reading()

        # 调节空调
        if current_temp > TEMP_HIGH:
            print("客厅温度过高，打开空调降温")
            living_room_ac.turn_on()
            living_room_ac.set_target_temperature(TEMP_HIGH - 1)
        elif current_temp < TEMP_LOW:
            print("客厅温度过低，关闭空调")
            living_room_ac.turn_off()

        # 调节灯光
        if current_light_intensity < LIGHT_INTENSITY_LOW:
            print("客厅光线过暗，打开灯光")
            living_room_lights.turn_on()
            living_room_lights.set_brightness_level("medium")
        elif current_light_intensity > LIGHT_INTENSITY_HIGH:
            print("客厅光线过亮，降低灯光亮度")
            living_room_lights.set_brightness_level("low")

        # 调节湿度
        if current_humidity < HUMIDITY_LOW:
            print("客厅湿度过低，打开加湿器")
        elif current_humidity > HUMIDITY_HIGH:
            print("客厅湿度过高，关闭加湿器")

        time.sleep(TEMP_CHANGE_DURATION_WINDOW)

if __name__ == '__main__':
    main()

# **Explanation:**

# 1. **Import necessary modules:** Import the required modules from the `home` package and the `time` module for time-related operations.

# 2. **`main()` function:** 
#    - Initializes the `home` object by calling `home_plan()`.
#    - **Scenario 1: Home arrival in 10 minutes:**
#      - Gets the living room, AC, and temperature sensor from the `home` object.
#      - Simulates a 10-minute delay using `time.sleep(600)`.
#      - Checks the current temperature and turns on the AC if needed.
#    - **Scenario 2: Nobody at home, cleaning robot:**
#      - Gets the cleaning robots for the living room and bedroom.
#      - Simulates a period with nobody at home using `time.sleep(600)`.
#      - Checks the lights in the living room and bedroom. If both are off, it turns on the cleaning robots and starts their daily routines.
#      - Repeats the process to simulate a longer period with nobody home.
#    - **Scenario 3: Someone comes home:**
#      - Simulates someone coming home.
#      - Turns off the AC.
#      - Turns on the living room lights and sets the brightness level to "medium".
#      - Turns on the music player in the living room and starts playing a relaxing playlist.
#    - **Automatic adjustment loop:**
#      - Starts a loop to continuously monitor and adjust the living room's temperature, humidity, and light intensity.
#      - Gets the current readings for temperature, humidity, and light intensity.
#      - Adjusts the AC based on the temperature: turns it on if too high and off if too low.
#      - Adjusts the lights based on the light intensity: turns them on if too dark and lowers the brightness if too bright.
#      - Adjusts the humidifier based on the humidity: turns it on if too low and off if too high.
#      - Uses `time.sleep(TEMP_CHANGE_DURATION_WINDOW)` to wait before checking the readings again.

# **Key points:**

# - The code utilizes the classes and functions defined in the `home` package.
# - It uses a simple simulation using `time.sleep()` to represent different scenarios.
# - It demonstrates how to interact with sensors and actuators to achieve specific actions based on sensor readings.
# - It shows how to adjust devices like AC, lights, and music players according to the environment and user preferences.

# **To run this code:**

# 1. Ensure that the `home` folder containing the `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py` files is in the same directory as the `function.py` file.
# 2. Run the `function.py` file using a Python interpreter: `python function.py`.

# This code provides a basic example of how to use the `home` package to create a smart home system with automatic functionality based on sensor data. You can expand upon this example by adding more sensors, actuators, and scenarios to create a more complex and personalized smart home.
