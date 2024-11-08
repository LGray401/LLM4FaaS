# Sure! Here is the 'function.py' file based on your functional description and the given source code:

from home.home_plan import home_plan, get_room_actuators, get_room_sensors
from home.actuator import CoffeeMachine, Door, SmartTV
from home.sensor import LightIntensiveSensor, IndoorTemperatureSensor
from home.logger_config import logger


def morning_plan():
    logger.info("Executing Morning Plan")
    print("Executing Morning Plan")

    home = home_plan()
    living_room_sensors = get_room_sensors(home, "LivingRoom")

    for sensor in living_room_sensors:
        if isinstance(sensor, LightIntensiveSensor):
            if sensor.get_reading() < 200:  # Adjust the threshold value as per your requirement
                logger.info("It is dark in the room. Turning on the lights.")
                print("It is dark in the room. Turning on the lights.")
                living_room_actuators = get_room_actuators(home, "LivingRoom")
                for actuator in living_room_actuators:
                    if isinstance(actuator, SmartTV):
                        actuator.turn_on()
                    elif isinstance(actuator, Door):
                        actuator.unlock()
                    elif isinstance(actuator, CoffeeMachine):
                        actuator.make_coffee("7.40 degree coffee")

    logger.info("Morning Plan executed successfully.")
    print("Morning Plan executed successfully.")


def leave_home_plan():
    logger.info("Executing Leave Home Plan")
    print("Executing Leave Home Plan")

    home = home_plan()
    living_room_sensors = get_room_sensors(home, "LivingRoom")

    for sensor in living_room_sensors:
        if isinstance(sensor, IndoorTemperatureSensor):
            current_temperature = sensor.get_reading()
            if current_temperature > 25:  # Adjust the threshold value as per your requirement
                logger.info("It is hot in the room. Turning on the AC.")
                print("It is hot in the room. Turning on the AC.")
                living_room_actuators = get_room_actuators(home, "LivingRoom")
                for actuator in living_room_actuators:
                    if isinstance(actuator, Door):
                        actuator.lock()

    logger.info("Leave Home Plan executed successfully.")
    print("Leave Home Plan executed successfully.")


def movie_plan():
    logger.info("Executing Movie Plan")
    print("Executing Movie Plan")

    home = home_plan()
    living_room_actuators = get_room_actuators(home, "LivingRoom")

    for actuator in living_room_actuators:
        if isinstance(actuator, SmartTV):
            actuator.play_channel("Movie")

    logger.info("Movie Plan executed successfully.")
    print("Movie Plan executed successfully.")


if __name__ == "__main__":
    morning_plan()
    leave_home_plan()
    movie_plan()