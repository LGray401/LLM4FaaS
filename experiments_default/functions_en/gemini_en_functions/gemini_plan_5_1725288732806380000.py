from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators, print_home_plan
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, \
    OutdoorTemperatureSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, \
    SmartSocket, Door, \
    CleaningRobot, SmartTV
from home.config import TEMP_CHANGE_DURATION_WINDOW, TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, \
    LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger

import time


def morning_plan(home):
    print("\n--- Morning Plan ---")
    logger.info("Starting Morning Plan")

    # Get the coffee machine in the kitchen
    kitchen = get_room(home, "Kitchen")
    coffee_machine = get_room_actuators(home, "Kitchen")[0]  # Assuming there's only one coffee machine

    # Turn on the coffee machine and make coffee
    if coffee_machine.status == "off":
        coffee_machine.turn_on()
    coffee_machine.make_coffee("Espresso")

    # Adjust temperature in the living room if needed
    living_room = get_room(home, "LivingRoom")
    living_room_temp_sensor = get_room_sensors(home, "LivingRoom")[0]
    living_room_heater = get_room_actuators(home, "LivingRoom")[0]
    current_temp = living_room_temp_sensor.get_reading()
    if current_temp < TEMP_LOW:
        living_room_heater.turn_on()
        living_room_heater.set_target_temperature(TEMP_HIGH)
        print(f"Turned on Heater in Living Room to {TEMP_HIGH}°C.")
        logger.info(f"Turned on Heater in Living Room to {TEMP_HIGH}°C.")
        time.sleep(TEMP_CHANGE_DURATION_WINDOW)
    elif current_temp > TEMP_HIGH:
        living_room_heater.turn_off()
        print(f"Turned off Heater in Living Room.")
        logger.info(f"Turned off Heater in Living Room.")

    print("Morning Plan Completed")
    logger.info("Morning Plan Completed")


def leave_home_plan(home):
    print("\n--- Leave Home Plan ---")
    logger.info("Starting Leave Home Plan")

    # Turn off lights in all rooms
    for room in home:
        for light in room.actuators:
            if light.actuator_type == "Light":
                if light.status == "on":
                    light.turn_off()
                    print(f"Turned off light in {room.name}")
                    logger.info(f"Turned off light in {room.name}")

    # Lock all doors
    all_doors = get_all_actuators(home, "Door")
    for door in all_doors:
        door.lock()
        print(f"Locked {door.id}")
        logger.info(f"Locked {door.id}")

    print("Leave Home Plan Completed")
    logger.info("Leave Home Plan Completed")


def movie_plan(home):
    print("\n--- Movie Plan ---")
    logger.info("Starting Movie Plan")

    # Get the living room and its components
    living_room = get_room(home, "LivingRoom")
    living_room_curtain = get_room_actuators(living_room, "Curtain")[0]
    living_room_tv = get_room_actuators(living_room, "SmartTV")[0]

    # Close the curtains
    if living_room_curtain.status == "off":
        living_room_curtain.turn_on()
    print(f"Closed curtains in Living Room.")
    logger.info(f"Closed curtains in Living Room.")

    # Turn on the TV and play a movie
    if living_room_tv.status == "off":
        living_room_tv.turn_on()
    living_room_tv.play_channel("Netflix")
    print(f"Turned on TV in Living Room and started playing Netflix.")
    logger.info(f"Turned on TV in Living Room and started playing Netflix.")

    # Adjust lighting
    living_room_light_sensor = get_room_sensors(living_room, "LightIntensive")[0]
    current_light_intensity = living_room_light_sensor.get_reading()
    for light in living_room.actuators:
        if light.actuator_type == "Light":
            if current_light_intensity > LIGHT_INTENSITY_HIGH:
                light.turn_off()
                print(f"Turned off light in Living Room because light intensity is too high.")
                logger.info(f"Turned off light in Living Room because light intensity is too high.")
            elif current_light_intensity < LIGHT_INTENSITY_LOW:
                light.turn_on()
                light.set_brightness_level("low")
                print(f"Turned on light in Living Room with low brightness.")
                logger.info(f"Turned on light in Living Room with low brightness.")

    print("Movie Plan Completed")
    logger.info("Movie Plan Completed")


def main():
    home = home_plan()
    print_home_plan(home)

    morning_plan(home)
    leave_home_plan(home)
    movie_plan(home)


if __name__ == "__main__":
    main()
