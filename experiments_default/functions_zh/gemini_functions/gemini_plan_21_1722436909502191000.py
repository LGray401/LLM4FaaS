from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators, print_home_plan
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, \
    OutdoorTemperatureSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, \
    SmartSocket, Door, \
    CleaningRobot, SmartTV
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, \
    TEMP_CHANGE_DURATION_WINDOW
from home.logger_config import logger

import time


def morning_plan(home):
    print(f"\n---Morning Plan---")
    # # Example invocation
    # home = home_plan()
    # # home plan
    # print_home_plan(home)

    # find living room
    living_room = get_room(home, "LivingRoom")

    # turn on light in living room
    light = get_room_actuators(home, "LivingRoom")[0]
    light.turn_on()
    light.set_brightness_level("medium")

    # turn on Coffee Machine in Kitchen
    kitchen = get_room(home, "Kitchen")
    coffee_machine = get_room_actuators(kitchen, "Kitchen")[0]
    coffee_machine.turn_on()
    coffee_machine.make_coffee("Latte")

    # open window in living room
    window = get_room_actuators(living_room, "LivingRoom")[1]
    window.turn_on()
    # print(window.id)

    # check light intensity
    light_sensor = get_room_sensors(home, "LivingRoom")[0]
    light_sensor.turn_on()
    light_intensity = light_sensor.get_reading()

    if light_intensity < LIGHT_INTENSITY_LOW:
        print("Light intensity is low, turning on living room lights.")
        light.turn_on()
    else:
        print("Light intensity is sufficient.")

    # wait for 5 seconds
    print(f"Waiting for {TEMP_CHANGE_DURATION_WINDOW} seconds...")
    time.sleep(TEMP_CHANGE_DURATION_WINDOW)

    # check indoor temperature and adjust AC
    temp_sensor = get_room_sensors(home, "LivingRoom")[1]
    temp_sensor.turn_on()
    current_temperature = temp_sensor.get_reading()
    print(f"Living room temperature is: {current_temperature}")

    ac = get_room_actuators(home, "LivingRoom")[11]
    if current_temperature > TEMP_HIGH:
        print("Living room temperature is high, turning on AC.")
        ac.turn_on()
    else:
        print("Living room temperature is comfortable.")

    print("Morning plan finished!")


def leave_home_plan(home):
    print(f"\n---Leave Home Plan---")
    # # Example invocation
    # home = home_plan()
    # # home plan
    # print_home_plan(home)

    # lock the door in LivingRoom
    living_room = get_room(home, "LivingRoom")
    door = get_room_actuators(living_room, "LivingRoom")[0]
    door.lock()

    # turn off the lights in LivingRoom
    light = get_room_actuators(living_room, "LivingRoom")[1]
    light.turn_off()

    # turn off the smart sockets in all the rooms
    smart_sockets = get_all_actuators(home, "SmartSocket")
    for socket in smart_sockets:
        socket.turn_off()

    print(f"Leave Home plan Finished")


def movie_plan(home):
    print(f"\n---Movie Plan---")
    # # Example invocation
    # home = home_plan()
    # # home plan
    # print_home_plan(home)

    # find living room
    living_room = get_room(home, "LivingRoom")

    # turn off lights in living room
    light = get_room_actuators(living_room, "LivingRoom")[1]
    light.turn_off()

    # dim the lights in living room
    light.set_brightness_level("low")

    # close the curtains
    curtain = get_room_actuators(living_room, "LivingRoom")[5]
    curtain.turn_off()

    # turn on the TV
    tv = get_room_actuators(living_room, "LivingRoom")[10]
    tv.turn_on()
    # Play a channel (e.g., "Netflix")
    tv.play_channel("Netflix")

    print(f"Movie plan Finished")


if __name__ == '__main__':
    # initialize home plan
    home = home_plan()
    print_home_plan(home)

    # Run morning plan
    morning_plan(home)

    # Run leave home plan
    leave_home_plan(home)

    # Run movie plan
    movie_plan(home)