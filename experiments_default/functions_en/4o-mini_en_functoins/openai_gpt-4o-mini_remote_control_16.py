# Based on your functional description and the provided source code, I'll create a `function.py` file that serves as the main entry point for your smart home project. This file will utilize the classes defined in `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py` to control the smart home environment.
# 
# Here’s the `function.py` code:

# functions/function.py
from home.home_plan import home_plan, print_home_plan, get_room, get_room_sensors, get_room_actuators
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor, HumiditySensor
from home.actuator import Heater, AC, Light, NotificationSender, CleaningRobot

def main():
    # Initialize the home plan
    home = home_plan()

    # Print the home plan
    print_home_plan(home)

    # Example control logic
    room_name = "LivingRoom"
    room = get_room(home, room_name)

    if room:
        # Get sensors in the room
        sensors = get_room_sensors(home, room_name)
        actuators = get_room_actuators(home, room_name)

        # Example: Check temperature and control the heater and AC
        temperature_sensor = next((sensor for sensor in sensors if isinstance(sensor, IndoorTemperatureSensor)), None)
        if temperature_sensor:
            temperature_sensor.turn_on()
            current_temp = temperature_sensor.get_reading()

            heater = next((actuator for actuator in actuators if isinstance(actuator, Heater)), None)
            ac = next((actuator for actuator in actuators if isinstance(actuator, AC)), None)

            if current_temp is not None:
                if heater:
                    heater.set_target_temperature(22)  # Set desired temperature
                    heater.adjust_temperature(current_temp)

                if ac:
                    ac.set_target_temperature(24)  # Set desired temperature
                    ac.adjust_temperature(current_temp)

        # Control the light
        light = next((actuator for actuator in actuators if isinstance(actuator, Light)), None)
        if light:
            light.turn_on()
            light.set_brightness_level('high')

        # Send a notification
        notifier = next((actuator for actuator in actuators if isinstance(actuator, NotificationSender)), None)
        if notifier:
            notifier.turn_on()
            notifier.notification_sender("All systems are operational in the Living Room.")

        # Start cleaning robot
        cleaning_robot = next((actuator for actuator in actuators if isinstance(actuator, CleaningRobot)), None)
        if cleaning_robot:
            cleaning_robot.turn_on()
            cleaning_robot.daily_routine()

if __name__ == "__main__":
    main()