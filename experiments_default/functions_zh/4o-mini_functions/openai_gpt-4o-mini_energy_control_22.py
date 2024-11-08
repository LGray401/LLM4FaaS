# Based on the functional description you provided and the existing source code, here is the implementation of the `function.py` file. This file will contain the main function that will monitor sensor readings and control actuators according to the specified conditions.

# functions/function.py
from home.home_plan import home_plan
from home.config import TEMP_LOW, TEMP_HIGH
from home.sensor import SmokeSensor, IndoorTemperatureSensor
from home.actuator import AC, Light


def main():
    # Create the home with rooms and their components
    home = home_plan()

    # Assume we are monitoring the Kitchen room
    kitchen = next((room for room in home if room.name == "Kitchen"), None)

    if kitchen is not None:
        smoke_sensor = next((sensor for sensor in kitchen.sensors if isinstance(sensor, SmokeSensor)), None)
        indoor_temp_sensor = next((sensor for sensor in kitchen.sensors if isinstance(sensor, IndoorTemperatureSensor)), None)
        ac = next((actuator for actuator in kitchen.actuators if isinstance(actuator, AC)), None)
        light = next((actuator for actuator in kitchen.actuators if isinstance(actuator, Light)), None)

        # Turn on sensors to get readings
        if smoke_sensor:
            smoke_sensor.turn_on()
        if indoor_temp_sensor:
            indoor_temp_sensor.turn_on()

        # Monitor smoke and temperature
        smoke_reading = smoke_sensor.get_reading() if smoke_sensor else None
        temp_reading = indoor_temp_sensor.get_reading() if indoor_temp_sensor else None

        # Check smoke level and respond
        if smoke_reading is not None and smoke_reading > 50:  # Assuming 50 is the threshold for smoke
            print("Smoke level is high! Activating smoke alarm.")
            # Here you can add code to activate smoke alarm
            # For example, you can turn on a notification sender actuator

        # Check temperature thresholds and control AC
        if temp_reading is not None:
            if temp_reading < TEMP_LOW:
                print("Temperature is low. Turning off the AC.")
                if ac:
                    ac.turn_off()
            elif temp_reading > TEMP_HIGH:
                print("Temperature is high. Turning on the AC.")
                if ac:
                    ac.turn_on()

        # Control lights based on occupancy (assumed logic)
        # Here you would have some occupancy sensor logic; for now, let's assume it's based on smoke presence
        if smoke_reading is not None and smoke_reading > 0:  # Presence detected
            print("Someone is in the kitchen. Turning on the lights.")
            if light:
                light.turn_on()
        else:
            print("No one is in the kitchen. Turning off the lights.")
            if light:
                light.turn_off()

        # Cleanup: turn off sensors
        if smoke_sensor:
            smoke_sensor.turn_off()
        if indoor_temp_sensor:
            indoor_temp_sensor.turn_off()

    else:
        print("Kitchen not found in the home plan.")


if __name__ == "__main__":
    main()