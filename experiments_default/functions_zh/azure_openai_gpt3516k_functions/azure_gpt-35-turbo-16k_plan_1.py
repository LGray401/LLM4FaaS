# Here is the 'function.py' file you requested:

from home.home_plan import home_plan, print_home_plan, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, OutdoorTemperatureSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, SmartSocket, Door, CleaningRobot, SmartTV
from home.logger_config import logger
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

home = home_plan()

def main():
    # print_home_plan(home)
    
    room_name = input("Enter the name of the room: ")
    sensors = get_room_sensors(home, room_name)
    if sensors is not None:
        print("\n---Sensors in the room---")
        for sensor in sensors:
            print(sensor.id)
    
    actuators = get_room_actuators(home, room_name)
    if actuators is not None:
        print("\n---Actuators in the room---")
        for actuator in actuators:
            print(actuator.id)

    indoor_temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    print("\n---All Indoor Temperature Sensors---")
    for sensor in indoor_temperature_sensors:
        print(sensor.id)

    light_actuators = get_all_actuators(home, "Light")
    print("\n---All Light Actuators---")
    for actuator in light_actuators:
        print(actuator.id)

    logger.info("Function executed successfully.")

if __name__ == "__main__":
    main()