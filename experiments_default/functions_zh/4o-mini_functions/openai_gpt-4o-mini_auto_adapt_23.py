# Based on the functional description you've provided and the existing code in your project, I will create a `function.py` file that will serve as the main entry point for your smart home system. This file will instantiate the necessary sensors and actuators, retrieve readings, and provide feedback on the system's status.
# 
# Here is the `function.py` file:

# function.py
from home.home_plan import home_plan, print_home_plan, get_room_sensors, get_room_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.actuator import Heater, AC, NotificationSender, Light
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor

def main():
    # Initialize the home plan
    home = home_plan()
    
    # Print the home plan structure
    print_home_plan(home)

    # Get sensors and actuators for specific rooms
    living_room_sensors = get_room_sensors(home, "LivingRoom")
    living_room_actuators = get_room_actuators(home, "LivingRoom")

    # Example of getting readings from sensors and adjusting actuators based on the readings
    for sensor in living_room_sensors:
        sensor.turn_on()
        reading = sensor.get_reading()

        if isinstance(sensor, IndoorTemperatureSensor):
            if reading is not None:
                if reading < TEMP_LOW:
                    for actuator in living_room_actuators:
                        if isinstance(actuator, Heater):
                            actuator.set_target_temperature(23)  # Set to a comfortable temperature
                            actuator.adjust_temperature(reading)
                elif reading > TEMP_HIGH:
                    for actuator in living_room_actuators:
                        if isinstance(actuator, AC):
                            actuator.set_target_temperature(23)  # Set to a comfortable temperature
                            actuator.adjust_temperature(reading)

        elif isinstance(sensor, HumiditySensor):
            if reading is not None:
                if reading < HUMIDITY_LOW:
                    for actuator in living_room_actuators:
                        if isinstance(actuator, NotificationSender):
                            actuator.turn_on()
                            actuator.notification_sender("Humidity is low, consider using a humidifier.")
                
        elif isinstance(sensor, LightIntensiveSensor):
            if reading is not None:
                if reading < LIGHT_INTENSITY_LOW:
                    for actuator in living_room_actuators:
                        if isinstance(actuator, Light):
                            actuator.turn_on()
                            actuator.set_brightness_level('high')
                elif reading > LIGHT_INTENSITY_HIGH:
                    for actuator in living_room_actuators:
                        if isinstance(actuator, Light):
                            actuator.turn_on()
                            actuator.set_brightness_level('low')

    # Send notifications
    notifier = next((actuator for actuator in living_room_actuators if isinstance(actuator, NotificationSender)), None)
    if notifier:
        notifier.turn_on()
        notifier.notification_sender("All systems are functioning properly.")
    
    # Turn off the sensors after use
    for sensor in living_room_sensors:
        sensor.turn_off()

if __name__ == "__main__":
    main()