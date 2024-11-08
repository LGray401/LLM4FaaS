# Based on your functional description and the provided source code, I will create a `function.py` file that contains the main function to manage your smart home. This function will initialize the rooms, sensors, and actuators, and provide some basic functionality to interact with them.
# 
# Here is the `function.py` file:

from home.home_plan import home_plan, print_home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators
from home.sensor import Sensor
from home.actuator import Actuator
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
import time

def main():
    # Initialize the home plan
    home = home_plan()
    print_home_plan(home)

    # Example interactions
    # Turn on all lights in the LivingRoom
    living_room = get_room(home, "LivingRoom")
    if living_room:
        for actuator in living_room.actuators:
            if actuator.actuator_type == "Light":
                actuator.turn_on()

    # Get temperature readings from all IndoorTemperature sensors
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    for sensor in indoor_temp_sensors:
        sensor.turn_on()
        print(f"{sensor.id} reading: {sensor.get_reading()}")
        sensor.turn_off()

    # Adjust heaters and ACs based on temperature thresholds
    for room in home:
        temp_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "IndoorTemperature"]
        heaters = [actuator for actuator in room.actuators if actuator.actuator_type == "Heater"]
        acs = [actuator for actuator in room.actuators if actuator.actuator_type == "AC"]

        if temp_sensors:
            temp_sensor = temp_sensors[0]  # Assuming only one temperature sensor per room for simplicity
            temp_sensor.turn_on()
            current_temp = temp_sensor.get_reading()
            temp_sensor.turn_off()

            for heater in heaters:
                if current_temp < TEMP_LOW:
                    heater.turn_on()
                else:
                    heater.turn_off()

            for ac in acs:
                if current_temp > TEMP_HIGH:
                    ac.turn_on()
                else:
                    ac.turn_off()

    # Example of getting notifications for smoke detected
    smoke_sensors = get_all_sensors(home, "Smoke")
    notification_senders = get_all_actuators(home, "NotificationSender")
    for smoke_sensor in smoke_sensors:
        smoke_sensor.turn_on()
        smoke_level = smoke_sensor.get_reading()
        if smoke_level > 50:  # Example threshold
            for notification_sender in notification_senders:
                notification_sender.turn_on()
                notification_sender.notification_sender(f"Smoke detected in {smoke_sensor.room_name}!")
                notification_sender.turn_off()
        smoke_sensor.turn_off()

    # Daily routine for cleaning robots
    cleaning_robots = get_all_actuators(home, "CleaningRobot")
    for robot in cleaning_robots:
        robot.turn_on()
        robot.daily_routine()
        # Give some time for the robot to finish its routine before turning it off (handled within daily_routine method)

    # Example of turning on the coffee machine in the Kitchen
    kitchen = get_room(home, "Kitchen")
    if kitchen:
        for actuator in kitchen.actuators:
            if actuator.actuator_type == "CoffeeMachine":
                actuator.turn_on()
                actuator.make_coffee("Espresso")
                # Assuming the coffee machine turns off automatically or you can add logic to turn it off after use

    # Additional functionality can be added as needed

if __name__ == "__main__":
    main()