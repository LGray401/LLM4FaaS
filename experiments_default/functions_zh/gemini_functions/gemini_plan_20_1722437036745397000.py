from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, \
    OutdoorTemperatureSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, \
    SmartSocket, Door, \
    CleaningRobot, SmartTV
from home.config import TEMP_HIGH, TEMP_LOW, HUMIDITY_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_HIGH, \
    LIGHT_INTENSITY_LOW, DAILY_ROUTINE_DURATION
from home.logger_config import logger

# from home import *
import time

def morning_plan(home):
    living_room = get_room(home, "LivingRoom")
    if living_room is not None:
        curtain = get_room_actuators(home, "LivingRoom")[5] # curtain is the 5th actuator
        if curtain is not None:
            curtain.turn_on()
        else:
            logger.warning(f"Fail to find curtain in living room, cannot open it.")


def leave_home_plan(home):
    # all_lights = get_all_actuators(home, "Light")
    living_room = get_room(home, "LivingRoom")
    if living_room is not None:
        light = get_room_actuators(living_room, "LivingRoom")[1]
        if light is not None:
            light.turn_off()
        else:
            logger.warning(f"Fail to find light in living room, cannot turn it off.")
    else:
        logger.warning(f"Fail to find living room.")

    bedroom = get_room(home, "Bedroom")
    if bedroom is not None:
        light = get_room_actuators(bedroom, "Bedroom")[0]
        if light is not None:
            light.turn_off()
        else:
            logger.warning(f"Fail to find light in bedroom, cannot turn it off.")
    else:
        logger.warning(f"Fail to find bedroom.")


def movie_plan(home):
    living_room = get_room(home, "LivingRoom")
    if living_room is not None:
        light = get_room_actuators(home, "LivingRoom")[1] # light is the 1st actuator
        if light is not None:
            light.set_brightness_level("low")
        else:
            logger.warning(f"Fail to find light in living room, cannot turn it off.")
    else:
        logger.warning(f"Fail to find living room.")


def daily_routine(home):
    cleaning_robot = get_all_actuators(home, "CleaningRobot")[0]
    if cleaning_robot is not None:
        cleaning_robot.turn_on()
        cleaning_robot.daily_routine()
    else:
        logger.warning(f"Fail to find Cleaning Robot, cannot start the daily cleaning.")


def temperature_control(home):
    for room in home:
        # Get temperature sensors in each room
        temperature_sensors = get_room_sensors(home, room.name)
        if temperature_sensors is not None:
            for sensor in temperature_sensors:
                if sensor.sensor_type == "IndoorTemperature":
                    current_temperature = sensor.get_reading()
                    if current_temperature is not None:
                        # Get heaters and ACs in each room
                        heaters = get_room_actuators(home, room.name)
                        if heaters is not None:
                            for heater in heaters:
                                if heater.actuator_type == "Heater":
                                    heater.adjust_temperature(current_temperature)
                        acs = get_room_actuators(home, room.name)
                        if acs is not None:
                            for ac in acs:
                                if ac.actuator_type == "AC":
                                    ac.adjust_temperature(current_temperature)


def humidity_control(home):
    for room in home:
        humidity_sensors = get_room_sensors(home, room.name)
        if humidity_sensors is not None:
            for sensor in humidity_sensors:
                if sensor.sensor_type == "Humidity":
                    current_humidity = sensor.get_reading()
                    if current_humidity is not None:
                        # Get humidifiers in each room
                        humidifiers = get_room_actuators(home, room.name)
                        if humidifiers is not None:
                            for humidifier in humidifiers:
                                if humidifier.actuator_type == "Humidifier":
                                    if current_humidity < HUMIDITY_LOW:
                                        humidifier.increase_humidity()
                                    elif current_humidity > HUMIDITY_HIGH:
                                        humidifier.decrease_humidity()


def light_intensity_control(home):
    for room in home:
        light_intensity_sensors = get_room_sensors(home, room.name)
        if light_intensity_sensors is not None:
            for sensor in light_intensity_sensors:
                if sensor.sensor_type == "LightIntensive":
                    current_light_intensity = sensor.get_reading()
                    if current_light_intensity is not None:
                        # Get lights in each room
                        lights = get_room_actuators(home, room.name)
                        if lights is not None:
                            for light in lights:
                                if light.actuator_type == "Light":
                                    if current_light_intensity < LIGHT_INTENSITY_LOW:
                                        light.turn_on()
                                    elif current_light_intensity > LIGHT_INTENSITY_HIGH:
                                        light.turn_off()


def smoke_alarm(home):
    for room in home:
        smoke_sensors = get_room_sensors(home, room.name)
        if smoke_sensors is not None:
            for sensor in smoke_sensors:
                if sensor.sensor_type == "Smoke":
                    current_smoke_reading = sensor.get_reading()
                    if current_smoke_reading is not None:
                        # Get notification sender in each room
                        notification_sender = get_room_actuators(home, room.name)
                        if notification_sender is not None:
                            for sender in notification_sender:
                                if sender.actuator_type == "NotificationSender":
                                    sender.notification_sender(f"Smoke detected in {room.name}!")
                                    # take further actions like turning on ventilation, opening windows, etc.


def main():
    home = home_plan()
    # print_home_plan(home)
    print(f"Welcome to your Smart Home!")
    # Start the Smart Home System
    while True:
        # Example: Run plans and controls
        # morning_plan(home) # Example plan
        # temperature_control(home)
        # humidity_control(home)
        # light_intensity_control(home)
        # leave_home_plan(home) # Example plan
        # movie_plan(home) # Example plan
        smoke_alarm(home)
        daily_routine(home)

        time.sleep(1)