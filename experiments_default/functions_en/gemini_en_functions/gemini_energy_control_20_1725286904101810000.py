from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators, print_home_plan
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, \
    OutdoorTemperatureSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, \
    SmartSocket, Door, \
    CleaningRobot, SmartTV
from home.config import TEMP_CHANGE_DURATION_WINDOW, TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, \
    LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

import time


def main():
    """
    Main function for the smart home system.
    """
    # Get home plan and print it
    home = home_plan()
    print_home_plan(home)

    # # Example: Adjust temperature in Living Room
    # living_room = get_room(home, "LivingRoom")
    # if living_room:
    #     temperature_sensor = get_room_sensors(home, "LivingRoom")[0]
    #     heater = get_room_actuators(home, "LivingRoom")[0]
    #     # Simulate a low temperature scenario
    #     temperature_sensor.turn_on()
    #     while temperature_sensor.get_reading() < TEMP_LOW:
    #         print(f"Current temperature is {temperature_sensor.get_reading()}°C. Turning on heater...")
    #         heater.turn_on()
    #         time.sleep(TEMP_CHANGE_DURATION_WINDOW)
    #         print(f"Current temperature is {temperature_sensor.get_reading()}°C.")
    #     heater.turn_off()

    # # Example: Adjust humidity in Kitchen
    # kitchen = get_room(home, "Kitchen")
    # if kitchen:
    #     humidity_sensor = get_room_sensors(home, "Kitchen")[0]
    #     humidifier = get_room_actuators(home, "Kitchen")[0]
    #     # Simulate a low humidity scenario
    #     humidity_sensor.turn_on()
    #     while humidity_sensor.get_reading() < HUMIDITY_LOW:
    #         print(f"Current humidity is {humidity_sensor.get_reading()}%. Increasing humidity...")
    #         humidifier.increase_humidity()
    #         time.sleep(TEMP_CHANGE_DURATION_WINDOW)
    #         print(f"Current humidity is {humidity_sensor.get_reading()}%.")
    #     # Simulate a high humidity scenario
    #     while humidity_sensor.get_reading() > HUMIDITY_HIGH:
    #         print(f"Current humidity is {humidity_sensor.get_reading()}%. Decreasing humidity...")
    #         humidifier.decrease_humidity()
    #         time.sleep(TEMP_CHANGE_DURATION_WINDOW)
    #         print(f"Current humidity is {humidity_sensor.get_reading()}%.")
    #     humidifier.turn_off()

    # # Example: Adjust light intensity in Bedroom
    # bedroom = get_room(home, "Bedroom")
    # if bedroom:
    #     light_sensor = get_room_sensors(home, "Bedroom")[0]
    #     light = get_room_actuators(home, "Bedroom")[0]
    #     # Simulate a low light intensity scenario
    #     light_sensor.turn_on()
    #     while light_sensor.get_reading() < LIGHT_INTENSITY_LOW:
    #         print(f"Current light intensity is {light_sensor.get_reading()} lux. Turning on light...")
    #         light.turn_on()
    #         light.set_brightness_level("high")
    #         time.sleep(TEMP_CHANGE_DURATION_WINDOW)
    #         print(f"Current light intensity is {light_sensor.get_reading()} lux.")
    #     light.turn_off()
    # # Simulate a high light intensity scenario
    #     while light_sensor.get_reading() > LIGHT_INTENSITY_HIGH:
    #         print(f"Current light intensity is {light_sensor.get_reading()} lux. Turning on light...")
    #         light.turn_on()
    #         light.set_brightness_level("low")
    #         time.sleep(TEMP_CHANGE_DURATION_WINDOW)
    #         print(f"Current light intensity is {light_sensor.get_reading()} lux.")
    #     light.turn_off()

    # Example: Trigger daily routine for cleaning robot in Living Room
    living_room = get_room(home, "LivingRoom")
    if living_room:
        cleaning_robot = get_room_actuators(home, "LivingRoom")[0]
        cleaning_robot.turn_on()
        cleaning_robot.daily_routine()
        cleaning_robot.turn_off()


if __name__ == "__main__":
    main()
