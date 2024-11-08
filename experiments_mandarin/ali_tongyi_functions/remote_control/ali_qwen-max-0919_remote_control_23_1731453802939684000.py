# Based on your functional description and the provided source code, I will create a `function.py` file that contains the main function to control the smart home system. This script will initialize the home plan, simulate sensor readings, and control actuators based on the readings.
# 
# Here is the `function.py` file:

# functions/function.py

import time
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, OutdoorTemperatureSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, SmartSocket, Door, CleaningRobot, SmartTV, Humidifier
from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, DAILY_ROUTINE_DURATION

def main():
    # Initialize the home plan
    home = home_plan()
    print_home_plan(home)

    # Simulate the smart home system
    while True:
        for room in home:
            # Get sensors and actuators for the current room
            sensors = get_room_sensors(home, room.name)
            actuators = get_room_actuators(home, room.name)

            # Simulate sensor readings
            for sensor in sensors:
                sensor.turn_on()
                reading = sensor.get_reading()
                sensor.turn_off()

                if reading is not None:
                    # Control actuators based on sensor readings
                    if isinstance(sensor, IndoorTemperatureSensor):
                        for actuator in [act for act in actuators if isinstance(act, (Heater, AC))]:
                            if reading < TEMP_LOW:
                                actuator.set_target_temperature(TEMP_HIGH)
                                actuator.adjust_temperature(reading)
                            elif reading > TEMP_HIGH:
                                actuator.set_target_temperature(TEMP_LOW)
                                actuator.adjust_temperature(reading)
                            else:
                                actuator.turn_off()

                    elif isinstance(sensor, HumiditySensor):
                        for actuator in [act for act in actuators if isinstance(act, Humidifier)]:
                            if reading < HUMIDITY_LOW:
                                actuator.increase_humidity()
                            elif reading > HUMIDITY_HIGH:
                                actuator.decrease_humidity()
                            else:
                                actuator.turn_off()

                    elif isinstance(sensor, LightIntensiveSensor):
                        for actuator in [act for act in actuators if isinstance(act, Light)]:
                            if reading < LIGHT_INTENSITY_LOW:
                                actuator.turn_on()
                                actuator.set_brightness_level("high")
                            elif reading > LIGHT_INTENSITY_HIGH:
                                actuator.turn_off()
                            else:
                                actuator.set_brightness_level("medium")

                    # Additional logic for other sensors and actuators can be added here

        # Daily routine for cleaning robots
        for robot in get_all_actuators(home, "CleaningRobot"):
            robot.turn_on()
            robot.daily_routine()

        # Wait for a while before the next iteration
        time.sleep(DAILY_ROUTINE_DURATION)

def print_home_plan(home):
    print(f"\n---Home Plan---")
    for room in home:
        room.print_info()

if __name__ == "__main__":
    main()