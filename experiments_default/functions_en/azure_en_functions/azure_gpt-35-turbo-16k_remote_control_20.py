# Sure, I can help you with that. Here is the 'function.py' file based on your functional description and the provided source code:

from home.home_plan import home_plan, get_all_sensors, get_all_actuators, get_room_sensors, get_room_actuators, print_home_plan
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC, CleaningRobot, NotificationSender

def main():
    home = home_plan()

    # Get all sensors and actuators
    all_sensors = get_all_sensors(home, "IndoorTemperature")
    all_actuators = get_all_actuators(home, "CleaningRobot")

    # Get sensors and actuators in a specific room
    living_room_sensors = get_room_sensors(home, "LivingRoom")
    living_room_actuators = get_room_actuators(home, "LivingRoom")

    # Print the home plan
    print_home_plan(home)

    # Turn on the air conditioner ten minutes before going home
    for sensor in all_sensors:
        if isinstance(sensor, IndoorTemperatureSensor):
            temperature = sensor.get_reading()
            if temperature is not None and temperature > TEMP_LOW and temperature < TEMP_HIGH:
                for actuator in all_actuators:
                    if isinstance(actuator, AC):
                        actuator.set_target_temperature(temperature - 2)
                        actuator.turn_on()
                        break

    # Use the robot vacuum cleaner to sweep the floor when no one is at home
    for sensor in living_room_sensors:
        if isinstance(sensor, LightIntensiveSensor):
            light_intensity = sensor.get_reading()
            if light_intensity is not None and light_intensity < LIGHT_INTENSITY_LOW:
                for actuator in living_room_actuators:
                    if isinstance(actuator, CleaningRobot):
                        actuator.turn_on()
                        actuator.daily_routine()
                        break

    # Send notification if humidity is too high
    for sensor in all_sensors:
        if isinstance(sensor, HumiditySensor):
            humidity = sensor.get_reading()
            if humidity is not None and humidity > HUMIDITY_HIGH:
                for actuator in all_actuators:
                    if isinstance(actuator, NotificationSender):
                        actuator.notification_sender("Humidity is too high. Please take necessary actions.")
                        break

if __name__ == "__main__":
    main()