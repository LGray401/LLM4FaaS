# # function.py

from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, \
    OutdoorTemperatureSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, \
    SmartSocket, Door, CleaningRobot, SmartTV
from home_plan import home_plan, get_room, get_room_sensors, get_room_actuators
from home.logger_config import logger
import time

def main():
    home = home_plan()

    # Morning Plan
    logger.info("Starting Morning Plan...")
    room = get_room(home, "LivingRoom")
    if room:
        light = get_room_actuators(room, "Light")[0]
        if light:
            light.turn_on()
            time.sleep(2)  # Wait for the light to turn on
            light.turn_off()
        tv = get_room_actuators(room, "SmartTV")[0]
        if tv:
            tv.play_channel("News")
            time.sleep(10)  # Wait for the TV to start playing
            tv.play_channel("None")  # Turn off the TV
    logger.info("Morning Plan completed.")

    # Leave Home Plan
    logger.info("Starting Leave Home Plan...")
    room = get_room(home, "LivingRoom")
    if room:
        door = get_room_actuators(room, "Door")[0]
        if door:
            door.unlock()
            time.sleep(1)  # Wait for the door to unlock
            door.lock()
        light = get_room_actuators(room, "Light")[0]
        if light:
            light.turn_off()
    logger.info("Leave Home Plan completed.")

    # Movie Plan
    logger.info("Starting Movie Plan...")
    room = get_room(home, "LivingRoom")
    if room:
        tv = get_room_actuators(room, "SmartTV")[0]
        if tv:
            tv.play_channel("Movie")
            time.sleep(10)  # Wait for the TV to start playing
            tv.play_channel("None")  # Turn off the TV
        light = get_room_actuators(room, "Light")[0]
        if light:
            light.turn_off()
    logger.info("Movie Plan completed.")

if __name__ == "__main__":
    main()