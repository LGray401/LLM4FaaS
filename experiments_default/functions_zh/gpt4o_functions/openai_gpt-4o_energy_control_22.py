# Based on the provided functional description and the source code, here's `function.py` that implements the main function to monitor and control the smart home devices as specified. This script will:
# 
# 1. Turn on the smoke alarm if the kitchen smoke level exceeds a certain threshold.
# 2. Automatically manage the AC based on indoor temperature during summer.
# 3. Control lights based on presence detection.
# 
# Here's your `function.py`:

import time
from home.sensor import SmokeSensor, IndoorTemperatureSensor, LightIntensiveSensor
from home.actuator import Light, AC, NotificationSender
from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.config import TEMP_LOW, TEMP_HIGH, DAILY_ROUTINE_DURATION

def main():
    # Get the home plan
    home = home_plan()
    
    # Get kitchen sensors and actuators
    kitchen_sensors = get_room_sensors(home, "Kitchen")
    kitchen_actuators = get_room_actuators(home, "Kitchen")
    
    # Get living room sensors and actuators
    living_room_sensors = get_room_sensors(home, "LivingRoom")
    living_room_actuators = get_room_actuators(home, "LivingRoom")

    # Find specific sensors and actuators
    smoke_sensor = next((sensor for sensor in kitchen_sensors if isinstance(sensor, SmokeSensor)), None)
    ac = next((actuator for actuator in living_room_actuators if isinstance(actuator, AC)), None)
    light = next((actuator for actuator in living_room_actuators if isinstance(actuator, Light)), None)
    notification_sender = next((actuator for actuator in living_room_actuators if isinstance(actuator, NotificationSender)), None)

    # Turn on all sensors and actuators
    for sensor in kitchen_sensors + living_room_sensors:
        sensor.turn_on()
    for actuator in kitchen_actuators + living_room_actuators:
        actuator.turn_on()

    while True:
        # Check smoke levels in the kitchen
        smoke_level = smoke_sensor.get_reading()
        if smoke_level is not None and smoke_level > 50:  # Assuming 50 as the smoke threshold
            notification_sender.notification_sender("Smoke detected in the kitchen! Alarm triggered.")
            print("Smoke detected in the kitchen! Alarm triggered.")
        
        # Check indoor temperature in living room
        for sensor in living_room_sensors:
            if isinstance(sensor, IndoorTemperatureSensor):
                indoor_temp = sensor.get_reading()
                if indoor_temp is not None:
                    if indoor_temp < 20:
                        ac.turn_off()
                    elif indoor_temp > 25:
                        ac.turn_on()
        
        # Check light intensity in living room to simulate presence detection
        for sensor in living_room_sensors:
            if isinstance(sensor, LightIntensiveSensor):
                light_intensity = sensor.get_reading()
                if light_intensity is not None:
                    if light_intensity < 950:  # Assuming 950 as the presence threshold
                        light.turn_on()
                    else:
                        light.turn_off()
        
        time.sleep(DAILY_ROUTINE_DURATION)

if __name__ == "__main__":
    main()