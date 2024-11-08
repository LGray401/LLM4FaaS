# Given the functional description and the provided code, here's a `function.py` file located in the `functions` folder that contains the main function to control various components of the smart home project.

# functions/function.py

import time
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor
from home.actuator import Heater, AC, Light, CleaningRobot, NotificationSender
from home.home_plan import home_plan
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, DAILY_ROUTINE_DURATION

def control(home):
    for room in home:
        print(f"\nChecking {room.name}...")

        # Iterate through each sensor and get readings
        for sensor in room.sensors:
            sensor.turn_on()
            reading = sensor.get_reading()
            sensor.turn_off()
            
            if isinstance(sensor, IndoorTemperatureSensor) or isinstance(sensor, OutdoorTemperatureSensor):
                if reading < TEMP_LOW:
                    print(f"Temperature in {room.name} is too low.")
                    actuators = [actuator for actuator in room.actuators if isinstance(actuator, Heater)]
                    for actuator in actuators:
                        actuator.turn_on()
                        actuator.set_target_temperature(TEMP_HIGH)
                elif reading > TEMP_HIGH:
                    print(f"Temperature in {room.name} is too high.")
                    actuators = [actuator for actuator in room.actuators if isinstance(actuator, AC)]
                    for actuator in actuators:
                        actuator.turn_on()
                        actuator.set_target_temperature(TEMP_LOW)
            
            elif isinstance(sensor, HumiditySensor):
                if reading < HUMIDITY_LOW:
                    print(f"Humidity in {room.name} is too low.")
                    actuators = [actuator for actuator in room.actuators if isinstance(actuator, Humidifier)]
                    for actuator in actuators:
                        actuator.turn_on()
                        actuator.increase_humidity()
                elif reading > HUMIDITY_HIGH:
                    print(f"Humidity in {room.name} is too high.")
                    actuators = [actuator for actuator in room.actuators if isinstance(actuator, Humidifier)]
                    for actuator in actuators:
                        actuator.turn_on()
                        actuator.decrease_humidity()
            
            elif isinstance(sensor, LightIntensiveSensor):
                if reading < LIGHT_INTENSITY_LOW:
                    print(f"Light intensity in {room.name} is too low.")
                    actuators = [actuator for actuator in room.actuators if isinstance(actuator, Light)]
                    for actuator in actuators:
                        actuator.turn_on()
                        actuator.set_brightness_level("high")
                elif reading > LIGHT_INTENSITY_HIGH:
                    print(f"Light intensity in {room.name} is too high.")
                    actuators = [actuator for actuator in room.actuators if isinstance(actuator, Light)]
                    for actuator in actuators:
                        actuator.turn_off()
            
            elif isinstance(sensor, SmokeSensor):
                if reading > 0:
                    print(f"Smoke detected in {room.name}.")
                    actuators = [actuator for actuator in room.actuators if isinstance(actuator, NotificationSender)]
                    for actuator in actuators:
                        actuator.turn_on()
                        actuator.notification_sender("Smoke detected! Please check immediately.")
                        actuator.turn_off()

def main():
    home = home_plan()
    while True:
        control(home)
        print("Sleeping for the configured duration...")
        time.sleep(DAILY_ROUTINE_DURATION)

if __name__ == "__main__":
    main()