# Based on your functional description and the provided source code, I will create a `function.py` file that contains the main function. This main function will initialize the home plan, interact with sensors and actuators, and demonstrate some of the functionalities.
# 
# Here is the `function.py` file:

# functions/function.py

from home.home_plan import home_plan, print_home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, DAILY_ROUTINE_DURATION
from home.actuator import Heater, AC, Light, CleaningRobot, NotificationSender
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor

def main():
    # Initialize the home plan
    home = home_plan()
    print_home_plan(home)

    # Example: Get a specific room
    living_room = get_room(home, "LivingRoom")
    if living_room:
        # Example: Turn on all lights in the LivingRoom
        for actuator in get_room_actuators(home, "LivingRoom"):
            if isinstance(actuator, Light):
                actuator.turn_on()

        # Example: Adjust temperature in the LivingRoom
        for sensor in get_room_sensors(home, "LivingRoom"):
            if isinstance(sensor, IndoorTemperatureSensor):
                current_temp = sensor.get_reading()
                if current_temp is not None:
                    for actuator in get_room_actuators(home, "LivingRoom"):
                        if isinstance(actuator, Heater):
                            actuator.set_target_temperature(TEMP_HIGH)
                            actuator.adjust_temperature(current_temp)
                        elif isinstance(actuator, AC):
                            actuator.set_target_temperature(TEMP_LOW)
                            actuator.adjust_temperature(current_temp)

        # Example: Start the cleaning robot's daily routine
        for actuator in get_room_actuators(home, "LivingRoom"):
            if isinstance(actuator, CleaningRobot):
                actuator.turn_on()
                actuator.daily_routine()

        # Example: Send a notification
        for actuator in get_room_actuators(home, "LivingRoom"):
            if isinstance(actuator, NotificationSender):
                actuator.turn_on()
                actuator.notification_sender("Daily cleaning routine completed.")

    # Example: Get all IndoorTemperature sensors and print their readings
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    for sensor in indoor_temp_sensors:
        sensor.turn_on()
        sensor.get_reading()
        sensor.turn_off()

    # Example: Get all Lights and set their brightness to medium
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_on()
        light.set_brightness_level("medium")

if __name__ == "__main__":
    main()