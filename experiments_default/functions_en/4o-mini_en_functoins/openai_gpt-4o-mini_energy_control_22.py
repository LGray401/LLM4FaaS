# Based on your functional description and the provided source code, I will create a `function.py` file that implements the specified functionalities for your smart home project. 
# 
# The functionalities include:
# 1. Activating the smoke alarm when smoke levels exceed a certain threshold.
# 2. Automatically managing the air conditioner based on indoor temperature readings.
# 3. Controlling the light based on the presence of people detected by a sensor.
# 
# Here's how the `function.py` file will look:

# functions/function.py
from home.home_plan import home_plan
from home.config import TEMP_LOW, TEMP_HIGH
from home.sensor import SmokeSensor, IndoorTemperatureSensor
from home.actuator import AC, Light

def main():
    # Initialize home plan
    home = home_plan()

    # Get kitchen and living room
    kitchen = next(room for room in home if room.name == "Kitchen")
    living_room = next(room for room in home if room.name == "LivingRoom")

    # Initialize smoke sensor and air conditioner
    smoke_sensor = next(sensor for sensor in kitchen.sensors if isinstance(sensor, SmokeSensor))
    indoor_temp_sensor = next(sensor for sensor in living_room.sensors if isinstance(sensor, IndoorTemperatureSensor))
    ac = next(actuator for actuator in living_room.actuators if isinstance(actuator, AC))
    light = next(actuator for actuator in living_room.actuators if isinstance(actuator, Light))

    # Turn on the smoke sensor and get readings
    smoke_sensor.turn_on()
    smoke_reading = smoke_sensor.get_reading()

    # Check smoke levels and activate smoke alarm if necessary
    if smoke_reading is not None and smoke_reading > 50:  # Assuming 50 is the threshold for smoke
        print("Smoke detected! Activating smoke alarm.")
        # Here you can implement the smoke alarm functionality, e.g., send notification, etc.

    # Turn on the indoor temperature sensor and get readings
    indoor_temp_sensor.turn_on()
    indoor_temp_reading = indoor_temp_sensor.get_reading()

    # Adjust air conditioner based on temperature readings
    if indoor_temp_reading is not None:
        if indoor_temp_reading < TEMP_LOW:
            ac.turn_off()  # Turn off AC if temperature is too low
            print("Indoor temperature is too low. Turning off the air conditioner.")
        elif indoor_temp_reading > TEMP_HIGH:
            ac.turn_on()  # Turn on AC if temperature is too high
            print("Indoor temperature is too high. Turning on the air conditioner.")

    # Simulate light control based on presence detection (not implemented in your code, but we'll assume a placeholder)
    presence_detected = True  # Placeholder for actual presence detection logic
    if presence_detected:
        light.turn_on()
        print("Presence detected. Turning on the light.")
    else:
        light.turn_off()
        print("No presence detected. Turning off the light.")

if __name__ == "__main__":
    main()