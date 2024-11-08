from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators, print_home_plan
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, \
    SmokeSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, \
    SmartSocket, Door, CleaningRobot, SmartTV
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, \
    DAILY_ROUTINE_DURATION, TEMP_CHANGE_DURATION_WINDOW
from home.logger_config import logger
import time
from datetime import datetime
import random

# Example usage:
# from functions.function import main
# main()

def main():
    home = home_plan()
    # print_home_plan(home)

    # MORNING PLAN
    # morning_plan(home)
    # print("Morning Plan Complete")

    # LEAVE HOME PLAN
    # leave_home_plan(home)
    # print("Leave Home Plan Complete")

    # MOVIE PLAN
    movie_plan(home)
    print("Movie Plan Complete")

    # TEMP CONTROL PLAN
    # temp_control_plan(home)
    # print("Temp Control Plan Complete")

    # LIGHT CONTROL PLAN
    # light_control_plan(home)
    # print("Light Control Plan Complete")

    # HUMIDITY CONTROL PLAN
    # humidity_control_plan(home)
    # print("Humidity Control Plan Complete")

    # CLEANING ROBOT DAILY ROUTINE
    # cleaning_robot_daily_routine(home)
    # print("Cleaning Robot Daily Routine Complete")


def morning_plan(home):
    # 7点叫我起床
    notification_sender = get_all_actuators(home, "NotificationSender")[0]
    notification_sender.turn_on()
    notification_sender.notification_sender("Wake Up!")

    # 7点零五把音乐大开，播放周杰伦歌单
    music_player = get_all_actuators(home, "MusicPlayer")[0]
    music_player.turn_on()
    music_player.play_music("Jay Chou Playlist")

    # 7：20做好咖啡
    coffee_machine = get_all_actuators(home, "CoffeeMachine")[0]
    coffee_machine.turn_on()
    coffee_machine.make_coffee("Espresso")

    # wait for 20 minutes
    time.sleep(20 * 60)  # 20 minutes


def leave_home_plan(home):
    # 7：30之后我离开家后自动锁门，关闭家中灯光插座
    living_room = get_room(home, "LivingRoom")
    bedroom = get_room(home, "Bedroom")
    kitchen = get_room(home, "Kitchen")
    bathroom = get_room(home, "Bathroom")

    # Lock Door
    door = get_room_actuators(living_room, "Door")[0]
    door.lock()

    # Turn off lights
    living_room_lights = get_room_actuators(living_room, "Light")
    for light in living_room_lights:
        light.turn_off()

    bedroom_lights = get_room_actuators(bedroom, "Light")
    for light in bedroom_lights:
        light.turn_off()

    kitchen_lights = get_room_actuators(kitchen, "Light")
    for light in kitchen_lights:
        light.turn_off()

    bathroom_lights = get_room_actuators(bathroom, "Light")
    for light in bathroom_lights:
        light.turn_off()

    # Turn off Smart Sockets
    living_room_sockets = get_room_actuators(living_room, "SmartSocket")
    for socket in living_room_sockets:
        socket.turn_off()

    bedroom_sockets = get_room_actuators(bedroom, "SmartSocket")
    for socket in bedroom_sockets:
        socket.turn_off()

    kitchen_sockets = get_room_actuators(kitchen, "SmartSocket")
    for socket in kitchen_sockets:
        socket.turn_off()

    bathroom_sockets = get_room_actuators(bathroom, "SmartSocket")
    for socket in bathroom_sockets:
        socket.turn_off()


def movie_plan(home):
    # 我开始播放电影时，关闭窗帘，调暗灯光
    living_room = get_room(home, "LivingRoom")

    # 关闭窗帘
    curtains = get_room_actuators(living_room, "Curtain")
    for curtain in curtains:
        curtain.turn_on()

    # 调暗灯光
    light = get_room_actuators(living_room, "Light")[0]
    light.turn_on()
    light.set_brightness_level("low")

    # 模拟电影播放时间
    time.sleep(120 * 60)  # 2 hours


def temp_control_plan(home):
    # Get all indoor temperature sensors
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")

    # Get all heaters and ACs
    heaters = get_all_actuators(home, "Heater")
    acs = get_all_actuators(home, "AC")

    # Set target temperatures for heaters and ACs
    for heater in heaters:
        heater.set_target_temperature(22)
    for ac in acs:
        ac.set_target_temperature(25)

    while True:
        # Get current temperatures
        current_temps = []
        for sensor in indoor_temp_sensors:
            current_temps.append(sensor.get_reading())

        # Adjust heater and AC status
        for heater in heaters:
            heater.adjust_temperature(current_temps[0])
        for ac in acs:
            ac.adjust_temperature(current_temps[0])

        # Sleep for a short duration
        time.sleep(TEMP_CHANGE_DURATION_WINDOW)


def light_control_plan(home):
    # Get all light intensive sensors
    light_intensive_sensors = get_all_sensors(home, "LightIntensive")

    # Get all lights
    lights = get_all_actuators(home, "Light")

    while True:
        # Get current light intensity
        current_intensities = []
        for sensor in light_intensive_sensors:
            current_intensities.append(sensor.get_reading())

        # Adjust light status
        for light in lights:
            if current_intensities[0] < LIGHT_INTENSITY_LOW:
                light.turn_on()
                light.set_brightness_level("high")
            elif current_intensities[0] > LIGHT_INTENSITY_HIGH:
                light.turn_off()

        # Sleep for a short duration
        time.sleep(1)


def humidity_control_plan(home):
    # Get all humidity sensors
    humidity_sensors = get_all_sensors(home, "Humidity")

    # Get all humidifiers
    humidifiers = get_all_actuators(home, "Humidifier")

    while True:
        # Get current humidity
        current_humidities = []
        for sensor in humidity_sensors:
            current_humidities.append(sensor.get_reading())

        # Adjust humidifier status
        for humidifier in humidifiers:
            if current_humidities[0] < HUMIDITY_LOW:
                humidifier.increase_humidity()
            elif current_humidities[0] > HUMIDITY_HIGH:
                humidifier.decrease_humidity()

        # Sleep for a short duration
        time.sleep(1)


def cleaning_robot_daily_routine(home):
    # Get all cleaning robots
    cleaning_robots = get_all_actuators(home, "CleaningRobot")

    # Start daily routine
    for robot in cleaning_robots:
        robot.turn_on()
        robot.daily_routine()


if __name__ == "__main__":
    main()