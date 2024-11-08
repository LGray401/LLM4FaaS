# Based on your functional description and the provided source code, I will create a `function.py` file that includes the main function to handle the smart home functionalities as described. The main function will check for smoke levels in the kitchen, manage the air conditioner based on the indoor temperature, and control the lights based on presence.
# 
# Here is the `function.py` file:

# functions/function.py

from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.sensor import IndoorTemperatureSensor, SmokeSensor
from home.actuator import Light, AC
from home.config import TEMP_HIGH, TEMP_LOW
import time

def main():
    # Initialize the home plan
    home = home_plan()

    while True:
        # Check for smoke in the kitchen
        kitchen_sensors = get_room_sensors(home, "Kitchen")
        for sensor in kitchen_sensors:
            if isinstance(sensor, SmokeSensor):
                sensor.turn_on()
                reading = sensor.get_reading()
                if reading is not None and reading > 50:  # Assume 50 is the threshold for smoke detection
                    print(f"Smoke detected in Kitchen! Reading: {reading}")
                    # Turn on the smoke alarm (assuming it's an actuator)
                    for actuator in get_room_actuators(home, "Kitchen"):
                        if isinstance(actuator, NotificationSender):
                            actuator.turn_on()
                            actuator.notification_sender("Smoke detected in the kitchen!")
                            break

        # Manage the air conditioner in all rooms
        for room_name in ["LivingRoom", "Bedroom", "Kitchen", "Bathroom"]:
            sensors = get_room_sensors(home, room_name)
            actuators = get_room_actuators(home, room_name)

            for sensor in sensors:
                if isinstance(sensor, IndoorTemperatureSensor):
                    sensor.turn_on()
                    temp_reading = sensor.get_reading()
                    if temp_reading is not None:
                        for actuator in actuators:
                            if isinstance(actuator, AC):
                                if temp_reading < TEMP_LOW:
                                    actuator.turn_off()
                                    print(f"AC turned off in {room_name}. Temperature: {temp_reading}°C")
                                elif temp_reading > TEMP_HIGH:
                                    actuator.turn_on()
                                    print(f"AC turned on in {room_name}. Temperature: {temp_reading}°C")

        # Manage the lights in all rooms
        for room_name in ["LivingRoom", "Bedroom", "Kitchen", "Bathroom"]:
            sensors = get_room_sensors(home, room_name)
            actuators = get_room_actuators(home, room_name)

            for sensor in sensors:
                if isinstance(sensor, LightIntensiveSensor):
                    sensor.turn_on()
                    light_reading = sensor.get_reading()
                    if light_reading is not None:
                        for actuator in actuators:
                            if isinstance(actuator, Light):
                                if light_reading < LIGHT_INTENSITY_LOW:
                                    actuator.turn_on()
                                    print(f"Light turned on in {room_name}. Light intensity: {light_reading} lux")
                                elif light_reading > LIGHT_INTENSITY_HIGH:
                                    actuator.turn_off()
                                    print(f"Light turned off in {room_name}. Light intensity: {light_reading} lux")

        # Sleep for a short duration before the next check
        time.sleep(TEMP_CHANGE_DURATION_WINDOW)

if __name__ == "__main__":
    main()